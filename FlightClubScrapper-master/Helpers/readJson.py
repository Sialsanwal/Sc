import json

# class to read a json file 
class readJson:
    def __init__(self, file_name):
        self.filename = file_name
    
    def data(self):
        with open(self.filename) as f:
            data = json.load(f)
        return data