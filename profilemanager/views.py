from django.shortcuts import render
from .models import profile
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import profileForm

def index(request):
    return render(request, 'index.html')

def listing(request):
    Profile=profile.objects.all()
    return render(request, 'list.html',{'profile':Profile})

def add(request):
    form = profileForm()
    return render(request, 'add.html',{'form':form})

def myprofile(request):
    form=profileForm(request.POST)
    if form.is_valid():
        data=profile(name = form.cleaned_data['name'],email = form.cleaned_data['email'])
        data.save()
    return HttpResponseRedirect('list')