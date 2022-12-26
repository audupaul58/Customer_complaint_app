from django.shortcuts import render
from .models import Agricom
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django. contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import AgriComForm

# Create your views here.

class AllNumbers(ListView):
    model = Agricom
    template_name = 'agricom/index.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        user = self.request.user
        return  Agricom.objects.filter(user=user)

class DeleteNumber(DeleteView):
    model = Agricom
    template_name = 'agricom/delete.html'
    success_url = reverse_lazy('agricom')
    
class AddNumber(LoginRequiredMixin, CreateView):
    form_class = AgriComForm
    template_name = 'agricom/create.html'
    success_url = reverse_lazy('agricom')
    
    def form_valid(self, form):
        #  This allow user save to it own page alone
        form.instance.user = self.request.user
        content = super().form_valid(form)
        return content
    
class UpdateNumber(LoginRequiredMixin, UpdateView):
    model = Agricom
    fields = ['phone_number', 'names', 'address', 'alternate_num', 'status', ]
    template_name = 'agricom/create.html'
    success_url = reverse_lazy('agricom')
    
    
class Search_Page(ListView):
    template_name = 'agricom/search.html'
    model = Agricom
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        object_list = Agricom.objects.filter(Q(phone_number__icontains=query)| Q(names__icontains=query)) 
        return object_list

