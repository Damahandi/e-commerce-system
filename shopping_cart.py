# shopping_cart.py
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def calculate_total(self):
        return sum(item.price for item in self.items)
