from jsonDB import JsonDB 
from rich import print


class FlightsDB(JsonDB):
    """
    Class for a simple JSON "database" specifically for flight records.
    Inherits from JsonDB to handle JSON file operations.
    """
    def __init__(self, filepath):
        """
        Initialize the FlightsDB with a path to the JSON file.
        """
        super().__init__(filepath)
        self.current = 0  # Initialize current index for iteration
        self._load_data()
        self._save_data()
    
    def create(self, record):
        """
        Insert a new flight record into the database.
        'record' should be a dictionary with flight details.
        """
        # Check if the record already exists
        for existing_record in self.data:
            if existing_record["id"] == record["id"]:
                print(f"[red]Record with ID {record['id']} already exists.[/red]")
                return None

        # Append the new record and save to file
        self.data.append(record)
        self._save_data()
        return record
    
    def read(self, **filters):
        """
        Read/search the database for flight records.
        Filters can be applied to search for specific records.
        """
        id = filters.get("id", None)
        first_name = filters.get("first_name", None)
        last_name = filters.get("last_name", None)
        email = filters.get("email", None)
        departure_city = filters.get("departure_city", None)
        arrival_city = filters.get("arrival_city", None)

        records = []
        flights ={}

        

        if id:
            i = 0
            for record in self.data:
                if record["id"] == int(id):
                    records.append(record)
                i += 1

        elif first_name:
            i = 0
            for record in self.data:
                if record["first_name"] == first_name:
                    records.append(record)
                i += 1

        elif last_name:
            i = 0
            for record in self.data:
                if record["last_name"] == last_name:
                    records.append(record)
                    i += 1

        elif email:
            i = 0
            for record in self.data:
                if record["email"] == email:
                    records.append(record)
                    i += 1

        elif departure_city:    
            i = 0
            for record in self.data:
                if record["departure_city"] == departure_city:
                    records.append(record)
                    i += 1

        elif arrival_city:
            i = 0
            for record in self.data:
                if record["arrival_city"] == arrival_city:
                    records.append(record)
                    i += 1

        return records
    
    def update(self, id, updated_data):
        """
        Update an existing flight record by its ID.
        'updated_data' should be a dictionary with the fields to update.
        """
        for record in self.data:
            if record["id"] == id:
                record.update(updated_data)
                self._save_data()
                return record
        print(f"[red]Record with ID {id} not found.[/red]")
        return None
    
    def delete(self, id):
        print(f"[red]Deleting row ID: {row_id}[/red]")
        del [row_id]

if __name__ == "__main__":
    db = FlightsDB("flights.json")

    data = db.read(id=500)
    print(data)
                