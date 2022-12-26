from django.shortcuts import render
from .models import Polcom
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import PolComForm
# Create your views here.

class AllNumbers(ListView):
    model = Polcom
    template_name = 'polcom/index.html'
    context_object_name = 'items'
    
    def get_queryset(self):
        user = self.request.user
        return  Polcom.objects.filter(user=user)

class DeleteNumber(DeleteView):
    model = Polcom
    template_name = 'polcom/delete.html'
    success_url = reverse_lazy('polcom')
    
class AddNumber(LoginRequiredMixin, CreateView):
    form_class = PolComForm
    template_name = 'polcom/create.html'
    success_url = reverse_lazy('polcom')
    
    def form_valid(self, form):
        #  This allow user save to it own page alone
        form.instance.user = self.request.user
        content = super().form_valid(form)
        return content
    
class UpdateNumber(LoginRequiredMixin, UpdateView):
    model = Polcom
    fields = ['phone_number', 'names', 'address', 'alternate_num', 'status', 'rank' ]
    template_name = 'polcom/update.html'
    success_url = reverse_lazy('polcom')
    
class Search_Page(ListView):
    template_name = 'polcom/search.html'
    model = Polcom
    context_object_name = 'items'

    def get_queryset(self):
        query = self.request.GET.get('q') 
        object_list = Polcom.objects.filter(Q(phone_number__icontains=query)| Q(names__icontains=query)) 
        return object_list
    
    

