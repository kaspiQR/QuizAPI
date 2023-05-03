from django.db import models


class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    @property
    def count_questions(self):
        """
        Метод count_questions возвращает количество
        вопросов связанных к этому тесту
        """
        return self.quiz_questions.all().count()
        # return Question.objects.filter(quiz=self).count()

    def __str__(self):
        return self.title


class Question(models.Model):
    title = models.CharField(max_length=255)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,
                             related_name='quiz_questions')

    @property
    def count_answers(self):
        """
        Метод count_questions возвращает количество
        вопросов связанных к этому тесту
        """
        return self.question_answers.all().count()

    @property
    def count_correct_answers(self):
        """
        Метод count_questions возвращает количество
        вопросов связанных к этому тесту
        """
        return self.question_answers.filter(correct=True).count()

    def __str__(self):
        return f"{self.quiz.title} - {self.title}"


class Answer(models.Model):
    title = models.CharField(max_length=255)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 related_name='question_answers')

    def __str__(self):
        return self.title
