from sqlalchemy import *
from sqlalchemy.orm import *
from model import Product, ProductBase
from sqlmodel import SQLModel
from logger import Logger

class ORM:
    def __init__(self):
        self.engine = create_engine("sqlite:///data.db")
        self.log = Logger(True, "log.txt")
        SQLModel.metadata.create_all(self.engine)
        self.log.save_log(f"Инициализация БД")
    def add_product(self, product: ProductBase):
        with Session(autoflush=True,bind=self.engine) as db:
            self.log.save_log(f"Добавления товара")
            product_db = Product.model_validate(product)
            db.add(product_db)
            db.commit()
    def add_product_all(self, products: list[ProductBase]):
        with Session(autoflush=True,bind=self.engine) as db:
            self.log.save_log(f"Добавления товаров")
            products_db = [Product.model_validate(product) for product in products]
            db.add_all(products_db)
            db.commit()
    
