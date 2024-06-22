import requests
import csv
import json


url1 = "https://store.steampowered.com/appreviews/{}?json=1&review_type=all&purchase_type=all&language=all&num_per_page=0"
url2 = "https://store.steampowered.com/api/appdetails?appids={}"

app_id_dir = './app_id.csv'
with open(app_id_dir, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    counter = 0
    result = []
    for row in reader:
        app_id = row[0]
        print("API call for ", app_id)

        review_response = requests.get(url1.format(app_id))
        game_response = requests.get(url2.format(app_id))

        review_data = json.loads(review_response.content.decode('utf-8-sig'))
        game_data = json.loads(game_response.content.decode('utf-8-sig'))

        if review_data is None:
            continue
        if game_data is None:
            continue
        
        if review_data['success'] == 0:
            continue
        if game_data[app_id]['success'] == 0:
            continue

        if 'supported_languages' not in game_data[app_id]['data']:
            continue
        if 'header_image' not in game_data[app_id]['data']:
            continue

        total_reviews = review_data['query_summary']['total_reviews']
        positive_reviews = review_data['query_summary']['total_positive']

        name = game_data[app_id]['data']['name']
        name = name.replace(',', '')
        
        # languages = game_data[app_id]['data']['supported_languages']
        # languages = languages.replace('\r', '')
        # languages = languages.replace('\n', '')
        # languages = languages.replace('\t', '')
        # languages = languages.split(',')
        # languages = languages.replace(' ', '')
        # languages = list(map(lambda x: x.split('[')[0], languages))
        # languages = list(map(lambda x: x.split('<')[0], languages))
        # languages = '|'.join(languages)
        
        result.append([app_id, name, total_reviews, positive_reviews])

        counter += 1
        if counter >= 100:
            result = '\n'.join([','.join(map(str, item)) for item in result])
            with open('game.csv', 'a', encoding='utf-8-sig') as file:
                file.write(f'{result}\n')
            counter = 0
            result = []
    