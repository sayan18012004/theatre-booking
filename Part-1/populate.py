import csv

def populate_users():
    users = [
        ["johndoe", "John Doe", 30, "1234567890", "Normal"],
        ["janedoe", "Jane Doe", 28, "0987654321", "Admin"],
        ["alice", "Alice Wonderland", 25, "1112223333", "Normal"],
        ["bob", "Bob Builder", 35, "4445556666", "Admin"],
        ["charlie", "Charlie Chaplin", 40, "7778889999", "Normal"],
        ["diana", "Diana Prince", 32, "2223334444", "Admin"],
        ["eve", "Eve Adams", 27, "5556667777", "Normal"],
        ["frank", "Frank Sinatra", 45, "8889990000", "Admin"],
        ["grace", "Grace Hopper", 38, "1114447777", "Normal"],
        ["henry", "Henry Ford", 50, "2225558888", "Admin"]
    ]

    with open('user_data.csv', "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Username", "Name", "Age", "Phone Number", "Type"])  # Write header
        writer.writerows(users)
    print("User data populated successfully.")

def populate_movies():
    movies = [
        ["Inception", "Sci-Fi", "14:00", "16:30", 100, 50, 150, 100, "PG-13"],
        ["Avengers", "Action", "17:00", "19:30", 200, 150, 200, 150, "PG-13"],
        ["Frozen", "Animation", "10:00", "11:45", 150, 75, 120, 80, "G"],
        ["Titanic", "Romance", "20:00", "22:45", 180, 90, 180, 120, "PG-13"],
        ["Matrix", "Sci-Fi", "16:00", "18:30", 120, 60, 170, 110, "R"],
        ["Toy Story", "Animation", "09:00", "10:45", 130, 65, 110, 70, "G"],
        ["Avatar", "Sci-Fi", "12:00", "14:45", 210, 105, 220, 150, "PG-13"],
        ["Coco", "Animation", "11:00", "12:45", 140, 70, 130, 90, "PG"],
        ["Gladiator", "Action", "19:00", "21:30", 160, 80, 190, 130, "R"],
        ["Up", "Animation", "08:00", "09:45", 120, 60, 100, 70, "PG"]
    ]

    with open('movies_data.csv', "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Movie Name", "Movie Type", "Start Time", "End Time", "Total Seats", "Booked Seats", "Price for 1 Adult", "Price for 1 Child", "Rating"])  # Write header
        writer.writerows(movies)
    print("Movie data populated successfully.")

def main():
    populate_users()
    populate_movies()

if __name__ == "__main__":
    main()
