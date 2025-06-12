from .views import UserListView, UserCreateView, UserUpdateView, UserDeleteView
from django.urls import path, include
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [

    path('', UserListView.as_view(), name='index'),


    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', UserCreateView.as_view(), name='create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='delete'),
]