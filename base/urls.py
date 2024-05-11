from django.urls import path
from .views import task_list, task_detail, task_create, task_update, task_delete
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import signup
from .views import logout_view

urlpatterns = [
    path('accounts/profile/', task_list, name='task_list'),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('task/<int:pk>/', task_detail, name='task_detail'),
    path('task/new/', task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_delete, name='task_delete'),
]
