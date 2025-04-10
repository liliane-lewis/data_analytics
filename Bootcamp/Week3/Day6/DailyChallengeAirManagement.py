#Instructions : Air management system
#
#Your goal is to build an airplanes traffic management system.
#
#
#Details
#
#Your program should rely on four classes: Airline, Airplane, Flight and Airport.
#
#Consider every plane can fly only once per day.
#
#
#The Airline class
#
#Attributes:
#
#    id (str) A two letters code
#    name (str)
#    planes : A list of Airplanes belonging to this airline (see below the Airplane class)
3
#This class has no methods
#
#
#The Airplane class
#
#Attributes:
#
#    id (int)
#    current_location : The Airport where the airplane is currently located (see below the Airport class)
#    company : The airline this airplane belongs to (see above the Airline class)
#    next_flights : The list of Flights. Every future flights of the airplane, this list should always be sorted by datetime. (see below the Flight class)
#
#
#Methods:
#
#    fly(self, destination): Make the airplane take off and land if a flight is scheduled for this destination (see below the Flight class)
#    location_on_date(self, date): Returns where the plane will be on this date
#    available_on_date(self, date, location) : Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).
#
#
#The Flight class
#
#Attributes:
#
#    date : datetime.Date
#    destination : The destination airport. (see below the Airport class)
#    origin : The departure airport. (see below the Airport class)
#    plane : The plane used during this flight. (see above the Airplane class)
#    id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.
#
#Methods:
#
#Those methods are here only to update the rest of the system:
#
#    take_off(self)
#    land(self) : change the location of the plane when it reaches its destination
#
#
#The Airport class
#
#Attributes:
#
#    city : (str) The code of the city where the airport is located
#    planes : The list of every plane that is currently in this airport. (see above the Airplane class)
#    scheduled_departures : The list of flight - Every future flight from this airport, sorted by date. (see above the Flight class)
#    scheduled_arrivals : The list of flight - Every future flight that will arrive to this airport, sorted by date. (see above the Flight class)
#
#
#Methods:
#
#    schedule_flight(self, destination, datetime) :
#        finds an available airplane from an airline, that serves the departure and the destination
#        schedule the airplane for the flight
#    info(self, start_date, end_date) : Displays every scheduled flight from start_date to end_date.
#
#
#You are free to add any class/method/attribute to your code, be sure to document everything you write.
#
#Write a small code to test your program. 

import datetime


class Airline:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.planes = []

class Airplane:
    def __init__(self, id, current_location, company):
        self.id = id
        self.current_location = current_location
        self.company = company
        self.next_flights = [] #The list of Flights. Every future flights of the airplane, this list should always be sorted by datetime. 


    def fly(self, destination): 
        for flight in self.next_flights:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                print(f"Plane {self.id} flew from {flight.origin.city} to {destination.city} on {flight.date}")
                break



    def location_on_date(self, date): 
        '''Returns where the plane will be on this date'''
        
        location = self.current_location

        for flight in self.next_flights:
            if flight.date > date:
                break
            location = flight.destination

        return location

    
    def available_on_date(self, date, location): 
        '''Returns True if the plane can fly from this location on this date (it can fly if it is in this location on this date and if it
          doesn't already have a flight planned).'''
        if self.location_on_date(date) != location:
            return False

        for flight in self.next_flights:
            if flight.date == date:
                return False
        return True 


class Flight:
    def __init__(self, date, destination, origin, plane):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{destination.city}-{plane.company.id}-{date}"

    def take_off(self):
        '''Removes the plane from the origin airport's planes list when it takes off'''
        '''self.origin is the Airport object'''
        '''self.plane is the Airplane object'''
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)
        print(f"Plane {self.plane.id} took off from {self.origin.city} on {self.date}")

    def land(self): 
        '''change the location of the plane when it reaches its destination'''
        if self.plane not in self.destination.planes:
            self.destination.planes.append(self.plane)
        
        self.plane.current_location = self.destination
        print(f"Plane {self.plane.id} landed at {self.destination.city} on {self.date}")

class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []


    def schedule_flight(self, destination, date):
        '''finds an available airplane from an airline, that serves the departure and the destination
        schedule the airplane for the flight'''
        for plane in self.planes:
            if plane.available_on_date(date, self):  # Check availability at THIS airport
                # Create a flight
                flight = Flight(date, destination, self, plane)

                # Add to plane's future flights (and keep it sorted)
                plane.next_flights.append(flight)
                plane.next_flights.sort(key=lambda f: f.date)

                # Add to airport's departures and destination's arrivals
                self.scheduled_departures.append(flight)
                self.scheduled_departures.sort(key=lambda f: f.date)

                destination.scheduled_arrivals.append(flight)
                destination.scheduled_arrivals.sort(key=lambda f: f.date)

                return flight  # Return the scheduled flight
        
        return None  # No available airplane

    def info(self, start_date, end_date):
        '''Displays every scheduled departure flight from start_date to end_date.'''
        print(f"Scheduled flights from {self.city} between {start_date} and {end_date}:")
    
        for flight in self.scheduled_departures:
            if start_date <= flight.date <= end_date:
                print(f" - {flight.date}: Flight {flight.id} to {flight.destination.city} using Plane {flight.plane.id}")
        




# === TEST SCENARIO: Brazil ===

# Airports
gru = Airport("GRU")  # São Paulo
gig = Airport("GIG")  # Rio de Janeiro
poa = Airport("POA")  # Porto Alegre

# Airlines
gol = Airline("G3", "GOL Linhas Aéreas")
azul = Airline("AD", "Azul Linhas Aéreas")
latam = Airline("LA", "LATAM Airlines Brasil")

# Airplanes
plane1 = Airplane(1001, gru, gol)
plane2 = Airplane(1002, gig, azul)
plane3 = Airplane(1003, poa, latam)

# Register airplanes in their airlines
gol.planes.append(plane1)
azul.planes.append(plane2)
latam.planes.append(plane3)

# Place airplanes at their respective airports
gru.planes.append(plane1)
gig.planes.append(plane2)
poa.planes.append(plane3)

# Dates
today = datetime.date(2025, 4, 10)
tomorrow = datetime.date(2025, 4, 11)

# ✈️ GOL: GRU → GIG
flight1 = gru.schedule_flight(gig, today)

# ✈️ AZUL: GIG → POA
flight2 = gig.schedule_flight(poa, tomorrow)

# ✈️ LATAM: POA → GRU
flight3 = poa.schedule_flight(gru, tomorrow)

# Scheduled flights
print("\nScheduled Flights:")
gru.info(today, tomorrow)
gig.info(today, tomorrow)
poa.info(today, tomorrow)

# Today
print("\nFlights happening today:")
if flight1: plane1.fly(gig)

# Tomorrow
print("\nFlights happening tomorrow:")
if flight2: plane2.fly(poa)
if flight3: plane3.fly(gru)
