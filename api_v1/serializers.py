from rest_framework import serializers
from .models import QuestionLibrary
from django_q.tasks import async_task

def validate_file(value):
    if value.name.split(".")[1] != "docx":
        raise serializers.ValidationError("not a valid word file")


class UploadSerializer(serializers.Serializer):

    temp_file = serializers.FileField(validators=[validate_file], max_length=100,allow_empty_file=False,use_url=True)
    # section_name = serializers.CharField( max_length=100, allow_null=True, allow_blank=True, required=False)

    def create(self, validated_data):
        # newconversion = QuestionLibrary.objects.create(**validated_data)
        newconversion = QuestionLibrary.objects.create()
        newconversion.temp_file = validated_data.get('temp_file', validated_data)
        newconversion.section_name = newconversion.temp_file.name.split(".")[0]
        print(newconversion.section_name)

        newconversion.folder_path = '/code/temp/' + str(newconversion.id)
        newconversion.image_path = newconversion.folder_path + '/media/'
        newconversion.create_directory()
        newconversion.save()
        async_task('api_v1.tasks.runconversion', newconversion)




        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file =validated_data.get('temp_file', instance.temp_file)
        instance.save()
        return instance
    
class SectionSerializer(serializers.Serializer):


    def create(self, validated_data):
        # newconversion = QuestionLibrary.objects.create(**validated_data)
        newconversion = QuestionLibrary.objects.create()
        newconversion.temp_file = validated_data.get('section_name', validated_data)
        newconversion.save()
        return newconversion

    def update(self, instance, validated_data):
        instance.temp_file =validated_data.get('section_name', instance.temp_file)
        instance.save()
        return instance


class DownloadSerializer(serializers.Serializer):

    class Meta:
            model = QuestionLibrary
            fields = ['zip_file']