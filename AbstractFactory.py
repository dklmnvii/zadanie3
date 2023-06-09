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

class AbstractFactory(ABC):
    @abstractmethod
    def create_product(self):
        pass

class PhoneFactory(AbstractFactory):
    def create_product(self):
        return Phone()

class LaptopFactory(AbstractFactory):
    def create_product(self):
        return Laptop()

def main():
    phone_factory = PhoneFactory()
    phone = phone_factory.create_product()
    print(f"Продукт: {phone.get_name()}")

    laptop_factory = LaptopFactory()
    laptop = laptop_factory.create_product()
    print(f"Продукт: {laptop.get_name()}")

if __name__ == '__main__':
    main()
 