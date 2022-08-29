
from django.urls import path
from .views import *

urlpatterns = [
    path('list/', TaskListView.as_view(), name='tasks'),
    path('list/<int:user_id>/', TaskListUserView.as_view(),name='tasks'),
    path('delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),
    path('detail/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('new/', TaskCreateView.as_view(), name='task_new'),
]