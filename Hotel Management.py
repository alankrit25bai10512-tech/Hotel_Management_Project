import random
from datetime import datetime

class HotelManagement:
    def __init__(self):
        self.rooms = {} 
        self.room_price = 1500 
        print("\n--- Hotel Management System Initialized ---")

    def check_in(self):
        print("\n--- GUEST CHECK-IN ---")
        try:
            name = input("Enter Guest Name: ")
            phone = input("Enter Phone Number: ")
            address = input("Enter Address: ")
            room_no = random.randint(101, 500)
            while room_no in self.rooms:
                room_no = random.randint(101, 500)
            self.rooms[room_no] = {
                'name': name,
                'phone': phone,
                'address': address,
                'room_rent': self.room_price,
                'food_bill': 0,
                'checkin_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }            
            print(f"\n✅ Check-in Successful!")
            print(f"Guest: {name}")
            print(f"Allocated Room Number: {room_no}")           
        except ValueError:
            print("❌ Error: Invalid input.")
    def room_service(self):
        print("\n--- ROOM SERVICE ---")
        try:
            room_no = int(input("Enter Room Number: "))           
            if room_no in self.rooms:
                print("--- Menu ---")
                print("1. Tea/Coffee (30)")
                print("2. Breakfast (150)")
                print("3. Lunch/Dinner (300)")               
                choice = int(input("Enter choice (1-3): "))
                cost = 0                
                if choice == 1: cost = 30
                elif choice == 2: cost = 150
                elif choice == 3: cost = 300
                else: 
                    print("Invalid choice.")
                    return
                self.rooms[room_no]['food_bill'] += cost
                print(f"✅ Ordered successfully! Current Food Bill: {self.rooms[room_no]['food_bill']}")
            else:
                print("❌ Room not occupied or does not exist.")
        except ValueError:
            print("❌ Error: Please enter numbers only.")
    def guest_status(self):
        print("\n--- CURRENTLY OCCUPIED ROOMS ---")
        if not self.rooms:
            print("No guests currently checked in.")
        else:
            print(f"{'Room No':<10} {'Guest Name':<20} {'Phone':<15}")
            print("-" * 45)
            for room, details in self.rooms.items():
                print(f"{room:<10} {details['name']:<20} {details['phone']:<15}")
    def check_out(self):
        print("\n--- GUEST CHECK-OUT ---")
        try:
            room_no = int(input("Enter Room Number: "))            
            if room_no in self.rooms:
                details = self.rooms[room_no]
                total_bill = details['room_rent'] + details['food_bill']                
                print("\n" + "*" * 30)
                print("       HOTEL RECEIPT       ")
                print("*" * 30)
                print(f"Name: {details['name']}")
                print(f"Room No: {room_no}")
                print(f"Check-in: {details['checkin_time']}")
                print("-" * 30)
                print(f"Room Rent:    {details['room_rent']}")
                print(f"Food Bill:    {details['food_bill']}")
                print("-" * 30)
                print(f"TOTAL AMOUNT: {total_bill}")
                print("*" * 30)
                del self.rooms[room_no]
                print("\n✅ Check-out complete. Thank you for visiting!")
            else:
                print("❌ Room number not found.")               
        except ValueError:
            print("❌ Error: Invalid input.")
def main():
    hotel = HotelManagement()    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check-In")
        print("2. Room Service")
        print("3. Guest Status")
        print("4. Check-Out")
        print("5. Exit")       
        choice = input("Enter Option: ")      
        if choice == '1':
            hotel.check_in()
        elif choice == '2':
            hotel.room_service()
        elif choice == '3':
            hotel.guest_status()
        elif choice == '4':
            hotel.check_out()
        elif choice == '5':
            print("Exiting System...")
            break
        else:
            print("Invalid Option. Please try again.")
if __name__ == "__main__":
    main()