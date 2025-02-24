from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import TodoItems
from .form import TodoItemsForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Create your views here.

def todos(request):

  user = request.user #request from accessing the user

  if request.method == "POST": #posting data
    if user.is_authenticated: #verify if the use is authenticated
      # handle todo post to the database
      if 'submit_todo' in request.POST: #button for submit todos
        form = TodoItemsForm(request.POST)

        data = request.POST.get('todo') #getting todo input to verify the length

        if len(data) > 3: #checking length
          # validating data to save it for the user
          if form.is_valid():
            print("adding new item")
            todo_item = form.save(commit=False)
            todo_item.user = request.user 
            # saves todo to te database
            todo_item.save()
            print("posted new todlist")
            return redirect('todolist')

          else:
            return #returns to us
          
        else:
          print("Item less ( < ) than 3")
          return HttpResponse("<h3>Item should be more than 3 characters in length</h3>")


      # update complete or false for todolist status
      elif 'update_todo' in request.POST:
        for items in TodoItems.objects.all():
          if request.POST.get("check-" + str(items.id)) == "clicked":
            items.completed = True
          else:
            items.completed = False

          items.save()
          print("item saved successfully")

    else:
      # redirect user if post and not authenticated
      return redirect('login')
  
  else:
    form = TodoItemsForm()

  if user.is_authenticated:
    todos = TodoItems.objects.filter(user=user)
    completed_todos = TodoItems.objects.filter(user=user, completed=True)
    active_todos = TodoItems.objects.filter(user=user, completed=False)
    no_todos = TodoItems.objects.filter(user=user, completed=False).count()

    context = {"todos": todos, "no_todos":no_todos, "active_todos":active_todos, 
              "completed_todos":completed_todos, "user":user}
    template_name = 'todos/index.html'
  
  else:
    context = {}
    template_name = 'todos/index.html'
    
  # renders html template
  return render(request, template_name, context)


# Delete todolist view
@login_required(login_url="login")
def delete_todo(request, pk):
  todo = TodoItems.objects.get(pk=pk)
  todo.delete()
  print("deleted todolist successfully")

  #redirecting the user to todolist page
  return redirect('todolist')


# Delete completed todolist view
@login_required(login_url='login')
def delete_completed_todos(request):  
  todos = TodoItems.objects.filter(completed=True)
  todos.delete()
  print('deleted all completed todolist')

  # redirecting the user to todolist page
  return redirect('todolist')


# Login form for todos
def login(request):
  page = 'login'

  if request.user.is_authenticated:
      return redirect('todolist')
  
  if request.method == 'POST':
    username = request.POST.get('username').lower()
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      auth_login(request, user)
      return redirect('todolist')

    messages.error(request, 'username or email not found')
      
  return render(request, 'todos/auth.html', {"page": page})


def signup(request):
  page = 'signup'

  if request.method == "POST":
    username = request.POST.get('username').lower()
    email = request.POST.get('email')
    password = request.POST.get('password')
    comfirm_password = request.POST.get("comfirm_password")

    not_recommended_lenght = 2

    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
      messages.error(request, 'username or email already exist')

    elif len(username) <= not_recommended_lenght:
      messages.error(request, 'username is too short')

    elif len(email) <= not_recommended_lenght:
      messages.error(request, 'email address is too short')

    elif password != comfirm_password:
      messages.error(request, 'password do no match')
      
    elif len(password) <= not_recommended_lenght:
      messages.error(request, 'password is too short')

    else:
      user = User.objects.create_user(username=username, email=email, password=password)   
      user.save()

      return redirect('login')
    
  return render(request, 'todos/auth.html', {'page': page})


# Log out view
def logout_view(request):
  logout(request)
  return redirect('login')