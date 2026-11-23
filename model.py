from sqlmodel import SQLModel, Field

class ProductBase(SQLModel):
    title: str = Field(min_length=2, max_length=200)
    price: int = Field(gt=0)

class Product(ProductBase, table=True):
    id: int = Field(default=None, primary_key=True)