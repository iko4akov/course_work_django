from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from distribution.models import Client, Distribution

class DistributionListView(ListView):
    model = Distribution

class DistributionDetailView(DetailView):
    model = Distribution

class DistributionCreateView(CreateView):
    model = CreateView

class DistributionUpdateView(UpdateView):
    model = CreateView

class DistributionDeleteView(DetailView):
    model = CreateView
