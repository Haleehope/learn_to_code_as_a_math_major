# ###################################################################
# Build a mini earthquake database
# ###################################################################

# create a function to print the strongest earthquake in the dataset
def show_strongest():
    strongest = max(earthquakes, key=lambda quake: quake["magnitude"])
    print("Strongest earthquake:", strongest)

# create a function that prints the earthquakes at a location that the user inputs
def search_location():
    location = input("Search location: ").lower()

    for quake in earthquakes:
        if location in quake["location"].lower():
            print(quake)

# create a function that adds a new row to the dataset
# get the earthquake name, location, and magnitude and append a dictionary of those values to the list
def add_earthquake():
    name = input("Earthquake name: ")
    location = input("Location: ")
    magnitude = float(input("Magnitude: "))

    earthquakes.append({
        "name": name,
        "location": location,
        "magnitude": magnitude
    })


# Store a list of dictionaries of the given earthquakes
earthquakes = [
    {"name": "Quake A", "location": "California", "magnitude": 4.2},
    {"name": "Quake B", "location": "Alaska", "magnitude": 5.7},
    {"name": "Quake C", "location": "Japan", "magnitude": 6.1},
]

# now use a while loop to give options to the user to call any of the functions or quit
while True:
    print("\n1. Search by location")
    print("2. Add earthquake")
    print("3. Show strongest")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        search_location()
    elif choice == "2":
        add_earthquake()
    elif choice == "3":
        show_strongest()
    elif choice == "4":
        break
    else:
        print("Invalid option.")