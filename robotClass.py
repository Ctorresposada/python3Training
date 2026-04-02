class robot:
    def __init__(self, name):
        self.name= name
        self.position = [0,0]
        print('My name is: ', self.name)
    def walk(self,x):
        self.position[0]= self.position[0] + x
        print('New position: ', self.position)

class Robot_Dog(robot):
    def make_noise(self):
        print('Woof Woof!')

class Robot_Michi(robot):
     def make_noise(self):
        print('Miau Miau!')

def main():
    my_dog_robot = Robot_Dog('Manchas')
    my_dog_robot.make_noise()
    my_dog_robot.walk(3)
    my_cat_robot = Robot_Michi('Pancha')
    my_cat_robot.make_noise()
    my_cat_robot.walk(7)
main()