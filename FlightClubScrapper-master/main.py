import requests
from Helpers import readJson, folderCreator
import os
folderName = folderCreator("Images").create()

def save(all_counter, type_name, ImgLink, counter):
    imgName = f'{all_counter}_{type_name}_sneaker_{counter}.jpg'
    imgPath = os.path.join(folderName, imgName)
    with open(imgPath, 'wb') as f:
        f.write(requests.get(ImgLink).content)
        print(f'Saved {imgName} to {folderName}')

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Origin': 'https://www.flightclub.com',
    'Referer': 'https://www.flightclub.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.57',
    'content-type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Microsoft Edge";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

json_holder = readJson("Payloads/data.json").data()
all_counter = 0

# first iterate years and shoe condition, us_men_size, us_women_size one by one after every year is printed






sneaker_count = 0
total_pages = 0
for bri, brands in enumerate(json_holder['brands']):
    for bmi, brand_models in enumerate(brands['models']):
        for syi, size_us_youth in enumerate(json_holder['size_us_youth']):
            for sci, shoe_condition in enumerate(json_holder['shoe_condition']):
                for smi, size_us_men in enumerate(json_holder['size_us_men']):
                    for swi, size_us_women in enumerate(json_holder['size_us_women']):
                        for ci, colors in enumerate(json_holder['color']):
                            for itr, year in enumerate(json_holder['years']):
                                brandName = json_holder["brands"][bri]["name"]
                                brandModel = brands["models"][bmi]["name"]
                                releasYear = json_holder["years"][itr]["name"]
                                shoeCondition = json_holder["shoe_condition"][sci]["name"]
                                sizeUsMen = json_holder["size_us_men"][smi]["name"]
                                sizeUsWomen = json_holder["size_us_women"][swi]["name"]
                                sizeUsYouth = json_holder["size_us_youth"][syi]["name"]
                                Color = json_holder["color"][ci]["name"]


                                # print all above variables
                                # if brandName != 'all':
                                # print(f'{brandName} - {brandModel} - {releasYear} - {shoeCondition} - {sizeUsMen} - {sizeUsWomen} - {sizeUsYouth} - {Color}')

                                numericFilters_list = [
                                    '',
                                    f'numericFilters=[\\"release_year<={releasYear}\\"]',
                                ]

                                # Facet filters
                                facetFilters_list = [
                                    '',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"]]',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"][\\"silhouette:{brandModel}\\"]]',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"][\\"silhouette:{brandModel}\\"][\\"shoe_condition:{shoeCondition}\\"]]',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"][\\"silhouette:{brandModel}\\"][\\"shoe_condition:{shoeCondition}\\"][\\"size_us_men:{sizeUsMen}\\"]]',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"][\\"silhouette:{brandModel}\\"][\\"shoe_condition:{shoeCondition}\\"][\\"size_us_men:{sizeUsMen}\\"][\\"size_us_women:{sizeUsWomen}\\"]]',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"][\\"silhouette:{brandModel}\\"][\\"shoe_condition:{shoeCondition}\\"][\\"size_us_men:{sizeUsMen}\\"][\\"size_us_women:{sizeUsWomen}\\"][\\"size_us_youth:{sizeUsYouth}\\"]]',
                                    f'facetFilters=[[\\"brand_name:{brandName}\\"][\\"silhouette:{brandModel}\\"][\\"shoe_condition:{shoeCondition}\\"][\\"size_us_men:{sizeUsMen}\\"][\\"size_us_women:{sizeUsWomen}\\"][\\"size_us_youth:{sizeUsYouth}\\"][\\"color:{Color}\\"]]'
                                ]

                                for numericFilter in facetFilters_list:
                                    for facetFilter in facetFilters_list:
                                        fF = facetFilter
                                        nF = numericFilter
                                        page = 0
                                        for pg in range(0, 35):
                                            snkr_counter = 0
                                            data = f'{{"requests":[{{"indexName":"product_variants_v2_flight_club","params":"distinct=true&{fF}&facets=[\\"brand_name\\",\\"silhouette\\",\\"presentation_size\\",\\"size_us_men\\",\\"size_us_women\\",\\"size_us_youth\\",\\"shoe_condition\\",\\"color\\",\\"single_gender\\",\\"category\\",\\"product_category\\",\\"designer\\",\\"collection_slugs\\",\\"is_under_retail\\",\\"lowest_price_cents_usd\\",\\"release_year\\"]&filters=&highlightPostTag=</ais-highlight-0000000000>&highlightPreTag=<ais-highlight-0000000000>&hitsPerPage=30&maxValuesPerFacet=40&{nF}&page={page}&query=&tagFilters="}},{{"indexName":"product_variants_v2_flight_club","params":"analytics=false&clickAnalytics=false&distinct=true&facets=brand_name&filters=&highlightPostTag=</ais-highlight-0000000000>&highlightPreTag=<ais-highlight-0000000000>&hitsPerPage=0&maxValuesPerFacet=40&{nF}&page={page}&query="}},{{"indexName":"product_variants_v2_flight_club","params":"analytics=false&clickAnalytics=false&distinct=true&{fF}&facets=release_year&filters=&highlightPostTag=</ais-highlight-0000000000>&highlightPreTag=<ais-highlight-0000000000>&hitsPerPage=0&maxValuesPerFacet=40&page={page}&query="}}]}}'
                                            response = requests.post(
                                                'https://2fwotdvm2o-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20JavaScript%20(4.14.3)%3B%20Browser%20(lite)%3B%20JS%20Helper%20(3.11.1)%3B%20react%20(18.2.0)%3B%20react-instantsearch%20(6.38.1)&x-algolia-api-key=ac96de6fef0e02bb95d433d8d5c7038a&x-algolia-application-id=2FWOTDVM2O',
                                                headers=headers,
                                                data=data,
                                            ).json()
                                            total_pages += 1
                                            counter = 0
                                            for snkr in response['results'][0]['hits']:
                                                sneaker_image = snkr['original_picture_url']
                                                brand_name = snkr['brand_name']
                                                missing_image = "https://cdn.flightclub.com/missing.png?w=1600"
                                                if sneaker_image != missing_image:
                                                    snkr_counter += 1
                                                    if brand_name:
                                                        # print(f'{sneaker_count}_{page}_{brand_name}_sneaker_{counter}.jpg')
                                                        save(f'{total_pages}_{sneaker_count}', brand_name, sneaker_image, counter)
                                                    else:
                                                        save(f'{total_pages}_{sneaker_count}', sneaker_image, "Null", counter)
                                                    sneaker_count += 1      
                                                    counter += 1
                                            page += 1                         