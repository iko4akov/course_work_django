from django.shortcuts import render

from mailing.models import Mailing

def index_view(request):
    context = {}
    context['object_list'] = Mailing.objects.all()
    return render(request, 'frontend/list.html', context)
