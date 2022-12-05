class Bottle:
    color = "Красная"
    value = 0.0


bottle_1 = Bottle()
bottle_2 = Bottle()
bottle_3 = Bottle()

setattr(bottle_1,'value', '0.7')
bottle_2.color = 'Белая'
bottle_2.value = 0.3
bottle_3.color = 'Черная'
bottle_3.value = 1.0




print(bottle_1.color, bottle_1.value)
print(bottle_2.color, bottle_2.value)
print(bottle_3.color, bottle_3.value)
# Красная 0.7
# Белая 0.3
# Черная 1.0