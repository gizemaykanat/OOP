class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity):
        if product.update_stock(quantity):
            if product.name in self.items:
                self.items[product.name]['quantity'] += quantity
            else:
                self.items[product.name] = {'product': product, 'quantity': quantity}
        else:
            print(f"Yetersiz stok: {product.name}")

    def remove_product(self, product_name):
        if product_name in self.items:
            del self.items[product_name]

    def display_cart(self):
        for number, item in enumerate(self.items.values(), start=1):
            print(f"{number}. {item['product'].name} - {item['quantity']} adet - {item['product'].price * item['quantity']} TL")

    def get_total(self):
        return sum(item['product'].price * item['quantity'] for item in self.items.values())