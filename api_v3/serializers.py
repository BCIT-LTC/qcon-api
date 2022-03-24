# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from rest_framework import serializers
from .models import DocumentError, Matching, MatchingAnswer, MatchingChoice, Ordering, QuestionError, QuestionLibrary, Section, Question, MultipleChoice, MultipleChoiceAnswer, TrueFalse, Fib, MultipleSelect, MultipleSelectAnswer, WrittenResponse
from django.conf import settings


def validate_docx_file(value):
    if value.name.split(".")[1] != "docx":
        raise serializers.ValidationError("not a valid word file")


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
        
        newconversion.main_title = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_main_title()
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
    json_data = serializers.JSONField(initial=dict)

    def create(self, validated_data):
        newconversion = QuestionLibrary.objects.create()
        newconversion.json_data = validated_data.get('json_data', validated_data)
        
        newconversion.folder_path = settings.MEDIA_ROOT + str(newconversion.id)
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
        # print("newconversion.create_xml_files()--------------------------------------")
        # newconversion.create_xml_files()
        # print("newconversion.zip_files()--------------------------------------")
        #     # ===========  6  ==================
        # newconversion.zip_files()

        return newconversion

    # def update(self, instance, validated_data):
    #     instance.temp_file = validated_data.get('temp_file',
    #                                             instance.temp_file)
    #     instance.save()
    #     return instance

class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultipleChoiceAnswer
        fields = ['answer', 'answer_feedback', 'weight']



class MultipleChoiceSerializer(serializers.ModelSerializer):
    multiple_choice_answers = MultipleChoiceAnswerSerializer(many=True,allow_null=True)

    class Meta:
        model = MultipleChoice
        fields = ['randomize', 'enumeration', 'multiple_choice_answers']


class TrueFalseSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrueFalse
        fields = ['true_weight', 'true_feedback', 'false_weight', 'false_feedback', 'enumeration']


class FibSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fib
        fields = ['type', 'text', 'order', 'size', 'weight']


class OrderingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ordering
        fields = ['text', 'order', 'ord_feedback']


class MultipleSelectAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = MultipleSelectAnswer
        fields = ['answer', 'answer_feedback', 'is_correct']


class MultipleSelectSerializer(serializers.ModelSerializer):
    multiple_select_answers = MultipleSelectAnswerSerializer(many=True,allow_null=True)

    class Meta:
        model = MultipleSelect
        fields = ['randomize', 'enumeration', 'style', 'grading_type', 'multiple_select_answers']


class MatchingAnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = MatchingAnswer
        fields = ['answer_text']

class MatchingChoiceSerializer(serializers.ModelSerializer):
    matching_answers = MatchingAnswersSerializer(many=True,allow_null=True)

    class Meta:
        model = MatchingChoice
        fields = ['choice_text', 'matching_answers']

class MatchingSerializer(serializers.ModelSerializer):
    matching_choices = MatchingChoiceSerializer(many=True,allow_null=True)

    class Meta:
        model = Matching
        fields = ['grading_type', 'matching_choices']


class WrittenResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = WrittenResponse
        fields = ['enable_student_editor', 'initial_text', 'answer_key', 'enable_attachments']


class QuestionSerializer(serializers.ModelSerializer):
    multiple_choice = MultipleChoiceSerializer(many=True, allow_null=True)
    true_false = TrueFalseSerializer(many=True, allow_null=True)
    fib = FibSerializer(many=True, allow_null=True)
    multiple_select = MultipleSelectSerializer(many=True, allow_null=True)
    matching = MatchingSerializer(many=True, allow_null=True)
    ordering = OrderingSerializer(many=True, allow_null=True)
    written_response = WrittenResponseSerializer(many=True, allow_null=True)

    class Meta:
        model = Question
        fields = ['title', 'text', 'points', 'difficulty', 'mandatory', 'hint', 'feedback', 'multiple_choice', 'true_false', 'fib', 'multiple_select', 'matching', 'ordering', 'written_response']


class SectionSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True,allow_null=True)

    class Meta:
        model = Section
        fields = ['is_main_content', 'title', 'is_title_displayed', 'text', 'is_text_displayed', 'shuffle', 'questions']


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
            'main_title', 'total_question_errors',
            'total_document_errors', 'document_errors', 'questions'
        ]

class QuestionLibrarySerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True,allow_null=True)
    # documenterrors = DocumentErrorSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionLibrary
        fields = [
            'main_title', 'randomize_answer', 'total_question_errors',
            'total_document_errors', 'sections'
        ]

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        question_library_instance = QuestionLibrary.objects.create(**validated_data)

        for section in sections_data:
            questions_data = section.pop('questions')
            section_instance = Section.objects.create(question_library=question_library_instance, **section)

            for question in questions_data:
                mc_data = question.pop('multiple_choice')
                tf_data = question.pop('true_false')
                fib_data = question.pop('fib')
                ms_data = question.pop('multiple_select')
                mat_data = question.pop('matching')
                ord_data = question.pop('ordering')
                wr_data = question.pop('written_response')

                question_instance = Question.objects.create(section=section_instance, **question)

                if mc_data:
                    for multiple_choice in mc_data:
                        mc_answers_data = multiple_choice.pop('multiple_choice_answers')
                        mc_instance = MultipleChoice.objects.create(question=question_instance, **multiple_choice)

                        for mc_answers in mc_answers_data:
                            mc_answers_instance = MultipleChoiceAnswer.objects.create(multiple_choice=mc_instance, **mc_answers)
                
                
                if tf_data:
                    for true_false in tf_data:
                        tf_instance = TrueFalse.objects.create(question=question_instance, **true_false)


                if fib_data:
                    for fib_item in fib_data:
                        fib_item_instance = Fib.objects.create(question=question_instance, **fib_item)


                if ms_data:
                    for multiple_select in ms_data:
                        ms_answers_data = multiple_select.pop('multiple_select_answers')
                        ms_instance = MultipleSelect.objects.create(question=question_instance, **multiple_select)

                        for ms_answers in ms_answers_data:
                            ms_answers_instance = MultipleSelectAnswer.objects.create(multiple_select=ms_instance, **ms_answers)


                if mat_data:
                    for matching in mat_data:
                        mat_choices_data = matching.pop('matching_choices')
                        
                        matching_instance = Matching.objects.create(question=question_instance, **matching)

                        for mat_choice_item in mat_choices_data:
                            mat_answers_data = mat_choice_item.pop('matching_answers')
                            mat_choice_item_instance = MatchingChoice.objects.create(matching=matching_instance, **mat_choice_item)

                            for mat_answer_item in mat_answers_data:
                                mat_answer_item_instance = MatchingAnswer.objects.create(matching_choice=mat_choice_item_instance, **mat_answer_item)


                if ord_data:
                    for ord_item in ord_data:
                        ord_item_instance = Ordering.objects.create(question=question_instance, **ord_item)


                if wr_data:
                    for written_response in wr_data:
                        wr_instance = WrittenResponse.objects.create(question=question_instance, **written_response)
                
        return question_library_instance


# class QuestionErrorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuestionError
#         fields = ['message', 'action', 'errortype']


# class DocumentErrorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = QuestionError
#         fields = ['message', 'action', 'errortype']



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