from dataclasses import dataclass
from datetime import date


@dataclass
class Vendite:
    Retailer_code: int
    Product_number: int
    Order_method_code: int
    Date: date
    Quantity: int
    Unit_price: float
    Unit_sale_price: float

    def __hash__(self):
        return hash((self.Retailer_code, self.Product_number, self.Order_method_code))

    def __eq__(self, other):
        return (self.Retailer_code == other.retailer_code
                and self.Product_number == other.product_number
                and self.Order_method_code == other.order_method_code)

    def __str__(self):
        return f"{self.Retailer_code}, {self.Product_number}, {self.Order_method_code}"