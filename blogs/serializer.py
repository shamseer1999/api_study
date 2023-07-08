from rest_framework import serializers

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    phone = serializers.CharField()
    place = serializers.CharField()
    
class BlogSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    sub_title = serializers.CharField()
    author = serializers.CharField()
    published_date = serializers.DateField()
    created_at = serializers.DateTimeField()