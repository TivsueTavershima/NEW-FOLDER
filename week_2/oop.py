# class vehicle():
#   def __init__(self,name,age,marital):
#     self.name = name
#     self.age = age
#     self.marital = marital
    
    
# pro = vehicle("taver",20,"single")
# print(f"my name is {pro.name} and i am {pro.age} yrs old and i am {pro.marital}.")


# class Calculator:
#   def ad(self, a, b):
#     return a + b

#   def mult(self, a, b):
#     return a * b

# calc = Calculator()
# print(calc.ad(5, 3))
# print(calc.mult(4, 7))


# class Vehicle():
#   def __init__(self,make,model):
#     self.make =make
#     self.model=model
    
  

    
#   def moves(self):
#     print("moves along...")
    
#   def get_make_model(self):
#     print(f"i'm {self.make} {self.model}.")
    
# my_car = Vehicle("tesla", "model 3")

# print(my_car.make)
# print(my_car.model)
# my_car.get_make_model()
# my_car.moves()


# class golfcart(Vehicle):
#     pass
# your_car = Vehicle("cadillac", "escalate")
# your_car.get_make_model()
# your_car.moves()

# class Airplane(Vehicle):
#   def __init__(self,make,model):
#     self.make =make
#     self.model=model
    
#   def moves(self):
#     print()
    
# class truck(Vehicle):
#   def moves(self):
#    print()
   
# class golfcart(Vehicle):
#  pass

# cessna = Airplane('cessna', 'skyhawk')
# mack = truck('mack', 'pinnacle')
# golfwagon = golfcart('yamaha', 'gc100')

# cessna.get_make_model()
# cessna.moves()
# mack.get_make_model()
# mack.moves()
# golfwagon.get_make_model()
# golfwagon.moves()

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)
