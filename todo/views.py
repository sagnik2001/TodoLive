from django.db import models
from django.db.models import fields
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin # for restricting the user to not allow to move to other pages if not login
from django.contrib.auth.forms import UserCreationForm # for creating a manuel form for registering an user
from django.contrib.auth import login
from .models import Task
# Create your views here.

class CustomLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo')
        
class RegisterPage(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo')
     # to add functionality to register the user after form is submitted
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)# user is valid
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs): # restrict the user to move around login and register and home page 
        if self.request.user.is_authenticated:
            return redirect('todo')
        return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin,ListView):
    model= Task
    context_object_name= 'tasks'
    def get_context_data(self, **kwargs):      # restrict the user to check other users todos
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__startswith=search_input)

        context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name="task" 
       

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title', 'description', 'complete']
    success_url= reverse_lazy('todo')

    def form_valid(self, form): 
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title', 'description', 'complete']
    success_url= reverse_lazy('todo')    

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name="task"   
    success_url= reverse_lazy('todo')  