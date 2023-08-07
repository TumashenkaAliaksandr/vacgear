from django.conf.urls.static import static
from django.urls import path

from vacgear import settings
from webapp.views import *


app_name = 'webapp'

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('knowledge/', kowledgen, name='knowledge'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)