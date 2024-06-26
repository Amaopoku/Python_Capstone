# tickets/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate-ticket/', views.generate_ticket_view, name='generate_ticket'),
    # Additional paths if needed
    path('http://127.0.0.1:8000/generate-ticket/', views.generate_ticket_view, name='generate_ticket')
]
