# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from rest_framework import serializers
from .models import DocumentError, QuestionError, QuestionLibrary, Section, Question, MultipleChoice, MultipleChoiceAnswer, TrueFalse, Fib, MultipleSelect, MultipleSelectAnswer, WrittenResponse
from django.conf import settings


def validate_docx_file(value):
    if value.name.split(".")[1] != "docx":
        raise serializers.ValidationError("not a valid word file")

def validate_json_file(value):
    if value.name.split(".")[1] != "json":
        raise serializers.ValidationError("not a valid json file")

def count_errors(questionlibrary):
    # COUNT NUMBER OF DOCUMENT ERRORS
    doc_errorlist = DocumentError.objects.filter(document=questionlibrary)
    questionlibrary.total_document_errors = doc_errorlist.count()

    # COUNT NUMBER OF QUESTION ERRORS
    question_list = Question.objects.filter(question_library=questionlibrary)
    num_question_errors = 0
    for q in question_list:
        q_errorlist = QuestionError.objects.filter(question=q)
        num_question_errors += q_errorlist.count()    
    questionlibrary.total_question_errors = num_question_errors
    questionlibrary.save()


class WordToJsonSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_docx_file],
                                      max_length=100,
                                      allow_empty_file=False,
                                      use_url=True)

    randomize = serializers.BooleanField(default=False)
    
    def create(self, validated_data):
        newconversion = QuestionLibrary.objects.create()
        newconversion.temp_file = validated_data.get('temp_file',
                                                     validated_data)
        
        newconversion.randomize_answer = validated_data.get(
            'randomize', validated_data)
        
        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_section_name()
        newconversion.folder_path = settings.MEDIA_ROOT + \
            str(newconversion.id)
        newconversion.image_path = newconversion.folder_path + settings.MEDIA_URL
        newconversion.create_directory()
        newconversion.save()

        newconversion.create_pandocstring()
        newconversion.save()
        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get('temp_file',
                                                instance.temp_file)
        instance.save()
        return instance


class JsonToScormSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_json_file],
                                      max_length=100,
                                      allow_empty_file=False,
                                      use_url=True)

    randomize = serializers.BooleanField(default=False)

    def create(self, validated_data):
        newconversion = QuestionLibrary.objects.create()
        newconversion.temp_file = validated_data.get('temp_file',
                                                     validated_data)

        newconversion.randomize_answer = validated_data.get(
            'randomize', validated_data)

        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_section_name()
        newconversion.folder_path = settings.MEDIA_ROOT + \
            str(newconversion.id)
        newconversion.image_path = newconversion.folder_path + settings.MEDIA_URL
        newconversion.create_directory()
        newconversion.save()

        import logging
        logger = logging.getLogger(__name__)

        logger.info(
            "[" + str(newconversion.id) + "] " +
            "<<<<<<<<<<Transaction Started<<<<<<<<<<")
        # ===========  1  ==================
        # newconversion.create_pandocstring()
        # ===========  2  ==================
        # newconversion.run_parser()

        # count_errors(newconversion)

        # if newconversion.total_document_errors == 0:
        #     # ===========  3, 4, 5  ==================
        newconversion.create_xml_files()
        #     # ===========  6  ==================
        newconversion.zip_files()

        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get('temp_file',
                                                instance.temp_file)
        instance.save()
        return instance

class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultipleChoiceAnswer
        fields = ['answer', 'answer_feedback', 'weight']



class MultipleChoiceSerializer(serializers.ModelSerializer):
    multiple_choices = MultipleChoiceAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = MultipleChoice
        fields = ['randomize', 'enumeration']


class TrueFalseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrueFalse
        fields = ['true_weight', 'true_feedback', 'false_weight', 'false_feedback', 'enumeration']


class FibSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fib
        fields = ['type', 'text', 'order', 'size', 'weight']


class MultipleSelectAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultipleSelectAnswer
        fields = ['answer', 'answer_feedback', 'is_correct']


class MultipleSelectSerializer(serializers.ModelSerializer):
    multiple_selects = MultipleSelectAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = MultipleSelect
        fields = ['randomize', 'enumeration', 'style', 'grading_type']


class WrittenResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WrittenResponse
        fields = ['enable_student_editor', 'initial_text', 'answer_key', 'enable_attachments']


class QuestionSerializer(serializers.ModelSerializer):
    multiple_choices = MultipleChoiceSerializer(many=True, read_only=True)
    true_false = TrueFalseSerializer(many=True, read_only=True)
    fibs = FibSerializer(many=True, read_only=True)
    multiple_selects = MultipleSelectSerializer(many=True, read_only=True)
    written_responses = WrittenResponseSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionLibrary
        fields = ['title', 'text', 'point', 'difficulty', 'mandatory', 'hint', 'feedback']


class SectionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionLibrary
        fields = ['validated', 'finished_processing', 'raw_data', 'questions_processed', 'questions_expected', 'title', 'is_title_displayed', 'text', 'is_text_displayed', 'shuffle']


class QuestionErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionError
        fields = ['error_type', 'message', 'action']


class DocumentErrorSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionError
        fields = ['error_type', 'message', 'action']


class QuestionErrorSummarySerializer(serializers.ModelSerializer):
    question_errors = QuestionErrorSerializer(many=True, read_only=True)
   
    class Meta:
        model = Question
        fields = [
            'prefix', 'question_errors'
        ]

class QuestionLibraryErrorSummarySerializer(serializers.ModelSerializer):
    document_errors = DocumentErrorSerializer(many=True, read_only=True)
    questions = serializers.SerializerMethodField('get_questions')

    def get_questions(self, questionlibrary):        
        question_list = Question.objects.filter(question_library=questionlibrary)
        filtered_question_list_ids = []
        for q in question_list:
            q_errorlist = QuestionError.objects.filter(question=q)
            if q_errorlist.count() > 0:
                filtered_question_list_ids.append(q.id)
        filtered_question_list_queryset = question_list.filter(id__in=filtered_question_list_ids)
        serializer = QuestionErrorSummarySerializer(instance=filtered_question_list_queryset, many=True, read_only=True)
        return serializer.data
    class Meta:
        model = QuestionLibrary
        fields = [
            'section_name', 'total_question_errors',
            'total_document_errors', 'document_errors', 'questions'
        ]

class QuestionLibrarySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)
    document_errors = DocumentErrorSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionLibrary
        fields = [
            'section_name', 'randomize_answer', 'total_question_errors',
            'total_document_errors', 'document_errors', 'questions'
        ]





class StatusResponseSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    app_description = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    version_number = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    build_hash = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    build_short_sha = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    build_date = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    cluster_name = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    build_env = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)
    app_tagline = serializers.CharField(max_length=None, min_length=None, allow_blank=True, trim_whitespace=True)