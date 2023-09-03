from django.shortcuts import render

from mailing.models import Mailing

def index_view(request):
    context = {}
    pk = request.user.pk
    context['object_list'] = Mailing.objects.filter(user=pk).all()
    return render(request, 'frontend/list.html', context)
