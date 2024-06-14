import csv


def login():
    if input("Login or Register?: ").lower() == "login":
        username = input("Enter your username: ")
        with open('user_data.csv', "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == username:
                    print("Welcome ", row[1], "\n")
                    return row[4]
            print("User not found\n")

    else:
        print("Register yourself\n\n")
        data = {}

        while True:
            username = input("Enter your username: ")
            name = input("Enter your name: ").capitalize()
            age = int(input("Enter your age: "))
            phone_no = input("Enter your phone number: ")
            user_type = input("Enter your type (normal/admin): ").capitalize()

            data[username] = [name, age, phone_no, user_type]

            with open('user_data.csv', "a", newline='') as f:
                writer = csv.writer(f)

                for key, value in data.items():
                    writer.writerow([key] + value)
            break
        return data[username][3]


def movie():
    movies_data = {}
    while True:
        movie_name = input("Enter the movie name: ").capitalize()
        movie_type = input("Enter the movie type: ")
        start_time = input("Enter the start time: ")
        end_time = input("Enter the end time: ")
        total_seats = int(input("Enter the total seats: "))
        booked_seats = int(input("Enter the booked seats: "))
        price_1_adult = int(input("Enter the price for 1 adult: "))
        price_1_child = int(input("Enter the price for 1 child: "))
        rating = input("Enter the rating: ")

        choice = input("Do you want to add more movies? (yes/no)").lower()
        if choice == "no":
            break

        movies_data[movie_name] = [movie_type,
                                   start_time,
                                   end_time,
                                   total_seats,
                                   booked_seats,
                                   price_1_adult,
                                   price_1_child,
                                   rating]

        with open("movies_data.csv", "a", newline='') as f:
            writer = csv.writer(f)
            for key, value in movies_data.items():
                writer.writerow([key] + value)


def book_ticket():
    movies_data = {}
    with open("movies_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("Movie Name: ", row[0],
                  "\nMovie Type: ", row[1],
                  "\nStart Time: ", row[2],
                  "\nEnd Time: ", row[3],
                  "\nTotal Seats: ", row[4],
                  "\nBooked Seats: ", row[5],
                  "\nPrice for 1 Adult: ", row[6],
                  "\nPrice for 1 Child: ", row[7],
                  "\nRating: ", row[8])
            print("\n")
            movies_data[row[0]] = row

    movie_name = input("Enter the movie name: ")
    if movie_name in movies_data:
        movie = movies_data[movie_name]
        print("Price for 1 Adult: ", movie[6], "\nPrice for 1 Child: ", movie[7])
        adult = int(input("\nEnter the number of adults: "))
        child = int(input("Enter the number of children: "))

        total_price = (adult * int(movie[6])) + (child * int(movie[7]))
        seats_booked = adult + child

        if seats_booked > int(movie[4]):
            print("Seats not available\n")
        else:
            confirm = str(input(("Total Price: " + str(total_price) + "\nType 'yes' to confirm booking: ")))

            if confirm == "yes":
                print("Booking confirmed\n")
                with open("movies_data.csv", "r") as f:
                    reader = csv.reader(f)
                    movies = list(reader)  # Read the file content into a list

                with open("movies_data.csv", "w", newline='') as f:
                    writer = csv.writer(f)
                    for row in movies:  # Now you can iterate over the list
                        if row[0] == movie_name:
                            row[5] = str(int(row[5]) + seats_booked)
                            writer.writerow(row)
                        else:
                            writer.writerow(row)

            else:
                print("Booking cancelled\n")
    else:
        print("Movie not found\n")



def display_users():
    with open('user_data.csv', "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("Username: ", row[0],
                  "\nName: ", row[1],
                  "\nAge: ", row[2],
                  "\nPhone Number: ", row[3],
                  "\nType: ", row[4])
            print("\n")


def display_movies():
    with open("movies_data.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print("Movie Name: ", row[0],
                  "\nMovie Type: ", row[1],
                  "\nStart Time: ", row[2],
                  "\nEnd Time: ", row[3],
                  "\nTotal Seats: ", row[4],
                  "\nBooked Seats: ", row[5],
                  "\nPrice for 1 Adult: ", row[6],
                  "\nPrice for 1 Child: ", row[7],
                  "\nRating: ", row[8])
            print("\n")


def main():
    print("\n\nWelcome to the movie ticket booking system\n")
    while True:

        user_type = login()

        if user_type == "Admin":
            while True:
                print("1. Add Movie\n"
                      "2. Display Users\n"
                      "3. Display Movies\n",
                      "4. Exit\n")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    movie()
                elif choice == 2:
                    display_users()
                elif choice == 3:
                    display_movies()
                elif choice == 4:
                    break
                else:
                    print("Invalid choice\n")

        elif user_type == "Normal":
            while True:
                print("1. Book Ticket\n"
                      "2. Display Movies\n",
                      "3. Exit\n")
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    book_ticket()
                elif choice == 2:
                    display_movies()
                elif choice == 3:
                    break
                else:
                    print("Invalid choice\n")

        break


if __name__ == "__main__":
    main()
