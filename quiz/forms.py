from django import forms

from quiz.models import QuizAttempt, Quiz


class QuizForm(forms.Form):
    class Meta:
        model = Quiz
        fields = ["id", 'name', ]


class QuizAttemptForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)

    class Meta:
        model = QuizAttempt
        fields = ['question', 'option', ]
