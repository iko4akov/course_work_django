import os

from django.core.mail import send_mail
from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


@method_decorator(never_cache, name='dispatch')
class BlogCreateView(CreateView):
    model = Blog
    fields = ['title', 'slug', 'content', 'preview', 'public', 'count_view']
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


@method_decorator(never_cache, name='dispatch')
class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['title', 'slug', 'content', 'preview', 'public', 'count_view']

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(public=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        if self.object.count_view == 100:
            send_mail(subject='yandex.ru', message='neujeli rabotaet', from_email='as1cs09@yandex.ru',
                      recipient_list=['iko4akov@gmail.com'], fail_silently=False)
            print('nice')
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')

    def get_object(self, queryset=None):
        object = super().get_object(queryset)
        if object.user != self.request.user:
            raise Http404

        return object
