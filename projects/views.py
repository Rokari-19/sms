from django.shortcuts import render, get_object_or_404, redirect
from .models import Workname

# Create your views here.

def detali(request, pk):
    work = get_object_or_404(Workname, pk=pk)

    return render(request, 'projects/detail.html', {
        'work':work
    })