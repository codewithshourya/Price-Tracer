import requests
from bs4 import BeautifulSoup

class PriceTracer:
    def __init__(self, url):
        self.url = url
        # Enhanced headers to better mimic a real browser
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }
        
        
        self.session = requests.Session()
        self.response = self.session.get(url=self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, 'lxml')

    def product_title(self):
        title = self.soup.select_one('#productTitle')
        return title.text

    def product_price(self):
        
        price = self.soup.select_one('.a-price-whole')
        return price.text


url = "https://www.amazon.in/dp/B0DW478NDF/"
device = PriceTracer(url=url)
print("Title:", device.product_title())
print("Price:", device.product_price())