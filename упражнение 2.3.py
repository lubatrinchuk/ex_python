class Animal:
    def __init__(self, name = "", age = 0):
        self.name = name
        self.age = age

class Zebra(Animal):
    def __init__(self, name = "", age = 0, info = ""):
        super().__init__(name, age)
        self.info = info
    def __str__(self):
        return "Информация о зебре по имени "+self.name+" :\n возраст: "+str(self.age)+"\n состояние: "+self.info

class Dolphin(Animal):
    def __init__(self, name="", age=0, info=""):
        super().__init__(name, age)
        self.info = info
    def __str__(self):
        return "Информация о дельфине по имени " + self.name + " :\n возраст: " + str(self.age) + "\n состояние: " + self.info

a = Zebra("Polly", 4, "больна")
print(a)
b = Dolphin("Игорь", 1, "здоров")
print(b)