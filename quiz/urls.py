from django.urls import path

from . import views

urlpatterns = [
    # ex: /quiz/
    path('', views.IndexView.as_view(), name='index'),
    # # ex: /quiz/5/
    path('<int:quiz_id>/', views.QuizView.as_view(), name='quiz_detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
