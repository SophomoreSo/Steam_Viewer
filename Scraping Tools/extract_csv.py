import json
import csv

with open('steam_data.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

def extract_dlc():
    dlc = {}
    for entry in data['entries']:
        app_id = entry['app_id']
        if entry[app_id]['success'] is False:
            continue
        if 'dlc' in entry[app_id]['data']:
            dlc[app_id] = entry[app_id]['data']['dlc']
    with open('dlc.csv', 'w', encoding='utf-8-sig', newline='') as f:
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

extract_review()