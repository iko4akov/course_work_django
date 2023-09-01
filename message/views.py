from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from message.models import Message


class MessageListView(ListView):
    model = Message


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(CreateView):
    model = Message
    fields = ['theme', 'message']

    success_url = reverse_lazy('message:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MessageUpdateView(UpdateView):
    model = Message
    fields = ['theme', 'message']

    def form_valid(self, form):
        pk = self.request.user.pk
        self.success_url = reverse_lazy('message:detail', kwargs={'pk': pk})
        return super().form_valid(form)


class MessageDeleteView(DeleteView):
    model = Message

    success_url = reverse_lazy('message:list')
