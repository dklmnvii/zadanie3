class Product:
    def __init__(self):
        self.name = None
        self.price = None
        self.category = None

    def __str__(self):
        return f"Продукт: {self.name}, Цена: {self.price}, Категория: {self.category}"

class ProductBuilder:
    def __init__(self):
        self.product = Product()

    def set_name(self, name):
        self.product.name = name

    def set_price(self, price):
        self.product.price = price

    def set_category(self, category):
        self.product.category = category

    def get_product(self):
        return self.product

class Shop:
    def __init__(self, builder):
        self.builder = builder

    def build_product(self, name, price, category):
        self.builder.set_name(name)
        self.builder.set_price(price)
        self.builder.set_category(category)
        return self.builder.get_product()

def main():
    builder = ProductBuilder()
    shop = Shop(builder)

    product = shop.build_product("Телефон", 999, "Электроника")
    print(product)

if __name__ == '__main__':
    main()