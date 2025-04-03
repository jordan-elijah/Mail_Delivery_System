# Parcel Class Generation
import datetime
class Parcel:
    def __init__(self, ID, destination, city, state, postalcode, cutoff_time, weight, status):
        self.ID = ID
        self.destination = destination
        self.city = city
        self.state = state
        self.postalcode = postalcode
        self.cutoff_time = cutoff_time
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.truck_ID = None
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, Truck: %s" % (self.ID, self.destination, self.city, self.state, self.postalcode,
                                                       self.cutoff_time, self.weight, self.delivery_time,
                                                       self.status, self.truck_ID)



    def print_status(self, convert_timedelta):
        temp_status = self.status
        temp_destination = self.destination
        temp_postalcode = self.postalcode

        if convert_timedelta > self.delivery_time:
            temp_status = "Delivered"
        elif convert_timedelta < self.departure_time:
            temp_status = "At Hub"
        else:
            temp_status = "En Route"



        if self.ID == 9:
            if convert_timedelta < datetime.timedelta(hours=10, minutes=20):
                temp_destination = "300 State St."
                temp_postalcode = "84103"
        if self.ID == 6 or 25 or 28 or 32:
            if convert_timedelta < datetime.timedelta(hours=9, minutes=5):
               temp_status = "Delayed on Flight"


        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, Truck: %s" % (
        self.ID, temp_destination, self.city, self.state, temp_postalcode,
        self.cutoff_time, self.weight, self.delivery_time,
        temp_status, self.truck_ID)

    def update_status(self, convert_timedelta):
        if self.departure_time > convert_timedelta and self.delivery_time > convert_timedelta:
            self.status = "En route"
        elif self.delivery_time < convert_timedelta:
            self.status = "Delivered"
        else:
            self.status = "At Hub"

