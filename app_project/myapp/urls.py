from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),  # Changed to a different path for about
    path('contact/', views.contact, name='contact'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
]