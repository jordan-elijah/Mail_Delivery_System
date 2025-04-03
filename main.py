# Student Name: Jordan-Elijah Baez
# Student ID: 011163565
# Class: C950 Data Structures and Algorithms II


from builtins import ValueError
import csv
import Truck
import datetime


from HashTable import Hashtable
from Parcel import Parcel

# Find Distance Information from CSV File
with open("CSVFiles/WGUPS_Distance_Table.csv") as csvfile:
    CSV_Mileage = csv.reader(csvfile)
    CSV_Mileage = list(CSV_Mileage)

# Find Destination Information from CSV File
with open("CSVFiles/WGUPS_Destination_List.csv") as csvfile1:
    CSV_Destination = csv.reader(csvfile1)
    CSV_Destination = list(CSV_Destination)

# Find Parcel Information from CSV File
with open("CSVFiles/WGUPS_Parcel_File.csv") as csvfile2:
    CSV_Parcel = csv.reader(csvfile2)
    CSV_Parcel = list(CSV_Parcel)



# Generation of Parcel Objects from CSV File/ Send Parcel Objects to HashTable
def get_parcel_info(filename, parcel_hash):
    with open(filename) as parcel_info:
        parcel_data = csv.reader(parcel_info)
        for parcel in parcel_data:
            pID = int(parcel[0])
            pdestination = parcel[1]
            pcity = parcel[2]
            pstate = parcel[3]
            ppostalcode = parcel[4]
            pcutoff_time = parcel[5]
            pweight = parcel[6]
            pstatus = "At Hub"




            p = Parcel(pID, pdestination, pcity, pstate, ppostalcode, pcutoff_time, pweight, pstatus)
            # Parcel Object Generation


            parcel_hash.insert(pID, p)
            # Send information to HashTable


# Finds difference between to destinations for parcels
def truck_distance(x_val, y_val):
    distance = CSV_Mileage[x_val][y_val]
    if distance == '':
        distance = CSV_Mileage[y_val][x_val]

    return float(distance)


# Gets all Parcel Destinations from CSV_Files
def pull_destination(destination):
    for row in CSV_Destination:
        if destination in row[2]:
            return int(row[0])


# Truck 1 Object generation
Truck_1 = Truck.Truck(1,16, 18, None, [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=8))

# Truck 2 Object generation
Truck_2 = Truck.Truck(2,16, 18, None, [3, 12, 17, 18, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39], 0.0,
                     "4001 South 700 East", datetime.timedelta(hours=10, minutes=20))

# Truck 3 Object generation
Truck_3 = Truck.Truck(3,16, 18, None, [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 0.0, "4001 South 700 East",
                     datetime.timedelta(hours=9, minutes=27))

#Hashtable Generation
parcel_hash = Hashtable()

# Place parcels into hashtable
get_parcel_info("CSVFiles/WGUPS_Parcel_File.csv", parcel_hash)


# Dropping of Parcels are done here, using the "nearest neighbor" Algorithm
# Final Route Distances are also calculated in Addition to the route ordering
def drop_off_parcels(truck):
    #


    not_dropped_off = []
    for parcelID in truck.parcels:
        parcel = parcel_hash.lookup(parcelID)
        not_dropped_off.append(parcel)

    # Below will ensure the parcel list of trucks will be cleared,
    # ensuring our nearest neighbor algo order is in place

    truck.parcels.clear()


    # creates the procedure to add parcels into the trucks
    # will iterate through the list until empty

    while len(not_dropped_off) > 0:
        next_destination = 2000
        next_parcel = None
        for parcel in not_dropped_off:
            if truck_distance(pull_destination(truck.destination), pull_destination(parcel.destination)) <= next_destination:
                next_destination = truck_distance(pull_destination(truck.destination), pull_destination(parcel.destination))
                next_parcel = parcel

        # Adds the next parcel due for the truckload
        truck.parcels.append(next_parcel.ID)
        # Same Parcel is removed from the list of parcels not dropped off
        not_dropped_off.remove(next_parcel)
        # Retrieves route distance to drop off current parcel
        truck.distance += next_destination
        # Uses retrieved distance and adds it to total route distance
        truck.destination = next_parcel.destination
        # Sets time taken for parcel delivery for current truck delivery
        truck.time += datetime.timedelta(hours=next_destination / 18)
        next_parcel.delivery_time = truck.time
        next_parcel.departure_time = truck.leave_time
        next_parcel.truck_ID = truck.ID




# Delivery Trucks will now be filled with appropriate parcels
drop_off_parcels(Truck_1)
drop_off_parcels(Truck_2)
# This makes sure the last delivery truck leaves last
#change address for parcel 9 here
parcel_hash.lookup(9).destination = "410 S State St"
parcel_hash.lookup(9).postalcode = "84111"
Truck_3.leave_time = min(Truck_1.time, Truck_2.time)
drop_off_parcels(Truck_3)


class Main:
    # Here Starts the beginning of the UI for our Program
    print("Welcome To The Western Governors University Parcel Service Dispatch System")
    print("Now Displaying Overall Distance Traveled:")
    #This will show us a Total Distance Traveled for all 3 trucks
    print(Truck_1.distance + Truck_2.distance + Truck_3.distance)
    print("Now displaying Individual Truck Distances Traveled:")
    print("Truck 1 Total Distance Traveled:", Truck_1.distance,  "Miles")
    print("Truck 2 Total Distance Traveled:", Truck_2.distance, "Miles")
    print("Truck 3 Total Distance Traveled:", Truck_3.distance, "Miles")
    # User interaction starts here! User will be asked to type "begin" to start.
    text = input("To Initiate Use, Please enter 'begin'. All other inputs will exit the program.")
   #
    if text == "begin":
        try:
            while True:
                # Operator will be prompted to enter a specific time query
                user_time = input("Time of Day Required to Continue. Please enter time as shown: HH-MM-SS")
                (h, m, s) = user_time.split("-")
                convert_timedelta = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # This next section enables the user to choose between tracking an individual parcel, or a master list of all parcels en route.
                parcel_list_input = input("To view individual parcel information, enter 'one'. For a rundown of every parcel, enter 'master'.")
                # here is the code segment for viewing one individual parcel
                if parcel_list_input == "one":
                    try:
                        # The parcel ID info will be recorded here
                        one_parcel = input("Please enter singular Parcel ID Number: ")
                        parcel = parcel_hash.lookup(int(one_parcel))
                        #print(parcel.print_status(convert_timedelta))
                        print(parcel.print_status(convert_timedelta))
                    except ValueError:
                        print("Unrecognized Command Entered. Program Exiting.")
                        exit()
                # The Commands for the databases master list are here
                elif parcel_list_input == "master":
                    try:
                        for parcelID in range(1, 41):
                            parcel = parcel_hash.lookup(parcelID)
                           # print(parcel.print_status(convert_timedelta))
                            print(parcel.print_status(convert_timedelta))
                    except ValueError:
                        print("Unrecognized Command Entered. Program Exiting.")
                else:
                    exit()
        except ValueError:
            print("Unrecognized Command Entered. Program Exiting.")
            exit()
    elif input != "begin":
        print("ERROR! Unrecognized Command Entered. Program Exiting.")
        exit()