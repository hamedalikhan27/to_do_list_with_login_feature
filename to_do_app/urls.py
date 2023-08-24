from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView, LoginView, Register
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('register/',Register.as_view(),name='register'),

    path('',ListView.as_view(),name='tasks_list'),
    path('create/',CreateView.as_view(),name= 'create'),
    path('update/<int:pk>/',UpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',DeleteView.as_view(),name='delete'),
]