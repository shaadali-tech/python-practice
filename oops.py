# class Car:
#   def __init__(self,age,name):
#     self.age=age
#     self.name=name

# car=Car(name="Shaad",age=25)
# print(car.name)
# print(car.age)


# git add .; git commit -m "Update project"; git push
#Inheritance

# class Car:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

#   def methods(self):
#     print(self.age)
#     print(self.name)

# class bmw(Car):
#   def move(self):
#     print("car is moving")

# cars=bmw("Bmw",2500)
# cars.move()
# cars.methods()

# ENCAPSULATION

class Student:

    def __init__(self):

        self.__marks = 95

    def display(self):

        print(self.__marks)


s = Student()

s.display()