from django.urls import path
from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, StatusListView, StatusCreateView, StatusUpdateView, StatusDeleteView

urlpatterns = [
    path('', UserListView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('statuses/', StatusListView.as_view(), name='statuses'),
    path('statuses/create/', StatusCreateView.as_view(), name='status_create'),
    path('statuses/<int:pk>/update/', StatusUpdateView.as_view(), name='status_update'),
    path('statuses/<int:pk>/delete/', StatusDeleteView.as_view(), name='status_delete'),
]