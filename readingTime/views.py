from django.shortcuts import render
from django.http import HttpResponse
from readingTime.models import Category, Book

def home(request):
    category_list = Category.objects.all()
    context_dict = {}
    context_dict['categories'] = category_list

    
    return render(request, 'readingTime/home.html', context=context_dict)

def signIn(request):
    # return HttpResponse("SignIn PAGE <a href='/readingTime/'>Home</a>")
    return render(request, 'readingTime/signIn.html')

def register(request):
    return render(request,'readingTime/register.html')
                  
def category(request):
    return render(request,'readingTime/category.html')

def book(request):
    return render(request,'readingTime/book.html')
