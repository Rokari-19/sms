from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import *
from projects.models import *
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/login/')
def index(request):
    work = Workname.objects.filter(mark_done = False)[0:6]
    category = Category.objects.all()
    return render(request, 'main_app/index.html',{
        'work':work,
        'project':category
    } )


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request, 'main_app/signup.html', {
        'form':form
    })


def logOut(request):
    logout(request)
    return redirect('/login/')
    