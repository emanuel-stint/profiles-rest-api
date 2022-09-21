from rest_framework import serializers
from profiles_api import models


class TestSerializer(serializers.Serializer):
    """Serializes a name field for testing TestApiView"""

    name = serializers.CharField(max_length=5)

# Whats happening here -> we call this serializwer, it validates entries defined and then calls the custom create function below


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializers a user profile object"""

    # meta class to point at particular model
    # list fields we want accessible in serializer

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        # bear in mind, we would like to make password write only
        extra_kwargs = {
            'password': {
                'write_only': True,
                # add custom style to not see password when you type
                'style': {'input_type': 'password'}
            }
        }

    # bear in mind model serializer by default uses defautl create user, but we want to override this
    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """Handle updating user account - total update"""

        # default behaviour by model serializer is to take whateevr fields passed to them and pass them directly to model
        # fine for many fields except password for example, which requires additional logic to hash/encrpyt them before saving update
        # function below basically pops the password from validated data, then hashes it using set_password from the framework
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
