from django.shortcuts import render

from send.models import Send


def index_view(request):
    context = {}
    context['object_list'] = Send.objects.all()
    return render(request, 'frontend/list.html', context)
