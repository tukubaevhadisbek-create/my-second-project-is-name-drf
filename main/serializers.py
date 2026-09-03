from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import (
    Employer,
    Category,
    Vacancy,
    Applicant,
    Resume,
    Favorite,
    Application
)
class Register(serializers.ModelSerializer):
    username = serializers.CharField(max_length = 150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=['applicant','employer'])

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'role'
        ]

    def create(self,validated_data):
        role = validated_data.pop('role')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        if role == 'employer':
            Employer.objects.create(
                user=user,
                company_name='',
                city=''
            )

        elif role == 'applicant':
            Applicant.objects.create(
                user=user,
                city=''
            )

        return user

class LoginSerialiser(serializers.Serializer):
    username = serializers.CharField(max_length = 150)
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        user = authenticate(
            username = data['username'],
            password = data['password']
        )
        if user is None:
            raise serializers.ValidationError(
                'Invalid password or username'
            )

        data['user'] = user
        return data

class ApplicantSerialisers(serializers.ModelSerializer):

    class Meta:
        model = Applicant
        fields = '__all__'

class ResumeSerialisers(serializers.ModelSerializer):

    class Meta:
        model = Resume
        fields = '__all__'

        
class VacancySerialisers(serializers.ModelSerializer):

    class Meta:
        model = Vacancy
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

class EmployerSerialisers(serializers.ModelSerializer):

    class Meta:
        model = Employer
        fields = '__all__'

class FavoriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorite
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

class ApplicationSerializers(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['applicant', 'created_at']
