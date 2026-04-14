from dataclasses import dataclass

@dataclass
class Prodotti:
    Product_number: int
    Product_line: str
    Product_type : str
    Product: str
    Product_brand: str
    Product_color: str
    Unit_cost: str
    Unit_price: str

    def __hash__(self):
        return hash(self.Product_number)

    def __eq__(self, other):
        return self.Product_number == other.Product_number

    def __str__(self):
        return f"{self.Product_number} - {self.Product}: {self.Product_brand}, {self.Unit_price}"
