from django.contrib import admin
from django.urls import *
from  .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('registerdata/', registerdata, name='registerdata'),
    path('login/', login, name='login'),
    path('logindata/', logindata, name='logindata'),
    path('dashbord/', dashbord, name='dashbord'),

]
