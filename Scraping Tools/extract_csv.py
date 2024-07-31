import json
import csv

with open('steam_data.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

def extract_dlc_id():
    dlc = {}
    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'dlc' in entry[app_id]['data']:
            dlc[app_id] = entry[app_id]['data']['dlc']
    with open('dlc_id.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['game_id', 'dlc_id'])
        for app_id, dlc_list in dlc.items():
            for dlc_id in dlc_list:
                writer.writerow([app_id, dlc_id])

def extract_language():
    with open('language_list.txt', 'r', encoding='utf-8-sig') as f:
        lang_list = f.readlines()
        lang_list = list(map(lambda x: x.replace('\n', ''), lang_list))
    language = {}

    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'supported_languages' in entry[app_id]['data']:
            langs_in_one_string = entry[app_id]['data']['supported_languages'].split(',')
            langs_in_one_string = list(map(lambda x: x.replace(' ', ''), langs_in_one_string))
            langs_in_one_string = list(map(lambda x: x.split('<')[0] if '<' in x else x, langs_in_one_string))
            langs_in_one_string = list(map(lambda x: x.split('-')[0] if '-' in x else x, langs_in_one_string))
            langs_in_one_string = list(map(lambda x: x.split('[')[0] if '[' in x else x, langs_in_one_string))
            langs_in_one_string = list(map(lambda x: x.split('(')[0] if '(' in x else x, langs_in_one_string))
            langs_in_one_string = list(map(lambda x: x.split('"')[0] if '"' in x else x, langs_in_one_string))
            langs_in_one_string = list(filter(lambda x: x in lang_list, langs_in_one_string))
            language[app_id] = langs_in_one_string
    with open('language.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['app_id', 'language'])
        for app_id, language_list in language.items():
            for lang in language_list:
                writer.writerow([app_id, lang])

def extract_genre():
    genre = {}
    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'genres' in entry[app_id]['data']:
            genres = entry[app_id]['data']['genres']
            genre[app_id] = list(map(lambda x: x['description'], genres))
    with open('genre.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['game_id', 'genre'])
        for app_id, genre_list in genre.items():
            for g in genre_list:
                writer.writerow([app_id, g])

def extract_review():
    review = {}
    for entry in data['entries']:
        app_id = entry['app_id']
        if entry['success'] is False:
            continue
        if entry['reviews'] != []:
            reviews = entry['reviews']
            for r in reviews:
                review_id = r['recommendationid']
                author = r['author']['steamid']
                voted_up = 0 if r['voted_up'] == False else 1
                review_text = r['review']
                timestamp_created = r['timestamp_created']
                if review_id is None or author is None or voted_up is None or timestamp_created is None:
                    continue
                review[review_id] = [app_id, author, voted_up, review_text, timestamp_created]
    with open('reviewID.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['review_id', 'game_id'])
        for review_id, review_info in review.items():
            writer.writerow([review_id, review_info[0]])

    with open('review.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['review_id', 'author', 'voted_up', 'review_text', 'timestamp_created'])
        for review_id, review_info in review.items():
            writer.writerow([review_id, review_info[1], review_info[2], review_info[3], review_info[4]])

def extract_app_ids():
    app_ids = []
    for entry in data['entries']:
        app_ids.append(entry['app_id'])
    with open('app_id.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['app_id'])
        for app_id in app_ids:
            writer.writerow([app_id])

def extract_game_data():
    game_data = {}
    dlc_data = {}
    soundtrack_data = {}

    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'name' not in entry[app_id]['data']:
            continue
        if 'query_summary' not in entry:
            continue
        if 'total_positive' not in entry['query_summary']:
            continue
        if 'total_reviews' not in entry['query_summary']:
            continue

        name = entry[app_id]['data']['name']
        rate_positive = entry['query_summary']['total_positive']
        rate_num = entry['query_summary']['total_reviews']
        
        if 'type' in entry[app_id]['data']:
            _type = entry[app_id]['data']['type']
            if _type == 'dlc':
                dlc_data[app_id] = [name, rate_num, rate_positive]
            elif _type == 'music':
                soundtrack_data[app_id] = [name, rate_num, rate_positive]
            else:
                game_data[app_id] = [name, rate_num, rate_positive]

    with open('game_data.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['game_id', 'name', 'rate_num', 'rate_positive'])
        for app_id, game_info in game_data.items():
            writer.writerow([app_id, game_info[0], game_info[1], game_info[2]])
    
    with open('dlc_data.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['dlc_id', 'name', 'rate_num', 'rate_positive'])
        for app_id, dlc_info in dlc_data.items():
            writer.writerow([app_id, dlc_info[0], dlc_info[1], dlc_info[2]])
    
    with open('soundtrack_data.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['soundtrack_id', 'name', 'rate_num', 'rate_positive'])
        for app_id, soundtrack_info in soundtrack_data.items():
            writer.writerow([app_id, soundtrack_info[0], soundtrack_info[1], soundtrack_info[2]])

def extract_description():
    description = {}
    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'short_description' in entry[app_id]['data']:
            short_description = entry[app_id]['data']['short_description']
            description[app_id] = short_description
    with open('description.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['game_id', 'short_description'])
        for app_id, short_description in description.items():
            writer.writerow([app_id, short_description])

def extract_price():
    price = {}
    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'price_overview' not in entry[app_id]['data']:
            continue
        current_price = entry[app_id]['data']['price_overview']['final_formatted']
        if '$' in current_price or 'CDN' in current_price or 'Free' in current_price:
            current_price = current_price.replace('CDN', '')
            current_price = current_price.replace('Free', '0')
            current_price = current_price.replace('$', '')
            try:
                price[app_id] = float(current_price)
            except:
                price[app_id] = -1
        else:
            price[app_id] = -1
    with open('current_price.csv', 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        import time
        unix_time = int(time.time())
        writer.writerow(['game_id', 'timestamp', 'price'])
        for app_id, price_value in price.items():
            writer.writerow([app_id, unix_time, price_value])

# extract_game_data()
# extract_description()
# extract_app_ids()
# extract_review()
# extract_dlc_id()
# extract_genre()
# extract_language()
extract_price()