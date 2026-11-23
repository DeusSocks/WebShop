from parse import Parse
from orm import ORM

parse_data = Parse("https://killprice24.ru/products?keyword=xiaomi")
data = parse_data.get_products()
orm_obj = ORM()
orm_obj.add_product_all(data)