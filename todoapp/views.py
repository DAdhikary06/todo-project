
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from todoapp.forms import TODOForm
from todoapp.models import TODO
from django.contrib.auth.decorators import login_required
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
    return render(request, 'signUp.html', {'form': form, 'title':'SignUp | Page'})

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
    return render(request, 'login.html', {'form': form,'title':'ToDo | LoginPage'})

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


