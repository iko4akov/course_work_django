from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from params.models import Params


class ParamsListView(ListView):
    model = Params


class ParamsDetailView(DetailView):
    model = Params


class ParamsCreateView(CreateView):
    model = Params


class ParamsUpdateView(UpdateView):
    model = Params


class ParamsDeleteView(DeleteView):
    model = Params
