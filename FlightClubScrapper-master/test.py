numericFilters_list = [
    '',
    'numericFilters=[\\"release_year<={release_year}\\"]',
]

# Facet filters
facetFilters_list = [
    '',
    'facetFilters=[[\\"brand_name:{brand_name}\\"]]',
    'facetFilters=[[\\"brand_name:{brand_name}\\"][\\"silhouette:{brand_model}\\"]]',
    'facetFilters=[[\\"brand_name:{brand_name}\\"][\\"silhouette:{brand_model}\\"][\\"shoe_condition:{shoe_condition}\\"]]',
    'facetFilters=[[\\"brand_name:{brand_name}\\"][\\"silhouette:{brand_model}\\"][\\"shoe_condition:{shoe_condition}\\"][\\"size_us_men:{size_us_men}\\"]]',
    'facetFilters=[[\\"brand_name:{brand_name}\\"][\\"silhouette:{brand_model}\\"][\\"shoe_condition:{shoe_condition}\\"][\\"size_us_men:{size_us_men}\\"][\\"size_us_women:{size_us_women}\\"]]',
    'facetFilters=[[\\"brand_name:{brand_name}\\"][\\"silhouette:{brand_model}\\"][\\"shoe_condition:{shoe_condition}\\"][\\"size_us_men:{size_us_men}\\"][\\"size_us_women:{size_us_women}\\"][\\"size_us_youth:{size_us_youth}\\"]]',
    'facetFilters=[[\\"brand_name:{brand_name}\\"][\\"silhouette:{brand_model}\\"][\\"shoe_condition:{shoe_condition}\\"][\\"size_us_men:{size_us_men}\\"][\\"size_us_women:{size_us_women}\\"][\\"size_us_youth:{size_us_youth}\\"][\\"color:{color}\\"]]'
]

bname = 'adidas'
bmodel = 'yeezy-boost-350-v2'
shoe_condition = 'new'
size_us_men = '40'
size_us_women = '40'
size_us_youth = '40'
color = 'black'
release_year = '2019'

for numericFilters in numericFilters_list:
    for facetFilters in facetFilters_list:
        url = facetFilters.format(
            brand_name=bname,
            brand_model=bmodel,
            shoe_condition=shoe_condition,
            size_us_men=size_us_men,
            size_us_women=size_us_women,
            size_us_youth=size_us_youth,
            color=color,
        )
        print(url)