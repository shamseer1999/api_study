from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    phone = serializers.CharField()
    place = serializers.CharField()
    
    def create(self,validated_data):
        return Authors.objects.create(**validated_data)
    
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    sub_title = serializers.CharField()
    author = serializers.PrimaryKeyRelatedField(queryset=Authors.objects.all())
    published_date = serializers.DateField()
    created_at = serializers.DateTimeField()
    
    def create(self,validated_data):
        return Blog.objects.create(**validated_data)