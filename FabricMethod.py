from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def get_name(self):
        pass

class Phone(Product):
    def get_name(self):
        return "Телефон"

class Laptop(Product):
    def get_name(self):
        return "Ноутбук"

class ProductCreator(ABC):
    @abstractmethod
    def create_product(self):
        pass

    def get_product(self):
        product = self.create_product()
        return product.get_name()

class PhoneCreator(ProductCreator):
    def create_product(self):
        return Phone()

class LaptopCreator(ProductCreator):
    def create_product(self):
        return Laptop()

# Пример использования
def main():
    phone_creator = PhoneCreator()
    phone = phone_creator.get_product()
    print(f"Продукт: {phone}")

    laptop_creator = LaptopCreator()
    laptop = laptop_creator.get_product()
    print(f"Продукт: {laptop}")

if __name__ == '__main__':
    main()