

#Truck Object Generation
class Truck:
    def __init__(self,ID,  max_load, speed, current_load, parcels, distance, destination, leave_time):
        self.ID = ID
        self.max_load = max_load
        self.speed = speed
        self.current_load = current_load
        self.parcels = parcels
        self.distance = distance
        self.destination = destination
        self.leave_time = leave_time
        self.time = leave_time

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID,self.max_load, self.speed, self.current_load, self.parcels, self.distance,
                                               self.destination, self.leave_time)