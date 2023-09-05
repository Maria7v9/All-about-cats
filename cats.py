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

for cat in cats:
    if cat.wght >4:
        cat.appease()
        break
            