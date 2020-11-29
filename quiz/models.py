from django.db import models

from users.models import User, BaseModel


class Quiz(BaseModel):
    name = models.CharField(max_length=200, )

    def __str__(self):
        return self.name


class Question(BaseModel):
    question = models.CharField(max_length=200, )
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.question


class Option(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    option = models.CharField(max_length=100, )

    def __str__(self):
        return f"{self.option}"


class Answer(BaseModel):
    question = models.OneToOneField(Question, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)


class QuizAttempt(BaseModel):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL, null=True)
    option = models.ForeignKey(Option, on_delete=models.SET_NULL, null=True)

    class Meta:
        unique_together = ('user', 'question',)

    @property
    def is_correct(self):
        return self.option == Answer.objects.get(question=self.question).option
