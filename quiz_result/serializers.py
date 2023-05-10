from rest_framework import serializers
from .models import QuizUser, UserAnswers


class UserAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAnswers
        fields = ['question', 'answer']


class QuizUserSerializer(serializers.ModelSerializer):
    user_answers = UserAnswersSerializer(many=True)
    current_answer = UserAnswersSerializer(many=True, read_only=True)

    class Meta:
        model = QuizUser
        fields = ['custom_user', 'quiz', 'user_answers', 'current_answer', 'current_answer_count']
        extra_kwargs = {
            'current_answer': {'read_only': True},
            'current_answer_count': {'read_only': True},
        }

    def create(self, validated_data):
        user_answers_data = validated_data.pop('user_answers')
        quiz_user = QuizUser.objects.create(**validated_data)
        for u in user_answers_data:
            UserAnswers.objects.create(
                quiz_user=quiz_user,
                **u
            )
        return quiz_user
