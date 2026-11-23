
import requests
from bs4 import BeautifulSoup
from model import Product, ProductBase
from logger import Logger



class Parse:
    def __init__(self, url:str):
        self.url = url
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text,"html.parser")
        self.data = None
        self.arr = []
        self.log = Logger(True, "log.txt")
    def get_products(self):
        links = self.soup.select("ul.pagination a")
        #ищет внутри тега ul с классом pagination все теги a
        last_page = int(links[-2].text.strip())
        self.data = []
        for page in range(1,last_page+1):
            self.log.save_log(f"Парсинг страницы {page}")
            self.response = requests.get(self.url+f"?page={page}")
            self.soup = BeautifulSoup(self.response.text,"html.parser")
            titles = self.soup.find_all("p", class_="b1c-name")
            prices = self.soup.find_all("div",class_="price")
            for i in range(len(titles)):
                title = titles[i].text
                price = prices[i].span.text 
                price = int(price.replace(" ","").replace("\xa0",""))
                self.arr.append(ProductBase(title=title,price=price))
        return self.arr

