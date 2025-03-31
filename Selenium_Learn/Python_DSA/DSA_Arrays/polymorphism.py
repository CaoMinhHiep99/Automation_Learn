class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "DogDog!"

class Cat(Animal):
    def speak(self):
        return "MeoMeo!"

class Cow(Animal):
    def speak(self):
        return "CowCow!"

def animal_sound(animal: Animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
cow = Cow()

animal_sound(dog)
animal_sound(cat)
animal_sound(cow)
