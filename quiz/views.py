from django.shortcuts import render
from django.views import View

from .forms import QuizForm
from .models import Quiz, Question


class IndexView(View):
    form_class = QuizForm
    initial = {'key': 'value'}
    template_name = 'quiz/index.html'

    def get(self, request, *args, **kwargs):
        quiz_list = Quiz.objects.all()
        ctx = {'quiz_list': quiz_list}
        return render(request, self.template_name, ctx)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})


class QuizView(View):
    form_class = QuizForm
    initial = {'key': 'value'}
    template_name = 'quiz/quiz.html'

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        question_list = Question.objects.filter(quiz_id=kwargs.get("quiz_id"))
        ctx = {'question_list': question_list}
        print(ctx, kwargs.get("quiz_id"))
        return render(request, self.template_name, ctx)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
    #
    #     return render(request, self.template_name, {'form': form})
