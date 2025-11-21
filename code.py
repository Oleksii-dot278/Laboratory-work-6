
class people:
    def __init__(self, people, name, age, mass = None) -> None:
        print(f"This is a {people} which names {name} which has a {age} years")
        self.people = people
        self.name = name
        self.age = age
        self.mass = 0 if mass==None else mass
    
    def speak(self):
        if self.people == "Teacher":
            return f"  {self.people} is talking about lesson"
        elif self.people == "Principal":
            return f"This {self.people} very important at college"
        else:
            return f"This {self.people} is fired :)"
    
    def add_one_year(self):
        self.age += 1
        return f"This {self.people} made me smarter for 1 year"

first = people("Teacher", "Andriy", 23, 79)
second = people("Student", "Pavlo", 17, 67)
third = people(people="Principal", name="Volodimr", age=45, mass=81)

print(f"This {first.people}:", first.speak())

print(f"This {third.people}:", third.speak())


print(f"{first.people} has {first.age} years")
print(first.add_one_year())
print(f"{first.people} now has {first.age} years")

print(f"This {second.people} which names {second.name} has problem with a {first.name} and now they will go to a {third.people} to solve a problem")

print(f"{second.name} is a {second.age} years old")
print(f"{first.name} is a {first.age} years old")
print(f"{third.name} is a {third.age} years old")
print(f"{third.name}is the oldest, and {second.name} is the youngest")