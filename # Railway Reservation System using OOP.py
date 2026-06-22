# Railway Reservation System using OOP

class Passenger:
    def __init__(self, pid, name, age, gender, mobile):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.mobile = mobile

    def display(self):
        print("Passenger ID :", self.pid)
        print("Passenger Name :", self.name)
        print("Age :", self.age)
        print("Gender :", self.gender)
        print("Mobile :", self.mobile)


class Train:
    def __init__(self, train_no, train_name, source, destination, total_seats, fare):
        self.train_no = train_no
        self.train_name = train_name
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare = fare

    def display(self):
        print("------------------------------------")
        print("Train Number :", self.train_no)
        print("Train Name :", self.train_name)
        print("Source :", self.source)
        print("Destination :", self.destination)
        print("Total Seats :", self.total_seats)
        print("Available Seats :", self.available_seats)
        print("Fare Per Ticket :", self.fare)
        print("------------------------------------")

    def check_availability(self, seats):
        return self.available_seats >= seats

    def book_seats(self, seats):
        self.available_seats -= seats

    def cancel_seats(self, seats):
        self.available_seats += seats


class Ticket:
    def __init__(self, passenger, train, seats):
        self.passenger = passenger
        self.train = train
        self.seats = seats
        self.ticket_no = passenger.name + str(passenger.pid)
        self.total_fare = seats * train.fare
        self.status = "Booked"

    def cancel_ticket(self):
        if self.status == "Booked":
            self.status = "Cancelled"
            self.train.cancel_seats(self.seats)
            print("Ticket Cancelled Successfully.")
        else:
            print("Ticket Already Cancelled.")

    def display(self):
        print("\n========== TICKET DETAILS ==========")
        print("Ticket Number :", self.ticket_no)
        print("\nPassenger Details")
        print("Name :", self.passenger.name)
        print("Age :", self.passenger.age)
        print("Gender :", self.passenger.gender)
        print("Mobile :", self.passenger.mobile)

        print("\nTrain Details")
        print("Train Number :", self.train.train_no)
        print("Train Name :", self.train.train_name)
        print("Source :", self.train.source)
        print("Destination :", self.train.destination)

        print("\nSeats Booked :", self.seats)
        print("Total Fare :", self.total_fare)
        print("Status :", self.status)
        print("====================================")


# Predefined Trains
trains = [
    Train(12627, "Kerala Express", "Trivandrum", "New Delhi", 200, 450),
    Train(12623, "Chennai Mail", "Trivandrum", "Chennai", 150, 350),
    Train(16348, "Maveli Express", "Trivandrum", "Kochi", 100, 250)
]

tickets = []


while True:
    print("\n===== Railway Reservation System =====")
    print("1. Book Ticket")
    print("2. Cancel Ticket")
    print("3. Check Seat Availability")
    print("4. Display Ticket Details")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:

        print("\nEnter Passenger Details")
        pid = input("Passenger ID: ")
        name = input("Passenger Name: ")
        age = int(input("Age: "))
        gender = input("Gender: ")
        mobile = input("Mobile Number: ")

        passenger = Passenger(pid, name, age, gender, mobile)

        print("\nAvailable Trains")
        for train in trains:
            train.display()

        train_no = int(input("Enter Train Number: "))

        selected_train = None
        for train in trains:
            if train.train_no == train_no:
                selected_train = train
                break

        if selected_train is None:
            print("Invalid Train Number")
            continue

        seats = int(input("Enter Number of Seats: "))

        if selected_train.check_availability(seats):
            selected_train.book_seats(seats)
            ticket = Ticket(passenger, selected_train, seats)
            tickets.append(ticket)

            print("\nBooking Successful")
            print("Ticket Number :", ticket.ticket_no)
            print("Total Fare :", ticket.total_fare)

        else:
            print("Seats Not Available")

    elif choice == 2:

        ticket_no = input("Enter Ticket Number: ")

        found = False
        for ticket in tickets:
            if ticket.ticket_no == ticket_no:
                ticket.cancel_ticket()
                found = True
                break

        if not found:
            print("Ticket Not Found")

    elif choice == 3:

        print("\nSeat Availability")
        for train in trains:
            print("-------------------------------")
            print("Train Number :", train.train_no)
            print("Train Name :", train.train_name)
            print("Total Seats :", train.total_seats)
            print("Available Seats :", train.available_seats)

    elif choice == 4:

        ticket_no = input("Enter Ticket Number: ")

        found = False
        for ticket in tickets:
            if ticket.ticket_no == ticket_no:
                ticket.display()
                found = True
                break

        if not found:
            print("Ticket Not Found")

    elif choice == 5:
        print("Thank You")
        break

    else:
        print("Invalid Choice")