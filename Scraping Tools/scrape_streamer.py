import requests
import csv
from bs4 import BeautifulSoup

url = f"https://www.twitchmetrics.net/channels/follower?game="

def get_streamers(url):
    response = requests.get(url)
    print(url)
    print(response.status_code)
    soup = BeautifulSoup(response.text, 'html.parser')
    streamers = []
    for streamer in soup.select('li.list-group-item'):
        name = streamer.select_one('h5.mr-2').text
        link = streamer.select_one('.mb-2 a')['href']
        followers = streamer.select_one('samp').text
        streamers.append({
            "name": name,
            "followers": followers,
            "link": link,
        })
    return streamers

import time

game_list_dir = "game_list.csv"
output = "streamers.csv"

game_list = {}
with open(game_list_dir, "r", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        game_list[row["game_name"]] = row["app_id"]

for game, appid in game_list.items():
    try:
        encoded_game = "".join([c for c in game if c.isalnum() or c in [" ", "-", "_", ":", "'"]])
        encoded_game = encoded_game.replace(" ", "+")
        streamers = get_streamers(url + encoded_game)
        if streamers == []:
            with open("error_log.txt", "a", encoding="utf-8-sig") as f:
                f.write(f"No streamers found for {game} -> {encoded_game}\n")
            continue
        else: 
            with open(output, "a", encoding="utf-8-sig", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["app_id", "game", "name", "followers", "link"])
                for streamer in streamers:
                    writer.writerow({
                        "app_id": appid,
                        "game": game,
                        "name": streamer["name"],
                        "followers": streamer["followers"],
                        "link": streamer["link"],
                    })
        time.sleep(2)
            
    except Exception as e:
        with open("error_log.txt", "a", encoding="utf-8-sig") as f:
            f.write(f"Error in {game} -> {encoded_game}: {e}\n")
        continue