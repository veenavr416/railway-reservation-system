# Railway Reservation System
# Total seats
total_seats = 50
available_seats = total_seats
# Store bookings
bookings = {}
# Function to check availability
def check_availability():
    print("\nAvailable Seats:", available_seats)
# Function to book ticket
def book_ticket():
    global available_seats
      if available_seats <= 0:
        print("\n No seats available!")
        return
     name = input("Enter Name: ")
    age = input("Enter Age: ")
     booking_id = len(bookings) + 1
     bookings[booking_id] = {
        "name": name,
        "age": age
    }
     available_seats -= 1
    print("\n Ticket Booked Successfully!")
    print("Booking ID:", booking_id)
# Function to view ticket
def view_ticket():
    bid = int(input("Enter Booking ID: "))
      if bid in bookings:
        print("\n Ticket Details:")
        print("Name:", bookings[bid]["name"])
        print("Age:", bookings[bid]["age"])
    else:
        print("\n Booking not found!")
# Function to cancel ticket
def cancel_ticket():
    global available_seats
     bid = int(input("Enter Booking ID to cancel: "))
    if bid in bookings:
        del bookings[bid]
        available_seats += 1
        print("\n Ticket Cancelled Successfully!")
    else:
        print("\n Invalid Booking ID!")
# Main menu loop
while True:
    print("\n===== Railway Reservation System =====")
    print("1. Check Availability")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")
     choice = input("Enter your choice: ")
     if choice == '1':
        check_availability()
         elif choice == '2':
        book_ticket()
        elif choice == '3':
        view_ticket()
          elif choice == '4':
        cancel_ticket()
          elif choice == '5':
        print("\nThank you for using the system!")
        break
          else:
        print("\n Invalid choice! Please try again.")
