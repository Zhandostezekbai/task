class Pet:
    def __init__(self, name, age):
        self._name = name
        self._salary  = age
        
    def get_name(self):
        return self._name
    def get_age(self):
        return self._age
    def set_name(self, name):
        self.new_name = name
    def set_age(self, age):
        self.new_age = age    

class Dog(Pet):
    def bark(self):
        print("гав гав")
        
    def make_sound(self):
        self.bark()
        
class Cat(Pet):
    def Meow(self):
        print("мяу мяу")
    def make_sound(self):
        self.Meow()

class Bird(Pet):
    def chirp(self):
        print("чик чик")
    def make_sound(self):
        self.chirp()
        
