import json
from rich import print

class JsonDB:
    """
    Base class for a simple JSON "database."

    Attributes:
        filepath (str): Path to the JSON file on disk.
        data (any): The loaded JSON data (e.g., list, dict).
    """
    def __init__(self, filepath):
        """
        Initialize the DB with a path to the JSON file.
        """
        self.filepath = filepath
        self.data = None
        self._load_data()
        self.current = 0

    def _load_data(self):
        """
        Internal helper to load JSON data from the file into self.data.
        Handle exceptions and set self.data appropriately if file is missing/corrupted.
        """
        with open(self.filepath) as f:
            self.data = json.load(f)

    def _save_data(self):
        """
        Internal helper to save self.data back to the JSON file.
        """
        with open(self.filepath, 'w') as f:
                json.dump(self.data, f, indent=4)

    def create(self, record):
        """
        Insert a new record into self.data.
        'record' could be a dict or some structure that matches the data layout.
        Return the inserted record or some identifier.
        """
        self.data.append(record)
        self._save_data()
        return record

    def read(self, **filters):
        """
        Read/search the database.
        E.g., read(name="Teresa", city="Los Angeles") might filter by matching fields.
        Return a list of matching records or a single record.
        """
        results = [
            record for record in self.data
            if all(record.get(k) == v for k, v in filters.items())
        ]
        return results

    def update(self, record_id, updated_data):
        """
        Update an existing record by some identifier.
        Return the updated record, or raise an error if not found.
        """
        for record in self.data:
            if record.get("id") == record_id:
                record.update(updated_data)
                self._save_data()
                return record
        raise ValueError(f"Record with id {record_id} not found.")

    def delete(self, record_id):
        """
        Remove a record by its identifier.
        Return the deleted record, or raise an error if not found.
        """
        for record in self.data:
            if record.get("id") == record_id:
                self.data.remove(record)
                self._save_data()
                return record
        raise ValueError(f"Record with id {record_id} not found.")


if __name__ == "__main__":
    db = JsonDB("flights.json")
    
   