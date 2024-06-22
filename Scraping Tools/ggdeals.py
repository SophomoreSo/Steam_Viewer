import requests
import bs4

for i in range(1, 6004):
    print(f"Working on Page {i}...")
    response = requests.get(f'https://gg.deals/games/?page={i}&type=1')

    result = []

    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    selected_objects = soup.select('.with-full-link a.full-link')
    for item in selected_objects:
        href = item['href']
        url = f'https://gg.deals{href}'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        selector = ".flex-column a.score-grade"
        selected_objects = soup.select(selector)
        if len(selected_objects) == 0:
            print(f"This game is not supported in Steam: {url}")
            continue
        rating = selected_objects[0].text
        rating = rating.replace(',', '')
        app_id = selected_objects[0]['href'].split('/')[4]

        selector = ".game-header-box"
        selected_objects = soup.select(selector)
        container_id = selected_objects[0]['data-container-game-id']

        result.append([app_id, rating, container_id])
    result = '\n'.join([','.join(map(str, item)) for item in result])
    with open('data.csv', 'a', encoding='utf-8-sig') as file:
        file.write(f'{result}\n')
    