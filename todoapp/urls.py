# todo_list_app/urls.py
from django.urls import path
# from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.user_login, name='login'),
    path('signUp/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('add-todo/', views.add_todo, name='add-todo'),
    path('delete-todo/<int:id>', views.delete_todo, name='delete-todo'),
    path('change-status/<int:id>/<str:status>', views.change_todo, name='change-todo'),
    path('delete-todo/<int:id>', views.delete_todo, name='delete-todo'),
    
]