from rest_framework import serializers
from .models import QuizUser, UserAnswers


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = ['question', 'answer']


class QuizUserSerializer(serializers.ModelSerializer):
    user_answers = UserAnswersSerializer(many=True)

    class Meta:
        model = QuizUser
        fields = ['custom_user', 'quiz', 'user_answers']

    def create(self, validated_data):
        user_answers_data = validated_data.pop('user_answers')
        quiz_user = QuizUser.objects.create(**validated_data)
        for u in user_answers_data:
            UserAnswers.objects.create(
                quiz_user=quiz_user,
                **u
            )
        return quiz_user
