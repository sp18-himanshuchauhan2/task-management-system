from django.urls import path
from .views import register_user, login_user, TaskListCreateView, TaskDetailView, TaskTimelineView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
      path('tasks/timeline/', TaskTimelineView.as_view(), name='task-timeline'),
]
