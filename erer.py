class Person:
    def __init__(self, name):
        self.name = name    
        self.age = 1        

    def display_info(self):
        print(f"Имя: {self.name}\tВозраст: {self.age}")


petr = Person("Петр")
petr.name = "Катя"       
petr.age = -129          
petr.display_info()

##2
class Person:
    def __init__(self, name):
        self.__name = name  
        self.__age = 1  

    def set_age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


petr = Person("Петр")
petr.display_info()
petr.set_age(-3486)  
petr.set_age(25)
petr.display_info()

##3
def set_age(self, age):
    if 1 < age < 110:
        self.__age = age
    else:
        print("Недопустимый возраст")

class Person:
    def __init__(self, name):
        self.__name = name  
        self.__age = 1  

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 1 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print(f"Имя: {self.__name}\tВозраст: {self.__age}")


petr = Person("Петр")

petr.display_info()
petr.age = -3486  
print(petr.age)
petr.age = 36
petr.display_info()
