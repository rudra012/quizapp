from django.contrib import admin

from quiz.models import Question, Answer, QuizAttempt, Option


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "question"]
    list_display_links = ["question"]


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "option"]
    list_display_links = ["question"]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "option"]
    list_display_links = ["question"]


@admin.register(QuizAttempt)
class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ["id", "question", "option", "user", "is_correct"]
    list_display_links = ["question"]
