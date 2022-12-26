from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, TemplateView,  DeleteView
from .models import BlogTask
from .forms import DataForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

# Create your views here.

class HomePage(TemplateView):
    template_name = 'todos/home.html'
    

class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'todos/tasklist.html'
    model = BlogTask
    context_object_name = 'items'
    
# restricting user to user specific pages
    def get_queryset(self):
        user = self.request.user
        return  BlogTask.objects.filter(user=user)

        # Add a search function to your listviews
       
    
        # search method for individual user iteme
        

class AdminView(ListView):
    template_name = 'todos/admin.html'
    model = BlogTask
    context_object_name = 'items'
    

class TaskCreateView(LoginRequiredMixin, CreateView):
    template_name = 'todos/create.html'
    form_class = DataForm
    success_url = reverse_lazy('tasklist')
    
    def form_valid(self, form):
        #  This allow user save to it own page alone
        form.instance.user = self.request.user
        content = super().form_valid(form)
        return content
    

class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = 'todos/update.html'
    model = BlogTask
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('admins')
    

class DeleteTask(LoginRequiredMixin, DeleteView):
    template_name = 'todos/delete.html'
    model = BlogTask
    success_url = reverse_lazy('admins')
    

class Search_Page(ListView):
    template_name = 'todos/search.html'
    model = BlogTask
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        object_list = BlogTask.objects.filter(Q(title__icontains=query)| Q(description__icontains=query)) 
        return object_list

    
    
