from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # return HttpResponse("HOME PAGE <a href='/readingTime/signIn/'>SignIn</a>")
    context_dict = {'message': 'ass, assa'}
    # We look inside templates/readingTime/<view.html>
    return render(request, 'readingTime/home.html')

def signIn(request):
    # return HttpResponse("SignIn PAGE <a href='/readingTime/'>Home</a>")
    return render(request, 'readingTime/signIn.html')

def register(request):
    return render(request,'readingTime/register.html')
                  


