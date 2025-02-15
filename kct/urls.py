from django.urls import path
from .views import *
 
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('activity/', activity, name='activity'),
    path('benefits/', benefits, name='benefits'),
    path('career/', career, name='career'),
    path('contacts/', contact, name='contact'),
    path('donate/', donate, name='donate'),
    path('dialysis', dialysis, name='dialysis'),
    path('ramzan', ramzan, name='ramzan'),
    path('help', help, name='help'),
]