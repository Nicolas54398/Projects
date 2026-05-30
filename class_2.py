class Parrot:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        self.song = song

blu = Parrot("Blu", 10)
print(blu.sing("'Happy'"))