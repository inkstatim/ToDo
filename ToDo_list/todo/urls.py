from django.urls import path
from .views import TaskListView, TaskCreateView, TaskDeleteView, TaskUpdateView, TaskDetailView

app_name = 'todo'
urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('create/', TaskCreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
]
