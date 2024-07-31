class GamePageData:
    def __init__(self, app_id, title, price, rate_num, rate_positive, historically_low):
        self.app_id = app_id
        self.title = title
        self.price = price
        self.historically_low = historically_low
        self.rate_num = rate_num
        self.rate_positive = rate_positive
        # derived attribute
        self.image_src = f'https://cdn.akamai.steamstatic.com/steam/apps/{app_id}/header.jpg'

    def toHtmlElement(self):
        HL = ''
        rating = int(self.rate_positive * 100 // self.rate_num)
        if self.historically_low:
            HL = r'<div class="historically-low">HL</div>'
        if self.price < 0:
            price = 'NA'
        else:
            price = self.price
        result = f'''
        <div class="game-card" style="animation-delay: 0s;">
            <img src="{self.image_src}" onclick="handleClick({self.app_id})">
            <div class="game-details">
                <div class="game-title" onclick="handleClick({self.app_id})">{self.title}</div>
                <div class="game-price">
                    ${price}
                    {HL}
                    <span class="positive-rating">{rating}%</span>
                    <span class="positive-rating">({self.rate_num})</span>
                </div>
            </div>
        </div>
        '''
        return result