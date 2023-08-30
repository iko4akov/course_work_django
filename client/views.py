from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from client.forms import ClientForm
from client.models import Client


class ClientListView(ListView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('client:client_list')

    def post(self, request):
        context = {}
        form = self.form_class(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            client.save()
            context['form'] = form
            return render(request, template_name='client/client_list.html', context=context)
        return render(request, self.template_name, context)

class ClientDetailView(DetailView):
    model = Client


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'second_name', 'third_name', 'email', 'comment')

    success_url = reverse_lazy('client:client_list')


class ClientDeleteView(DeleteView):
    model = Client

    success_url = reverse_lazy('client:client_list')
