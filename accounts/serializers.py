from rest_framework import serializers
from .models import CustomUser,  SatisfactionSurvey, Recognition, Kaizen

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'role', 'full_name']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data.get('role', 2),
            full_name=validated_data('full_name')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class SatisfactionSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = SatisfactionSurvey
        fields = '__all__'
        
        
class RecognitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recognition
        fields = '__all__'

class KaizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kaizen
        fields = '__all__'