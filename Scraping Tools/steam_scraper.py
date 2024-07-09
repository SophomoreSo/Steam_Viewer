import requests
import csv
import json


url1 = "https://store.steampowered.com/appreviews/{}?json=1&review_type=all&purchase_type=all&language=english"
url2 = "https://store.steampowered.com/api/appdetails?appids={}"

output_json = 'steam_data.json'
log_file = 'steam_data_log.txt'

app_id_dir = 'ids.txt'
with open(app_id_dir, 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    result = []
    for row in reader:
        try: 
            app_id = row[0]
            print("API call for ", app_id)

            review_response = requests.get(url1.format(app_id))
            game_response = requests.get(url2.format(app_id))

            game_data = json.loads(game_response.content.decode('utf-8-sig'))
            review_data = json.loads(review_response.content.decode('utf-8-sig'))

            data = {**game_data, **review_data}
            data['app_id'] = app_id
            with open('steam_data.json', 'a', encoding='utf-8-sig') as f:
                json.dump(data, f, indent=4)
                f.write('\n,')
        except:
            with open(log_file, 'a', encoding='utf-8-sig') as f:
                f.write(f"API call for {app_id} failed\n")