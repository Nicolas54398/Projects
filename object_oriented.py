class Person:

    # class attribute
    species = "Human"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Human Class
Tom = Person("Tom", 18)

# access the class attributes
print("Tom is a {}".format(Person.species))

# access the instance attributes
print("{} is {} years old".format( Tom.name, Tom.age))


