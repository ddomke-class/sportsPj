from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models  import *
# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'sportsShare/index.html')

def myStatsheets(request):
   listSheets = Statsheet.objects.all()
   print("active Stats. query set", listSheets)
   return render( request, 'sportsShare/myStatsheets.html')


