from django.urls import path
from webapp.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
]
