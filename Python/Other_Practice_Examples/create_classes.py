import turtle

class Dog():
    
    def __init__(self, name, woofs):
        self.name = name
        self.woofs = 0

    def count(self):
        self.woofs += 1
        for bark in range(self.woofs):
            self.speak()
        

    def speak(self):
        if self.name in command:
            self.speak()

class Chihuahua(Dog):
    
    def speak(self):
        print("Yip!")

class Husky(Dog):

        def speak(self):
            print("Awoo!")

class Daschund(Dog):

    def speak(self):
        print("Arr!")


class DogPark():

    def __init__(self, dogs):
        self.dogs = dogs

    def rollcall(self):
        print("Dogs in the Dog Park:")
        for dog in self.dogs:
            print(f"{dog.name}")

    def shout(self, command):
        for dog in self.dogs:
            dog.hear(command)
            
    def converse(self):
        command = input("PLease say a command: ")
        while True:
            if ("I quit" in command) or ("to quit" in command):
                print("Bye!")
                break
            else:
                self.shout(command)
                        

# class BlueTurle(turtle.Turtle):
    
#     def __init__(self):
#         super().__init__()
#         self.color("blue")

