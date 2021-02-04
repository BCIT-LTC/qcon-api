from rest_framework import serializers
from .models import QuestionLibrary, Transaction, Question
from django_q.tasks import async_task


def validate_file(value):
    if value.name.split(".")[1] != "docx":
        raise serializers.ValidationError("not a valid word file")


class UploadSerializer(serializers.Serializer):

    temp_file = serializers.FileField(
        validators=[validate_file], max_length=100, allow_empty_file=False, use_url=True)
    # section_name = serializers.CharField( max_length=100, allow_null=True, allow_blank=True, required=False)

    def create(self, validated_data):
        # newconversion = QuestionLibrary.objects.create(**validated_data)
        newtransaction = Transaction(user='qconweb')
        newtransaction.save()

        newconversion = QuestionLibrary.objects.create()
        newconversion.transaction = newtransaction
        # print("transaction " + str(newconversion.transaction))
        # print("qlibratry " + str(newtransaction.questionlibrary))
        newconversion.temp_file = validated_data.get(
            'temp_file', validated_data)
        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        # print(newconversion.section_name)

        newconversion.folder_path = '/code/temp/' + \
            str(newconversion.transaction)
        newconversion.image_path = newconversion.folder_path + '/media/'
        newconversion.create_directory()
        newconversion.save()
        async_task('api_v2.tasks.runconversion', newconversion)

        return newconversion.transaction

    def update(self, instance, validated_data):
        instance.temp_file = validated_data.get(
            'temp_file', instance.temp_file)
        instance.save()
        return instance


class SectionSerializer(serializers.Serializer):

    section_name = serializers.CharField(max_length=100, min_length=1)
    id = serializers.DecimalField(max_digits=8, decimal_places=0)

    # def create(self, validated_data):
    #     # newconversion = QuestionLibrary.objects.create(**validated_data)
    #     newconversion = QuestionLibrary.objects.create()
    #     newconversion.temp_file = validated_data.get('section_name', validated_data)
    #     newconversion.save()
    #     return newconversion

    def update(self, instance, validated_data):
        instance.section_name = validated_data.get(
            'section_name', instance.section_name)
        instance.id = validated_data.get('id', instance.id)
        instance.save()
        return instance



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['prefix', 'title', 'points', 'randomize_answer', 'question_type',
                  'question_body', 'question_feedback', 'hint', 'correct_answers_length', 'error']


class QuestionLibrarySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionLibrary
        fields = ['section_name', 'randomize_answer', 'error', 'questions']
