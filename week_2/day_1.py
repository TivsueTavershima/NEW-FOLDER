class MyClass():
  def __init__(self,age,name):
     self.age = age
     self.name = name
  
property = MyClass(36,"tavershima")
print(property.age)
print(property.name)


class MyClass():
  pass
  
property = MyClass()
property.age = 39
property.name = "tavershima"
  
print(property.age)
print(property.name)

   
class person():
  def __init__(self,name,age):
    
    self.name = name
    self.age = age
    
  def new(self):
    
   print(f"my name is {self.name} and my age is {self.age}")
    
property = person("Tavershima",28)
property.new()
print(property)

class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.name)
print(p1.name)


class calculate():
  def add(self,a,b):
    return a + b
  
cal = calculate()
print(cal.add(10, 8))


class multiplication():
  def multiply(self,a, b):
    return a * b
  
mul = multiplication()
print(mul.multiply(100,3))

class multiplication():
  def multiply(self,a, b):
    return a * b
  
cal = multiplication()
print(cal.multiply(20, 20))


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday, Taver! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()
p1.celebrate_birthday()