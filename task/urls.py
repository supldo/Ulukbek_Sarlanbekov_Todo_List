from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.TaskListAPIView.as_view()),
    path('tasks/create/', views.TaskCreateAPIView.as_view()),
    path('tasks/<int:id>/update/', views.TaskUpdateAPIView.as_view()),
    path('tasks/<int:id>/', views.TaskRetrieveAPIView.as_view()),
    path('tasks/<int:id>/delete/', views.TaskDestroyAPIView.as_view())
]