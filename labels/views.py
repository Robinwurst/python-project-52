from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Label
from .forms import LabelForm

class LabelListView(ListView):
    model = Label
    template_name = 'labels/index.html'

class LabelCreateView(CreateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    template_name = 'labels/create.html'

class LabelUpdateView(UpdateView):
    model = Label
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    template_name = 'labels/update.html'

class LabelDeleteView(DeleteView):
    model = Label
    success_url = reverse_lazy('labels')
    template_name = 'labels/delete.html'