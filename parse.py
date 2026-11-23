
import requests
from bs4 import BeautifulSoup

class Parse:
    def __init__(self, url:str):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text,"html.parser")
        self.data = None
    def get_products(self):
        links = self.soup.select("ul.pagination a")
        #ищет внутри тега ul с классом pagination все теги a
        last_page = int(links[-2].text.strip())
        self.data = []
        for page in range(1,last_page+1):
            self.response = requests.get(self.url+f"?page={page}")
            self.soup = BeautifulSoup(self.response.text,"html.parser")
            titles = self.soup.find_all("p", class_="b1c-name")
            prices = self.soup.find_all("input",class_="btn gradient-base-darkblue btn-sm product-block_cart_btn")
            

p = Parse("https://killprice24.ru/catalog/smartfony")
p.get_products()