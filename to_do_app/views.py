from django.shortcuts import redirect, render
from . models import AddTask
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class LoginView(LoginView):
    template_name = 'to_do_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks_list')
    
class Register(FormView):
    template_name = 'to_do_app/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks_list')
        return super(Register, self).get(*args, **kwargs)

class ListView(LoginRequiredMixin, ListView):
    model = AddTask
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        return context

class DetailView(LoginRequiredMixin, DetailView):
    model = AddTask
    context_object_name = 'task'

class CreateView(LoginRequiredMixin, CreateView):
    model = AddTask
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateView, self).form_valid(form)

class UpdateView(LoginRequiredMixin, UpdateView):
    model = AddTask
    fields = ['title','description','completed']
    success_url = reverse_lazy('tasks_list')

class DeleteView(LoginRequiredMixin, DeleteView):
    model = AddTask
    context_object_name = 'task'
    success_url = reverse_lazy('tasks_list')
