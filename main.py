# This Python file uses the following encoding: utf-8
import os, sys
class product():
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity
    
    def add_quantity(self,added_quantity):
        self.quantity += int(added_quantity)
        return f"Adding {added_quantity} to {self.quantity - int(added_quantity)}...\nThere are now {self.quantity} {self.id}'s."
    def get_total_price_of_stock(self):
        return f"The total price of the {self.id} stock is ${(self.price * float(self.quantity)):.2f}"
    
barbie = product(7.99, "Barbie Doll", 100)

print(f"There are {str(barbie.quantity)} {barbie.id}'s in inventory.")

added_barbies = 100

program_running = True

while program_running:
    print("Hello! Would you like to:")
    user_choice = input("1. Add more Barbies.\n2. Get the total price of Barbie stock\n3. Quit\n")

    match user_choice:
        case "1":
            added_quantity = input("What is the added quantity? ")
            print(f"{barbie.add_quantity(added_quantity)}")
        case "2":
            print(f"{barbie.get_total_price_of_stock()}")
        case "3":
            print("Quitting program...")
            program_running = False
        case _:
            print("Not a valid command.")

exit