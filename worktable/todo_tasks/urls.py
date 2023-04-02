from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth import views as auth_view
from . forms import LoginForm

urlpatterns = [
    path('login/', auth_view.LoginView.as_view(template_name='connexion.html', authentication_form=LoginForm, success_url=reverse_lazy('tasks')), name='login'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('create/', views.CreateTask.as_view(), name='create'),
    path('update/<pk>/', views.UpdateTask.as_view(), name='update'),
    path('delete/<pk>', views.DelteteTask, name='delete'),
    path('', views.TaskView, name='tasks'),
]