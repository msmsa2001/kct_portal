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
    path('payment_success/', payment_success, name='payment_success'),
    path('dialysis', dialysis, name='dialysis'),
    path('ramzan', ramzan, name='ramzan'),
    path('help', help, name='help'),
    path('display_particular_event/<int:eventId>/', displayParticularEvent, name='displayParticularEvent')
    # path('event/<slug:slug>/', views.event_detail, name='event_detail'),
]