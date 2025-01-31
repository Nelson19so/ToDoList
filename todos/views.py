from django.shortcuts import render, redirect
from .models import TodoItems
from .form import TodoItemsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.

@login_required(login_url='login')
def todos(request):
  todos = TodoItems.objects.all()
    
  # renders html template
  return render(request, 'todos/todo.html', {"todos": todos})


def todo_items(request, pk):
  todoitems = TodoItems.objects.get(pk=pk)

  # renders html template
  return render(request, 'todos/todositems.html', {"todoitems":todoitems})


def login(request):
  page = 'login'

  if request.user.is_authenticated:
      return redirect('todos')
  
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      auth_login(request, user)
      return redirect('todos')

    messages.error(request, 'username or email not found')

      
  return render(request, 'todos/login_signup.html', {"page": page})


def signup(request):
  page = 'signup'
  
  if request.method == "POST":
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    comfirm_password = request.POST.get("comfirm_password")

    not_recommended_lenght = 5

    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
      messages.error(request, 'username or email already exist')

    elif password != comfirm_password:
      messages.error(request, 'password do no match')
      
    elif len(password) <= not_recommended_lenght:
      messages.error(request, 'password is too short')
      
    elif len(username) <= not_recommended_lenght:
      messages.error(request, 'username is too short')

    else:
      user = User.objects.create_user(username=username, email=email, password=password)   
      user.save()

      return redirect('login')
    
  return render(request, 'todos/login_signup.html', {'page': page})


def blog(request):
  return render(request, 'base.html')


def logout(request):
  logout(request)
  return redirect('logedout')


def loged_out(request):
  return render(request, 'logedout.html')


def todos_list_form(request):
  form = TodoItemsForm

  if request.method == "POST":
    print(request.POST)
    form = TodoItemsForm(request.POST)

    if form.is_valid():
      form.save()
  else:
    form = TodoItemsForm()
  return render(request, 'todos/form.html', {"form":form})