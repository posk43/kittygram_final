"""Brief description of YourClass."""
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Achievement, Cat
from .serializers import AchievementSerializer, CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Brief description of YourClass."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    pagination_class = PageNumberPagination
    """Brief description of YourClass."""

    def perform_create(self, serializer):
        """Brief description of YourClass."""
        serializer.save(owner=self.request.user)


class AchievementViewSet(viewsets.ModelViewSet):
    """Brief description of YourClass."""

    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    pagination_class = None
