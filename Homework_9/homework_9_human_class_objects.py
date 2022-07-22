from homework_9_human_class import Human
from datetime import date

# class object's description
misha = Human('Misha', 'Pitterson', 'm', birth_date=date(2000, 1, 3))
print(misha)
misha.eat('cake')
misha.sleep(7)
misha.talk()
misha.walk()
misha.stand()
misha.lie()
print(Human.humans_population)

# uncomment 13 and 14 if you want to delete misha - Human's class object :'(
# del misha
# print(misha)

