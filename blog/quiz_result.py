from rest_framework import generics, serializers, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Quiz, Question, Answer, QuizResult


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)

    class Meta:
        model = Question
        fields = '__all__'


class QuizResultSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = QuizResult
        fields = ('id', 'user', 'quiz', 'start_time', 'end_time', 'is_completed', 'result')

    def create(self, validated_data):
        quiz = validated_data['quiz']
        quiz_result = QuizResult.objects.create(**validated_data)
        quiz_result.questions.set(quiz.quiz_questions.all())
        quiz_result.current_question = quiz.quiz_questions.first()
        quiz_result.save()
        return quiz_result


class QuizStartView(generics.CreateAPIView):
    serializer_class = QuizResultSerializer

    def post(self, request, *args, **kwargs):
        quiz_id = request.data.get('quiz_id')
        quiz = Quiz.objects.get(id=quiz_id)
        quiz_result = QuizResult.objects.filter(user=request.user, quiz=quiz, is_completed=False).first()
        if quiz_result:
            # The user has already started the quiz, return the current question
            serializer = QuizResultSerializer(quiz_result)
            return Response(serializer.data)

        # Create a new quiz result
        quiz_result_serializer = self.get_serializer(data=request.data)
        quiz_result_serializer.is_valid(raise_exception=True)
        quiz_result_serializer.save()
        serializer = QuizResultSerializer(quiz_result_serializer.instance)
        return Response(serializer.data)


class QuizNextQuestionView(generics.UpdateAPIView):
    serializer_class = QuizResultSerializer

    def put(self, request, *args, **kwargs):
        quiz_result = self.get_object()
        quiz = quiz_result.quiz
        question_id = request.data.get('question_id')
        answer_ids = request.data.get('answer_ids', [])
        current_question = quiz_result.current_question
        if current_question.id != question_id:
            return Response({'error': 'Invalid question id'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the answer is correct
        correct_answers = current_question.question_answers.filter(correct=True)
        correct_answer_ids = [str(answer.id) for answer in correct_answers]
        is_correct = set(answer_ids) == set(correct_answer_ids)
        # Save the answer result
        quiz_result.result[current_question.id] = {'is_correct': is_correct, 'selected_answers': answer_ids}
        quiz_result.save()

        # Get the next question or complete the quiz
        next_question = quiz.quiz_questions.filter(id__gt=current_question.id).first()
        if not next_question:
            quiz_result.is_completed = True
            quiz_result.end_time = timezone.now()
            quiz_result.save()
            serializer = QuizResultSerializer(quiz_result)
            return Response(serializer.data)

        # Update the current question
        quiz_result.current_question = next_question
        quiz_result.save()
        serializer = QuizResultSerializer(quiz_result)
        return Response(serializer.data)


class QuizResultDetailView(generics.RetrieveAPIView):
    serializer_class = QuizResultSerializer
    queryset = QuizResult
