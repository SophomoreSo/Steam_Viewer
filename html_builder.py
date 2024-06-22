import bs4

# Uses builder pattern to create HTML elements

index_html_dir = "./page.html"
game_html_dir = "./game_page.html"

class IndexPage:
    def __init__(self):
        self.reset()
        self.parser = bs4.BeautifulSoup(self.html, 'html.parser')
    
    def setNavigator(self, total_page, current_page=1):
        if total_page == 1:
            return

        fixed_bar = self.parser.find('div', {'class': 'fixed-bar'})

        if total_page <= 5:
            for i in range(1, total_page + 1):
                fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick({i})">{i}</span>')
        else:
            if current_page <= 3:
                for i in range(1, 6):
                    fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick({i})">{i}</span>')
                fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick({total_page})">{total_page}</span>')
            elif current_page > total_page - 3:
                fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick(1)">1</span>')
                for i in range(total_page - 4, total_page + 1):
                    fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick({i})">{i}</span>')
            else:
                fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick(1)">1</span>')

                for i in range(current_page - 2, current_page + 3):
                    fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick({i})">{i}</span>')

                fixed_bar.append(f'<span class="page-index" onclick="handleIndexClick({total_page})">{total_page}</span>')


    def setSearchResultCount(self, count):
        count_str = 'No' if count == 0 else str(count)
        self.parser.find('header', {'class': 'header'}).append(f'We Found {count_str} Results.')

    def setGameList(self, game_lst):
        content = ''
        for game in game_lst:
            content += game.toHtmlElement()
        self.parser.find('div', {'id': 'content'}).append(content)

    def setSortOption(self, option):
        options = self.parser.find('select', {'id': 'sortDropdown'})
        options.find('option', {'value': option})['selected'] = 'selected'
    
    def setAscending(self, is_ascend):
        to_string = 'up' if is_ascend else 'down'
        tag = self.parser.find('div', {'class': 'sort-container'}).find('span', {'id': 'sortToggle'})
        tag['class'] = "sort-toggle " + to_string

    def reset(self):
        with open(index_html_dir, 'r', encoding='utf-8-sig') as file:
            self.html = file.read()

    def build(self):
        import html
        soup = self.parser
        html_result = soup.prettify()
        html_result = str(soup)
        html_result = html.unescape(html_result)
        return html_result
    
class GamePage:
    def __init__(self):
        self.reset()
        self.parser = bs4.BeautifulSoup(self.html, 'html.parser')

    def setGameImage(self, image_src):
        self.parser.find('div', {'class': 'game-info'}).find('img')['src'] = image_src

    def setGameName(self, name):
        self.parser.find('div', {'class': 'game-details'}).find('h1').string = name

    def setGamePrice(self, price):
        self.parser.find('div', {'class': 'game-details'}).find('h2').string = f'Price: ${price}'

    def setPriceHistory(self, price_history):
        import json
        from datetime import datetime
        
        price_history = list(zip(*price_history))

        timestamp_list = list(map(lambda x: datetime.fromtimestamp(x / 1000), price_history[0]))
        timestamp_list = list(map(lambda x: x.strftime('%Y-%m-%d %H:%M:%S'), timestamp_list))
        prices_list = list(map(float, price_history[1]))

        price_history_data = {
            "labels": timestamp_list,
            "datasets": [{
                "data": prices_list,
                "borderColor": 'rgba(75, 192, 192, 1)',
                "backgroundColor": 'rgba(75, 192, 192, 0.2)',
                "fill": True,
                "tension": 0.0
            }]
        }
        price_history_data = json.dumps(price_history_data)
        script_tag = self.parser.find('script', text=lambda x: x and '{priceHistoryData}' in x).string
        script_tag = script_tag.replace('{priceHistoryData}', price_history_data)
        self.parser.find('script', text=lambda x: x and '{priceHistoryData}' in x).string = script_tag

    def reset(self):
        with open(game_html_dir, 'r', encoding='utf-8-sig') as file:
            self.html = file.read()
    
    def build(self):
        import html
        soup = self.parser
        html_result = soup.prettify()
        html_result = str(soup)
        html_result = html.unescape(html_result)
        return html_result