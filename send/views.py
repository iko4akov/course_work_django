from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from send.models import Send


class SendCreateView(CreateView):
    model = Send
    fields = ['period', 'message', 'time']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('send:detail', kwargs={'pk': pk})
        return super().form_valid(form)


class SendListView(ListView):
    model = Send


class SendDetailView(DetailView):
    model = Send


class SendUpdateView(UpdateView):
    model = Send
    fields = ['status', 'period', 'message', 'time']
    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('send:detail', kwargs={'pk': pk})
        return super().form_valid(form)

class SendDeleteView(DeleteView):
    model = Send
    success_url = reverse_lazy('send:list')


