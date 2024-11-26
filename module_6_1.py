class Animal: # зададим класс Животные
    def __init__(self, name):  # зададим метод для базовых парам.
        self.alive = True  # живой
        self.fed = False  # накормленный
        self.name = name  # индив. назв. животного


class Plant:  # зададим класс Растения
    def __init__(self, name):  # зададим метод для базовых парам.
        self.edible = False  # съедобность
        self.name = name  # индив. назв. растения

class Mammal(Animal):  # зададим класс Млекопитающее
    def eat(self, food):  # зададим метод для базовых парам.
        if food.edible:  # если растение съедобное то:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:  # иначе
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Predator(Animal):  # зададим класс Хищник
    def eat(self, food):  # зададим метод для базовых парам.
        if food.edible:  # если съедобное то:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:  # иначе
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Flower(Plant):  # зададим класс Цветы
    pass

class Fruit(Plant):  # зададим класс Фрукты
    def __init__(self, name):  # зададим метод для базовых парам.
        super().__init__(name) # передаем в класс Plant аргумент name
        self.edible = True  # переопределяем атрибут

# пример
a1 = Predator('Бандит, полицейский, дьявол')
a2 = Mammal('Мышь')
p1 = Flower('Цветок зла')
p2 = Fruit('Искрящийся арбуз')

print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)

# животные едят растения
a1.eat(p1)  # 'Бандит, полицейский, дьявол' не стал(и) есть 'Цветок зла'
a2.eat(p2)  # 'Мышь' съел 'Искрящийся арбуз'

print(a1.alive)
print(a2.fed)