from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from message.models import Message


class MessageListView(ListView):
    model = Message

    def get_queryset(self):
        pk = self.request.user.pk
        queryset = super().get_queryset().filter(user=pk)
        return queryset


class MessageDetailView(DetailView):
    model = Message


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['theme', 'message']
    success_url = reverse_lazy('message:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ['theme', 'message']

    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        self.success_url = reverse_lazy('message:detail', kwargs={'pk': pk})
        return super().form_valid(form)


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message

    success_url = reverse_lazy('message:list')
