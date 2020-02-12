from rest_framework import serializers
from .models import Post, Profile

''' Post serializers'''

class PostSerializer(serializers.ModelSerializer):
    likes_num = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ('id', 'image_caption', 'image', 'author', 'likes_num', 'likes')

    def get_likes_num(self, obj):
        return obj.likes.all().count()

class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'image')

    def get_likes_num(self, obj):
        return obj.likes.all().count()

''' Profile serializers'''

class ProfileSerializer(serializers.ModelSerializer):
    follows = serializers.SerializerMethodField()
    followers = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'password', 'username', 'last_name', 'first_name', 'email', 'is_superuser', 'follows', 'followers')

    def get_follows(self, obj):
        return obj.follows.all().count()

    def get_followers(self, obj):
        return obj.followers.all().count()

    def create(self, validated_data):
        password = validated_data.pop('password')

        # crypts the password in the database
        user_obj = Profile(**validated_data)
        user_obj.set_password(password)
        user_obj.save()

        return user_obj
