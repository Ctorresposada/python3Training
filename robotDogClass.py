class Robot_Dog:
    def __init__(self,name_value,breed_value):
        self.name=name_value
        self.breed=breed_value
    def bark(self):
        print("Woof Woof!")



#Main
mydog = Robot_Dog('Manchitas','Maltipoo')
print(mydog.name)
print(mydog.breed)
mydog.bark()
