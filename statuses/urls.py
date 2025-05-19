from django.urls import path
from statuses.views import (
    StatusListView,
    StatusUpdateView,
    StatusDeleteView,
    StatusCreateView

)

urlpatterns = [
    path('', StatusListView.as_view(), name='statuses'),
    path('create/', StatusCreateView.as_view(), name='new_status'),
    path('<int:pk>/update/', StatusUpdateView.as_view(), name='edit_status'),
    path('<int:pk>/delete/', StatusDeleteView.as_view(),
         name='drop_status'),
    ]