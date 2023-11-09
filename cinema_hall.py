class Hall:
    def __init__(self, row, col, hall_no):
        self.__seats = {}
        self.__show_list = []
        self.__row = row
        self.__col = col
        self.__hall_no = hall_no
        self.__seat = [[0 for i in range(col)] for j in range(row)]

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[id] = [
            [0 for _ in range(self.__col)] for _ in range(self.__row)]

    def book_seats(self, show_id, seats_to_book):
        if show_id in self.__seats:
            show_seats = self.__seats[show_id]
            for row, col in seats_to_book:
                if 1 <= row <= self.__row and 1 <= col <= self.__col:
                    if show_seats[row - 1][col - 1] == 0:
                        show_seats[row - 1][col - 1] = 1
                    else:
                        print("Seat is already booked.")
                else:
                    print("Invalid seat.")
        else:
            print("Show not found.")

    def view_show_list(self):
        for show in self.__show_list:
            print(show)

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            show_seats = self.__seats[show_id]
            for row in show_seats:
                print(" ".join(map(str, row)))
        else:
            print("Show not found.")


class StarCinema:
    def __init__(self):
        self.hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

    def hall_by_no(self, hall_no):
        for hall in self.hall_list:
            if hall._Hall__hall_no == hall_no:
                return hall
        return None


hall1 = Hall(row=5, col=6, hall_no=1)
hall2 = Hall(row=8, col=7, hall_no=2)

hall1.entry_show(id='100', movie_name='Pathan', time='1:00 PM')
hall1.entry_show(id='101', movie_name='Jawan', time='3:00 PM')

hall2.entry_show(id='102', movie_name='Tiger 3', time='2:00 PM')
hall2.entry_show(id='103', movie_name='Don', time='4:00 PM')

cinema = StarCinema()
cinema.entry_hall(hall1)
cinema.entry_hall(hall2)

while True:
    print("Menu:")
    print("1. View all shows today")
    print("2. View available seats")
    print("3. Book tickets")
    print("4. Exit")

    option = input("Enter your choice: ")

    if option == '1':
        for hall in cinema.hall_list:
            print(f"Hall No: {hall._Hall__hall_no}")
            hall.view_show_list()
        print()
    elif option == '2':
        show_id = input("Enter Show ID: ")
        hall = None
        for i in cinema.hall_list:
            if show_id in i._Hall__seats:
                hall = i
                break
        if hall:
            hall.view_available_seats(show_id)
        else:
            print("Show not found.")
    elif option == '3':
        show_id = input("Enter Show ID: ")
        count = int(input("Enter the number of seats to book: "))
        booking_seat = []
        for _ in range(count):
            seat_input = input(f"Enter seat {_ + 1} (e.g., 1-2): ")
            seat = tuple(map(int, seat_input.split('-')))
            booking_seat.append(seat)
        hall = None
        for i in cinema.hall_list:
            if show_id in i._Hall__seats:
                hall = i
                break
        if hall:
            hall.book_seats(show_id, booking_seat)
            print("Booking successful!")
        else:
            print("Show not found.")
    elif option == '4':
        break
    else:
        print(" Please choose a valid option.")
