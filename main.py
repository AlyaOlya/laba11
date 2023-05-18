def  z1():
    class Restorant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название Ресторана {self.restaurant_name}, кухня: {self.cuisine_type} .")
        def open_restaurant(self):
            print("Ресторан сейчас открыт.")
    newRestoraunt = Restorant(" В Гостях у Удмуртки Ксюши ", "итальянская ")
    print(newRestoraunt.restaurant_name)
    print(newRestoraunt.cuisine_type)
    newRestoraunt.describe_restaurant()
    newRestoraunt.open_restaurant()
def  z2():
    class Restorant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
        def describe_restaurant(self):
            print(f"Название Ресторана {self.restaurant_name}, кухня: {self.cuisine_type} ")
        def open_restaurant(self):
            print("Ресторан сейчас открыт.")
    imya = input("Введите название ресторана: ")
    kyxnya = input("Введите кухню:")
    newRestoraunt = Restorant(imya, kyxnya)
    print(newRestoraunt.restaurant_name)
    print(newRestoraunt.cuisine_type)
    newRestoraunt.describe_restaurant()
    newRestoraunt.open_restaurant()
    imya = input("Введите название ресторана: ")
    kyxnya = input("Введите кухню:")
    newRestoraunt2 = Restorant(imya, kyxnya)
    print(newRestoraunt2.restaurant_name)
    print(newRestoraunt2.cuisine_type)
    newRestoraunt2.describe_restaurant()
    newRestoraunt2.open_restaurant()
    imya = input("Введите название ресторана: ")
    kyxnya = input("Введите кухню:")
    newRestoraunt3 = Restorant(imya, kyxnya)
    print(newRestoraunt3.restaurant_name)
    print(newRestoraunt3.cuisine_type)
    newRestoraunt3.describe_restaurant()
    newRestoraunt3.open_restaurant()
def z3():
    class Restorant:
        def __init__(self, restaurant_name, cuisine_type, reiting_res):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting_res = reiting_res
    newRestoraunt = Restorant("В Гостях у Удмуртки Ксюши ", "итальянская", 5)
    print(newRestoraunt.restaurant_name)
    print(newRestoraunt.cuisine_type)
    print(newRestoraunt.reiting_res)
    newRestoraunt.reiting_res = input("Новый рейтинг: ")
    print(newRestoraunt.restaurant_name)
    print(newRestoraunt.cuisine_type)
    print(newRestoraunt.reiting_res)
z1()
z2()
z3()