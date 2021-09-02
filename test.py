from typing import List


print("Hello World2")

# x = 4
# x = "5"
# x = 3.5
# x = True
# x = False

# def x(x):
#     print(x)

# x(x)

# x = [1,"2",[3.0]]
# x.append(True)
# x += [False]

# print(x)

x = [1,2,3]
x = [4] + x

# i = 0
# while i < len(x):
#     print(x[i])
#     i+=1

# for i in range(len(x)):
#     print(x[i])

# for n in x:
#     print(n)

x = dict()
x = {
    "key":"value",
    "key2":"value2"
}
x["key3"]=3

# def z(a):
#     print(a)
# # print(x["key3"])

# y = (1,2)
# x[y]=True
# x[False]=z
# print(x)
# x[False](x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def set_age(self, age):
    self.age = age

  def __str__(self):
    return f"%s is %d old" % (self.name, self.age)

class Student(Person):
  def __init__(self, name, age, year):
    Person.__init__(self, name, age)
    self.year = year





x = Person("Bryan", 38)
x.set_age(29)
print(x)
print(x.name)