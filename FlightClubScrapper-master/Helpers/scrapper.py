import requests
from Helpers import folderCreator, imageSaver

class scrapper:
    def __init__(self, payload):
        self.payload = payload

    def scrap(self):
        folder = folderCreator('Images').create()
        app_id = '2FWOTDVM2O'
        api_key = 'ac96de6fef0e02bb95d433d8d5c7038a'
        index_name = 'product_variants_v2_flight_club'
        url = f'https://{app_id}.algolia.net/1/indexes/{index_name}/query'
        headers = {
            'Content-Type': 'application/json',
            'X-Algolia-API-Key': api_key,
            'X-Algolia-Application-Id': app_id
        }
        response = requests.post(url, headers=headers, json=self.payload).json()
        if response['hits'] is not None:
            for snkr in response['hits']:
                image = snkr['original_picture_url']
                product_type = snkr['product_type']
                counter = 0
                if product_type == 'sneakers':
                    counter += 1
                    imageSaver(folder, product_type, image, counter).save()