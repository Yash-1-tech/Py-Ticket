import pyfiglet
from my_utilities.my_functions import get_input
import json
from pathlib import Path

registered_users = ["User_1", "User_2"]
train_seats_data = Path("data/train_seats.json")

class Train:
    def __init__(self):
        with open(train_seats_data,"r") as data:
            self.seats_data = json.load(data) 

    def book_lower(self):
        if self.seats_data["seats"]["lower_seats"] > 0:
            self.seats_data["seats"]["lower_seats"] -= 1
            with open(train_seats_data,"w") as file:
                json.dump(self.seats_data, file, indent=4)
        else:
            return "Full"
        print("Lower seat booked successfully!")

    def book_upper(self):
        if self.seats_data["seats"]["upper_seats"] > 0:
            self.seats_data["seats"]["upper_seats"] -= 1
            with open(train_seats_data,"w") as file:
                json.dump(self.seats_data, file, indent=4)
        else:
            return "Full"
        print("Upper seat booked successfully!")

    def book_middle(self):
        if self.seats_data["seats"]["middle_seats"] > 0:
            self.seats_data["seats"]["middle_seats"] -= 1
            with open(train_seats_data,"w") as file:
                json.dump(self.seats_data, file, indent=4)
        else:
            return "Full"
        print("Middle seat booked successfully!")


def main():
    f = pyfiglet.Figlet(font="slant")  
    print(f.renderText("WELCOME TO PY-TICKET"))
    username = get_verified_user()
    name, age, passenger_count = get_booking_details()
    seat_type = book_ticket(age)
    create_ticket(username, name, age, passenger_count, seat_type)


def get_verified_user():
    while True:
        username = get_input(prompt="Enter your PY-TICKET Username: ", required=True)
        if username not in registered_users:
            print("Not a registered user! ")
            continue
        return username


def get_booking_details():  
    print("ENTER YOUR BOOKING DETAILS HERE!")
    passenger_count = get_input(prompt="How many passengers would you like to book seats for? ", input_type="int", error_prompt="Not a valid passenger amount!")
    name=[]
    age=[]
    for i in range(passenger_count):
        print (f"\nPassenger {i+1}")
        name.append(get_input(prompt="Name: ", required=True))
        age.append(get_input(prompt="Age: ", required=True, input_type="int", error_prompt="Not a valid age!"))
    return (name, age, passenger_count)


def book_ticket(a):  # ADD ALGORITHM TO BOOK SEAT TYPE BASED ON AGE FILTERING
    train = Train()
    train.book_lower()
    return "Lower-seat"


def create_ticket(username, name, age, passenger_count, seat_type):  # only displays the latest passenger ticket in ticket.txt (save ticket data somewhere).
    for i in range(passenger_count):
        with open("ticket.txt", "w") as file:
            file.write(
                f"Ticket under : {username}\n Name: {name[i]}\n Age: {age[i]}\n Seat: {seat_type}"
            )


if __name__ == "__main__":
    main()
