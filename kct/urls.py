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
    # path('payment_success/', payment_success, name='payment_success'),
    path('dialysis', dialysis, name='dialysis'),
    path('ramzan', ramzan, name='ramzan'),
    path('help', help, name='help'),
    path('display_particular_event/<int:eventId>/', displayParticularEvent, name='displayParticularEvent'),
    path('government-scheme/<int:schemeId>/', govtScheme, name='govtScheme'),
    path('project-detail/<int:projectId>/', projectDetail, name='projectDetail'),
    # path('event/<slug:slug>/', views.event_detail, name='event_detail'),
    path('news', news, name='news'),
    path('anual_report', anual_report, name='anual_report'),
    path('gallery', gallery, name='gallery'),
    path('sucess_story', success_story, name='success_story'),
    path('donation-terms/', donation_terms, name='donation_terms'),
    path("create-order/", create_cashfree_order, name="create_cashfree_order"),
    path("cashfree/webhook/", cashfree_webhook, name="cashfree_webhook"),
    path("payment-success/", payment_success, name="payment_success"),

]