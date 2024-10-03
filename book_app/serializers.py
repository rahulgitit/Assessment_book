from rest_framework import serializers
from book_app.models import Book
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSignupSerialier(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
            )
        return user
        
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, data):
        user = authenticate(**data)
        if user is None:
            raise serializers.ValidationError('Invalid credentials')
        return data


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields="__all__"


