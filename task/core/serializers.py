from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"

    # class Meta:
    #     model = File
    #     fields = ('id', 'name', 'file', 'created_at')
    #     read_only_fields = ('id', 'created_at')
    #     extra_kwargs = {
    #         'file': {'write_only': True}
    #     }

    # def create(self, validated_data):
    #     file = File.objects.create(**validated_data)
    #     return file
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.file = validated_data.get('file', instance.file)
    #     instance.save()
    #     return instance
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     representation['file_url'] = instance.file.url
    #     return representation
    
    # def to_internal_value(self, data):
    #     return super().to_internal_value(data)
    
    # def to_native_value(self, data):
    #     return super().to_native_value(data)
    