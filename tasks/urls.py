from django.urls import path

from . import views
from .views import TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskDetailView, index

app_name = 'tasks'

urlpatterns = [
    path('', TaskListView.as_view(), name='index'),
    path('index/', views.index),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/', TaskDetailView.as_view(), name='detail'),
]