from django.urls import path
from . import views

urlpatterns = [
  path('', views.todos, name="todolist"),
  path('register/', views.signup, name="register"),
  path('login/', views.login, name="login"),
  path('logout/', views.logout_view, name="logout"),
  path('delete/<int:pk>', views.delete_todo, name="delete"),
  path('deletecompletedtodos/', views.delete_completed_todos, name='deletecompletedtodos'),
]