class Robot:
    __state = {}

    def __init__(self, name):
        self.__dict__ = self.__state
        self.name = name

    def __str__(self):
        return self.name


robot1 = Robot("Rob")
print(robot1.name)

robot2 = Robot("Paul")
print(robot1.name, robot2.name)

robot3 = Robot("Greg")
print(robot1.name, robot2.name, robot3.name)
