from django.db import models

from blog.models import Quiz, Question, Answer
from users.models import CustomUser


class QuizUser(models.Model):
    custom_user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    time_start = models.DateTimeField(auto_now_add=True)
    time_end = models.DateTimeField(auto_now_add=True)

    @property
    def current_answer(self):
        pass

    def __str__(self):
        return f"{self.custom_user.username}:{self.quiz.title}"


class UserAnswers(models.Model):
    quiz_user = models.ForeignKey(QuizUser, on_delete=models.CASCADE,
                                  related_name="user_answers")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    @property
    def correct_answer(self) -> bool:
        return self.answer.correct

