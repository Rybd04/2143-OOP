from rich import print
from flightsDB import FlightsDB



menu = """
*****************************************************************************

1. Add New Row 
    Example: 
        id      first_name      last_name       email       departure_city      arrival_city
        999 Bob "Lopez Smith" blopezsmith@gmail.com Los Angeles New York

2. Search 
    Example:
        id 999
        first_name Bob 
        last_name "Lopez Smith"
        email blopezsmith@gmail.com
        departure_city Los Angeles
        arrival_city New York

3. Update
    Same as search criteria
    Example:
        id 102

4. Delete (row id is mandatory)
    Same as search criteria
    Example:
      id 999


*****************************************************************************
"""


def get_user_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        print("\nExiting...")
        exit(0)
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)

db = FlightsDB("flights.json")

while 1:
    print("Welcome to the Flight Database Management System")
    print(menu)
    choice = get_user_input("Enter your choice: ")
    if choice == "1":
        print("Adding new row...")
        row = input("Enter all the fields separated by space: \n").split( )
        print(row)
        for item in row:
            print(item)

    elif choice == "2":
        print("Searching...")
        k,v = input("Enter search criteria: \n").strip().split()
        if k == "id":
            search = db.read(id = v)
        elif k == "first_name":
            search = db.read(first_name = v)
        elif k == "last_name":
            search = db.read(last_name = v)
        elif k == "email":
            search = db.read(email = v)
        elif k == "departure_city":
            search = db.read(departure_city = v)
        elif k == "arrival_city":
            search = db.read(arrival_city = v)
        print(search)
        for item in search:
            if ":" in item:
                key, value = item.split()
                print(f"Key: {key}, Value: {value}")

    elif choice == "3":
        print("Updating...")
        print("Enter row ID to update")
        k == "id"
        search = db.update(id = v)
        update = input("Enter the update criteria: \n")
        update = update.split()
        print(update)

    elif choice == "4":
        print("Deleting row...")
        print("Search for the row to delete")
        search = input("Enter the search criteria: \n")
        search = search.split( )
        for item in search:
            if ":" in item:
                key, value = item.split( )
                print(f"Key: {key}, Value: {value}")
        delete = input("Enter the delete criteria: \n")
        delete = delete.split()
        print(delete)

    elif choice == "5":
        print("Exiting...")
        break