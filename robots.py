class Robot:
    """This class allows user to create Robot instances

    Attributes:
    name (str): name of the Robot
    buildyear (str): year Robot was build
    """


    Three_Laws = (
        """A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
        """A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
        """A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
        )
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build_year = build_year
    
    def say_hi(self):
        if self.__name:
            print("Hi, I am ", self.__name)
        else:
            print("Hi I am a robot without name")
    
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by
    
    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " +  str(self.__build_year) +  ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " +  str(self.__build_year)


if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    y = Robot("Caliban", 1943)
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")        
