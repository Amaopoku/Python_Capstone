# tickets/views.py

from django.shortcuts import render
from .utils import generate_reservation_ticket  # Import your ticket generator function

def generate_ticket_view(request):
    ticket = generate_reservation_ticket()
    return render(request, 'tickets/ticket.html', {'ticket': ticket})
