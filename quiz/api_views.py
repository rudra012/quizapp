from rest_framework import viewsets, generics, mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from quiz.models import Quiz, Question
from quiz.serializer import QuizSerializer, QuestionSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for Quiz related operations
    """
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    # permission_classes = [IsAccountAdminOrReadOnly]

    @action(methods=['get'], detail=True, )
    def get_questions(self, request, pk=None):
        print(pk)
        queryset = Question.objects.filter(quiz_id=pk)
        print(queryset)
        serializer = QuestionSerializer(queryset, many=True)
        return Response(serializer.data)


class QuestionsViewSet(mixins.ListModelMixin, GenericViewSet):
    """
    A ViewSet for Quiz details related operations
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        print(args, kwargs)
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
