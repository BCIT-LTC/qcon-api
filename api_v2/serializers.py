from rest_framework import serializers
from .models import QuestionLibrary, Transaction, Question, Answer, Fib
from django.conf import settings
# from django_q.tasks import async_task


def validate_file(value):
    if value.name.split(".")[1] != "docx":
        raise serializers.ValidationError("not a valid word file")


class UploadSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_file],
                                      max_length=100,
                                      allow_empty_file=False,
                                      use_url=True)

    # section_name = serializers.CharField( max_length=100, allow_null=True, allow_blank=True, required=False)

    def create(self, validated_data):
        # newconversion = QuestionLibrary.objects.create(**validated_data)
        newtransaction = Transaction(client='qconweb')
        newtransaction.save()

        newconversion = QuestionLibrary.objects.create()
        newconversion.transaction = newtransaction
        # print("transaction " + str(newconversion.transaction))
        # print("qlibratry " + str(newtransaction.questionlibrary))
        newconversion.temp_file = validated_data.get('temp_file',
                                                     validated_data)
        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_section_name()
        # print(newconversion.section_name)

        newconversion.folder_path = settings.MEDIA_ROOT + \
            str(newconversion.transaction)
        newconversion.image_path = newconversion.folder_path + '/assessment-assets/' + newconversion.filtered_section_name + '/'
        newconversion.create_directory()
        newconversion.save()
        # async_task('api_v2.tasks.runconversion', newconversion)

        return newconversion.transaction

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get('temp_file',
                                                instance.temp_file)
        instance.save()
        return instance


class WordToZipSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_file],
                                      max_length=100,
                                      allow_empty_file=False,
                                      use_url=True)

    randomize = serializers.BooleanField(default=False)

    def create(self, validated_data):
        newtransaction = Transaction(client='qconweb')
        newtransaction.save()
        newconversion = QuestionLibrary.objects.create()
        newconversion.transaction = newtransaction
        newconversion.temp_file = validated_data.get('temp_file',
                                                     validated_data)

        newconversion.randomize_answer = validated_data.get(
            'randomize', validated_data)
            
        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_section_name()
        newconversion.folder_path = settings.MEDIA_ROOT + \
            str(newconversion.transaction)
        newconversion.image_path = newconversion.folder_path + '/assessment-assets/' + newconversion.filtered_section_name + '/'
        newconversion.create_directory()
        newconversion.save()

        import logging
        WordToZipSerializer_Logger = logging.getLogger(
            'api_v2.serializers.WordToZipSerializer')

        WordToZipSerializer_Logger.info(
            "[" + str(newtransaction) + "] " +
            "<<<<<<<<<<Transaction Started<<<<<<<<<<")
        # ===========  1  ==================
        newconversion.create_pandocstring()
        # ===========  2  ==================
        newconversion.run_parser()
        # ===========  3, 4, 5  ==================
        newconversion.create_xml_files()
        # ===========  6  ==================
        newconversion.zip_files()

        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get('temp_file',
                                                instance.temp_file)
        instance.save()
        return instance


class WordToJsonZipSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_file],
                                      max_length=100,
                                      allow_empty_file=False,
                                      use_url=True)

    randomize = serializers.BooleanField(default=False)

    def create(self, validated_data):
        newtransaction = Transaction(client='qconweb')
        newtransaction.save()
        newconversion = QuestionLibrary.objects.create()
        newconversion.transaction = newtransaction
        newconversion.temp_file = validated_data.get('temp_file',
                                                     validated_data)

        newconversion.randomize_answer = validated_data.get(
            'randomize', validated_data)

        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_section_name()
        newconversion.folder_path = settings.MEDIA_ROOT + \
            str(newconversion.transaction)
        # This might be replaced if User enter section name on the form or have H1 inside the document
        newconversion.image_path = newconversion.folder_path + '/assessment-assets/' + newconversion.filtered_section_name + '/'
        newconversion.create_directory()
        newconversion.save()

        import logging
        WordToJsonZipSerializer_Logger = logging.getLogger(
            'api_v2.serializers.WordToJsonZipSerializer')

        WordToJsonZipSerializer_Logger.info(
            "[" + str(newtransaction) + "] " +
            "<<<<<<<<<<Transaction Started<<<<<<<<<<")
        # ===========  1  ==================
        newconversion.create_pandocstring()
        # ===========  2  ==================
        newconversion.run_parser()
        # ===========  3, 4, 5  ==================
        newconversion.create_xml_files()
        # ===========  6  ==================
        newconversion.zip_files()
        # ===========  7  ==================

        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get('temp_file',
                                                instance.temp_file)
        instance.save()
        return instance


class WordToJsonSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_file],
                                      max_length=100,
                                      allow_empty_file=False,
                                      use_url=True)

    def create(self, validated_data):
        newtransaction = Transaction(client='qconweb')
        newtransaction.save()
        newconversion = QuestionLibrary.objects.create()
        newconversion.transaction = newtransaction
        newconversion.temp_file = validated_data.get('temp_file',
                                                     validated_data)
        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        newconversion.filter_section_name()
        newconversion.folder_path = settings.MEDIA_ROOT + \
            str(newconversion.transaction)
        newconversion.image_path = newconversion.folder_path + '/assessment-assets/' + newconversion.filtered_section_name + '/'
        newconversion.create_directory()
        newconversion.save()

        # ===========  1  ==================
        newconversion.create_pandocstring()
        # ===========  2  ==================
        newconversion.run_parser()

        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get('temp_file',
                                                instance.temp_file)
        instance.save()
        return instance


# class SectionSerializer(serializers.Serializer):

#     section_name = serializers.CharField(max_length=100, min_length=1)
#     id = serializers.DecimalField(max_digits=8, decimal_places=0)

#     # def create(self, validated_data):
#     #     # newconversion = QuestionLibrary.objects.create(**validated_data)
#     #     newconversion = QuestionLibrary.objects.create()
#     #     newconversion.temp_file = validated_data.get('section_name', validated_data)
#     #     newconversion.save()
#     #     return newconversion

#     def update(self, instance, validated_data):
#         instance.section_name = validated_data.get(
#             'section_name', instance.section_name)
#         instance.id = validated_data.get('id', instance.id)
#         instance.save()
#         return instance


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'progress']


class FibSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fib
        fields = ['type', 'text', 'order']


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = [
            'prefix', 'answer_body', 'answer_feedback', 'is_correct',
            'match_left', 'match_right', 'order'
        ]


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    fib = FibSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [
            'prefix', 'title', 'points', 'randomize_answer', 'question_type',
            'question_body', 'question_feedback', 'hint',
            'correct_answers_length', 'error', 'answers', 'fib'
        ]


class QuestionLibrarySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionLibrary
        fields = ['section_name', 'randomize_answer', 'error', 'questions']
