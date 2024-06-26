from django.shortcuts import render
import random
import string

def generate_reservation_ticket():
    # Generate passenger name
    names = [
        "Ahmed Owusu", "Ama Agyemang", "Autumn Velez", "Brauleo Lizardo", "Celia Cen",
        "Clara Edward", "Dmari Smith", "Dumebi Chukwuma", "Hisham Hossain", "Jael Bonilla",
        "Jahaziel Ramos", "Jamal Dolah", "Jeffrey Hu", "Jonathan Luz", "Jovens Sagesse",
        "Kobe Lee-Whitfield", "Mamoudou Bah", "Mohammad Rahman", "Nia Davis", "Nurbek Jouraboev",
        "Pierre Boasiako", "Rohit Hoobraj", "Rosa Meneses", "Sean Randolph", "Soledad Vaquero",
        "Stephen Oke", "Tommy Wu", "Torell Butler", "Ty Reid", "Vincent Maitland", "Yanchen Lhamo"
    ]

    passenger_name = random.choice(names)

    # Generate flight details
    flight_number = "XY" + ''.join(random.choices(string.ascii_uppercase, k=3)) + str(random.randint(100, 999))
    departure_city = random.choice(["New York", "Los Angeles", "Chicago", "Miami", "San Francisco"])
    arrival_city = random.choice(["London", "Paris", "Tokyo", "Sydney", "Dubai"])
    departure_time = f"{random.randint(1, 12)}:{random.randint(0, 59)}{'AM' if random.random() < 0.5 else 'PM'}"
    arrival_time = f"{random.randint(1, 12)}:{random.randint(0, 59)}{'AM' if random.random() < 0.5 else 'PM'}"
    seat_assignment = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))

    # Create dictionary object for ticket details
    ticket = {
        'passenger_name': passenger_name,
        'flight_number': flight_number,
        'departure_city': departure_city,
        'arrival_city': arrival_city,
        'departure_time': departure_time,
        'arrival_time': arrival_time,
        'seat_assignment': seat_assignment,
    }

    return ticket

def generate_ticket_view(request):
    # Generate a new reservation ticket
    ticket = generate_reservation_ticket()

    # Render the template with the ticket details
    return render(request, 'tickets/ticket.html', {'ticket': ticket})
