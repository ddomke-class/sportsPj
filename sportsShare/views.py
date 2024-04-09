from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'sportsShare/index.html')

def myStatsheets(request):

# Render the HTML template index.html with the data in the context variable.
   return render( request, 'sportsShare/myStatsheets.html')
