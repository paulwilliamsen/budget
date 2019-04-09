from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    context = {
        'message': 'Hello world.'
    }
    return render(request, 'generic/base.html', context)