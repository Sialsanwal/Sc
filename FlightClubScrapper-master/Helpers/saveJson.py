import json

class saveJson:
    def __init__(self, json_data, file_name):
        self.json_data = json_data
        self.filename = file_name
    
    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.json_data, f, indent=4)