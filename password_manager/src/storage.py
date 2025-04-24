import json

class Storage:
    def __init__(self, file_path="passwords.json"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        """Load existing data from file."""
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return empty dict if file doesn't exist

    def save_data(self):
        """Save data to file."""
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_entry(self, service, username, encrypted_password, notes):
        """Add a new entry to the storage."""
        self.data[service] = {
            "username": username,
            "password": encrypted_password,
            "notes": notes
        }
        self.save_data()

    def get_entry(self, service):
        """Retrieve entry by service name."""
        return self.data.get(service, None)
