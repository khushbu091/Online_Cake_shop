from django.contrib import admin
from django.urls import *
from  .views import *


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('product/', product, name='product'),
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),

]
