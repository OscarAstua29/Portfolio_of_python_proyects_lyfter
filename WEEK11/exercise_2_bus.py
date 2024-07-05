import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Bus:

    max_passenger = 10

    def __init__(self):
        self.person = 0

    def add_passengers(self):
        
        if self.person < self.max_passenger:
            self.person += 1
            print("A PERSON GOT ON THE BUS")
        elif self.person == self.max_passenger:
            clear_screen()
            input("THE BUSS IS FULL, PRESS ENTER TO CONTINUE")

    def remove_passengers (self):
        clear_screen()
        while self.person != 0:
            self.person -= 1
            print("A PERSON GOT OFF THE BUS")

        input("THE BUSS IS EMPTY, PRESS ENTER TO CONTINUE")


my_bus = Bus()

while True:
    clear_screen()
    print("NUMBER OF PASSENGERS: ", my_bus.person)
    try:
        option = int(input("PRESS 1 TO ADD A PASSENGER\nPRESS 2 TO REMOVE A PASSENGER\n ENTER AN OPTION: "))
        if option == 1:
            my_bus.add_passengers()
        else:
            my_bus.remove_passengers()

    except ValueError:
        input("INVALID INPUT, PLEASE ENTER A VALID VALUE, PRESS ENTER TO CONTINUE")