from rest_framework import serializers
from .models import Quiz, Question, Answer


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'title', 'description', 'count_questions']
        extra_kwargs = {
            'count_questions': {'read_only': True}
        }


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = ['id', 'title', 'correct', 'question']
        extra_kwargs = {
            'question': {'read_only': True}
        }


class GetAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title']


class QuestionSerializer(serializers.ModelSerializer):
    question_answers = GetAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'quiz', 'count_answers', 'count_correct_answers', 'question_answers']
