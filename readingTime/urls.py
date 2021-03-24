from django.urls import path
from readingTime import views

app_name = 'readingTime'

urlpatterns = [
    # TODO handle the URL mapping by name rather than by the URL
    # See Section 8.1
    path('', views.home, name='home'),
    path('signIn/', views.signIn, name='signIn'),
    path('logOut/', views.logOut, name='logOut'),
    path('register/', views.register, name='register'),
    path('category/', views.category, name='category'),
    path('book/', views.book, name='book'),
]
