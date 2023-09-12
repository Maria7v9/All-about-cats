class Cat():
    def __init__(self, name: str, wght: float, paws: int, wild: bool):
        self.name = name
        self.wght = wght
        self.paws = paws
        self.wild = wild

    def ground_press(self):
        press = self.wght/self.paws
        print("Кошка давит на грунт", press)
        return press

    def angry(self):
        self.wild = True
        print( 'Кошенька', self.name,'злобная!', 'Дикость = ',self.wild)
        return self.wild

    def appease(self):
        self.wild = False
        print('Кошенька', self.name,'добренькая!', 'Дикость = ',self.wild)
        return self.wild

trisha = Cat('Trisha', 1.35, 4, False)
trisha.ground_press()
trisha.angry()
trisha.appease()
cats = [
    Cat('Trisha', 1.35, 4, False),
    Cat('Miusya', 6, 4, False),
    Cat('Tom', 8, 4, False),
    Cat('Batsik', 7.5, 4, False),
    Cat('Murka', 4.5, 3, False),
    Cat('Ryisa', 2.4, 4, False),
    Cat('Botya', 7.3, 4, False),
    Cat('Misa', 5, 2, False),
    Cat('Nosok', 8.2, 4, False),
    Cat('Sapog', 4.7, 4, False)
]
for cat in cats:
    cat.angry()

#for cat in cats:
#    if cat.wght >4:
#        cat.appease()
#        break

i = 0

while i< len(cats):
    if cats[i].wght > 4:
        cats[i].appease()
        break
    i +=1

class CatHouse():
    def __init__(self, cat):
        self.label = cat.name
        self.size = 'small' if cat.wght < 3 else 'big'

    def check_floor_is_strong_enough(self):
        return True if cat.ground_press() < 0.8 else False

cat2 = Cat("Barsik", 2.5, 4, False)
house1 = CatHouse(cat2)
print(house1.label)
print(f"{house1.size} кошка живет в домике под именем {house1.label}")
print(house1.check_floor_is_strong_enough())

cat_houses = []
for cat in cats:
    cat_houses.append(CatHouse(cat))
for cat_house in cat_houses:
    print(f"{cat_house.size} кошка живет в домике под именем {cat_house.label}")
