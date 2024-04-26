from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models  import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import Group


# Create your views here.
def index(request):
# Render the HTML template index.html with the data in the context variable.
   return render( request, 'sportsShare/index.html')

def myStatsheets(request):
   listSheets = Statsheet.objects.all()
   print("active Stats. query set", listSheets)
   return render( request, 'sportsShare/myStatsheets.html')

def statsheetDetail(request):
   return render( request, 'sportsShare/statsheetDetail.html')

def loginPage(request):
   return render( request, 'accounts/login.html')

def registerPage(request):

   form = CreateUserForm()

   if request.method == 'POST':
      form = CreateUserForm(request.POST)
      if form.is_valid():
         user = form.save()
         username = form.cleaned_data.get('username')
         group = Group.objects.get(name='guru')
         user.group.add(group)
         guru = Guru.objects.create(user=user,)
         binder = Binder.objects.create()
         guru.binder = binder
         guru.save()

         messages.success(request, 'Account was created for ' + username)
         return redirect('login')
      
   context ={'form':form}
   return render(request, 'accounts/register.html', context)
