
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from todoapp.forms import TODOForm
from todoapp.models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.
# Home page
@login_required(login_url='login')
def index(request):
    if request.user.is_authenticated:
        user=request.user
        form=TODOForm()
        todos = TODO.objects.filter(user=user).order_by('priority')
        return render(request, 'todo.html',context={'form':form, 'todos': todos, 'title':'TODO'})

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signUp.html', {'form': form, 'title':'SignUp-Page'})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,'title':'ToDo-Login-Page'})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')

# Add Todo page
def add_todo(request):
    if request.user.is_authenticated:
        user=request.user
        # print(user)
        form=TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            todo=form.save(commit=False) #is user somehows takes null then in this way we are trying to save user 
            todo.user=user
            todo.save()
            # print(todo)
            return redirect('home')
        return render(request, 'todo.html', context={'form':form})
    
# delete todo
def delete_todo(request, id):
    TODO.objects.get(pk=id).delete()
    return redirect('home')

# change status todos
def change_todo(request,id,status):
    todos=TODO.objects.get(pk=id)
    todos.status=status
    todos.save()
    return redirect('home')

# Create your views here.
# todo_list_app/views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.http import HttpResponse
# from django.contrib import messages
# from django.contrib.auth import authenticate,login,logout
# from.models import TodoItem
# from.forms import TodoItemForm

# def index(request):
#     return render(request, 'base.html',{'title':'Home'})

# def login(request):
#     if request.method=='GET':
#         form=AuthenticationForm() #create object
#         context={
#             "form":form
#         }
#         return render(request, 'login.html', context=context)
#     else:
#         form=AuthenticationForm()
#         if form.is_valid():
#             username=form.cleaned_data['username']
#             password=form.cleaned_data['password']
#             user=authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('create_todo_item')

# def signUp(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # username=form.cleaned_data.get('username')
#             # password=form.cleaned_data.get('password')
#             return redirect('login')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signUp.html', {'form': form ,'title':'SignUp'})

# login page
# def login(request):
#     if request.method == 'POST': 
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             form=login(request, user)
#             # messages.success(request,f'Welcome, {username}')    
#             return redirect('home')
#         # else:
#             # messages.info(request, f'account done not exit plz sign in')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form,'title':'Log in'})


                  
# # logout page
        
# def signUp(request):
#     if request.method == 'GET':
#         form = UserCreationForm()
#         context={
#             "form" : form
#         }
#         return render(request, 'signUp.html',context=context)
#     else:
#         print(request.POST)
#         form = UserCreationForm(request.POST)
#         context={
#             "form" : form
#         }
#         if form.is_valid():
#             user=form.save()
#             print(user)
#             if user is not None:
#                 return redirect('login')
#             return HttpResponse("Form is Valid")
#         else:
#             return render(request,'signUp.html',context=context)


# def todo_list(request):
#     todo_items = TodoItem.objects.all()
#     return render(request, 'todo_list.html', {'todo_items': todo_items})

# def create_todo_item(request):
#     if request.method == 'POST':
#         form = TodoItemForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoItemForm()
#     return render(request, 'create_todo_item.html', {'form': form})

# def update_todo_item(request, pk):
#     todo_item = TodoItem.objects.get(pk=pk)
#     if request.method == 'POST':
#         form = TodoItemForm(request.POST, instance=todo_item)
#         if form.is_valid():
#             form.save()
#             return redirect('todo_list')
#     else:
#         form = TodoItemForm(instance=todo_item)
#     return render(request, 'update_todo_item.html', {'form': form})

# def delete_todo_item(request, pk):
#     TodoItem.objects.get(pk=pk).delete()
#     return redirect('todo_list')
