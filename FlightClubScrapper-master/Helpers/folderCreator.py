import os
class folderCreator:
    def __init__(self, name) -> None:
        self.name = name
    
    def create(self):
        folder = f'{self.name}'
        if not os.path.exists(folder):
            os.makedirs(folder)
        return folder