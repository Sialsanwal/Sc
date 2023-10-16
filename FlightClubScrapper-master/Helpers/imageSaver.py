import os
import requests
class imageSaver:
    def __init__(self, page, all_counter, type_name, ImgLink, counter):
        self.page = page
        self.itr = all_counter
        self.type_name = type_name
        self.ImgLink = ImgLink
        self.counter = counter
        self.folderName = f'images/{self.page}/{self.type_name}'
        folderName = 'Images'

    def save(self):
        imgName = f'{self.all_counter}_{self.page}_{self.type_name}_sneaker_{self.counter}.jpg'
        imgPath = os.path.join(self.folderName, imgName)
        with open(imgPath, 'wb') as f:
            f.write(requests.get(self.ImgLink).content)
            print(f'Saved {imgName} to {self.folderName}')