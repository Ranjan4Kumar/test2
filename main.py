''' Q1 --> what is OOPs concept, why we use it?'''
''' Ans:--> The oops concept focuses on writing the reusable code. It is a most used technique to solve the problem by creating objects.
use OOP in their Python programs because it makes code more reusable and makes it easier to work with larger programs. 
OOP programs prevent you from repeating code because a class can be defined once and reused many times.'''





'''Q2--> Define constructor with syntax'''
'''Ans--> constructors is to assign values to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor'''



'''Q4--> Define inheritance, its types and write syntax for single in heritance?'''

''' Ans--> inheritance allow us to define a class that inherits all the properties of parent class to child class,
there are generally 2 types of inheritance
1. single inheritance
2. multilevel inheritance'''
# Syntax for single inheritance
class school:
  def __init__(self, name):
     self.name = name

  def say_hi(self):
    print("{} is new student".format(self.name), end = " ")

class student(school):
  def __init__(self,name,std):
    school.__init__(self, name)
    self.std = std

  def say_hi(self):
    school.say_hi(self)
    print("studying in class 5th standard {}".format(self.std))





''' Q5-->  Find the error in the code and explain the error'''

class Toy:
  def __init__(self):
    self.a = 123
    self._b = 125
    self.__c = 130

new_toy = Toy()
print(new_toy.a)# public objetc
print(new_toy._b) # private variable by convention but not variable
print(new_toy.__c) # python enforced private variable, access throw error



'''Q-->6 Explain Encapsulation and explain functionality of getter & setter method '''

'''Ans--> Encapsulation puts restrication on accessing the variable & methods directly and prevent
the accidental modification of data
getter():- Getter method is used to read the private data present in the file
setter():- setter method is used for updating/modifying the private data and
we check the modified data using getter method'''



'''Q7--> Name the module which we use to access the Abstract class inside python & write syntax for 
importing abstract method & module'''

'''Ans--> abc module is used to access the abstrcat mehtod in python'''
# Syntax
from abc import ABC, abstractmethod
# use
class polygon:
  @abstractmethod
  def noofsides(self):
    pass





'''Q9--> Define interface and write syntax for formal interface

ans--> Implementing an interface is a way of writing an organized code and achieve abstraction
It is abstract classes but allows child classes to implement multiplr classes
an interface is a set of publically accessible methods on an object which
can be used by other parts of the program to interact with that object'''

# Syntax
from abc import ABC, abstractmethod
class Bird(ABC): 
  abstractmethod 
  def fly(self):
    pass


class Parrot(Bird):
  def fly(self):
    print('flying')
p = Parrot()

class Aeroplane(ABC):
  abstractmethod 
  def fly(self):
    pass
class Boeing(Aeroplane): 
  def fly(self):
    print("Flying!") 
b = Boeing()