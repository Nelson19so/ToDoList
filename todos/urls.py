from django.urls import path
from . import views

urlpatterns = [
  path('todos/', views.todos, name='todos'),
  path('', views.blog, name='blog'),
  path('todositem/<int:pk>/', views.todo_items, name='todositem'),
  path('form/', views.todos_list_form, name="form"),
  path('signup/', views.signup, name="signup"),
  path('login/', views.login, name="login"),
  path('logout/', views.logout, name='logout'),
  path('logedout/', views.loged_out, name='logedout')
]