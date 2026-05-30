class Parrot:
    type = "toybird"
    def __init__(self, name, age):
        self.name = name
        self.age = age

blu = Parrot("Blu", 10)
print(blu.age)
print(blu.name)
print(blu.type)