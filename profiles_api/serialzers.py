from rest_framework import serializers
from profiles_api import models


class HelloSerializer(serializers.Serializer):
    """Serialzers a name field for testing our ApiView"""
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'},
            }
        }

    def create(self, validated_data):
        """Create and return User """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user


class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """serializers profile feed items"""

    class Meta: 
        model = models.ProfileFeedItem
        fields = ('id','user_profile','status_text','created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
