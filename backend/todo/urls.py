from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonViewSet, ToDoViewSet
app_name='todo'
router = DefaultRouter()
router.register(r'persons', PersonViewSet)
router.register(r'todos', ToDoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
