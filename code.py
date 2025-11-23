
class People:
    def __init__(self, profesion, name, age) -> None:
        self.profesion = profesion
        self.name = name
        self.age = age

    def __sub__(self, obj):
        if isinstance(obj, People):
            return f"Today {self.name} made smarter {obj.name}"
        elif isinstance(obj, int):
            self.age += obj
            return f"Today {self.name} have a birthday now he has {self.age}"
        return NotImplementedError
    
    def __gt__(self, obj):
        if isinstance(obj, People):
            if self.age > obj.age:
                return f"Старшим є {self.name}"
            return f"{self.name} не є старшим за {obj.name}"
        return NotImplementedError

    def __len__(self) -> int:
        print("Ми зайшли в метон len, та знаходимо довжину Імені тваринки")
        return len(self.name)
    

    def battle(person1, person2):
     if len(person1.name) > len(person2.name):
        return f"{person1.name} win bcs longer name"
     else:
        return f"{person2.name} win bcs shorter name"
            
        

first = People("Teacher", "Andriy", 23)
second = People("Student", "Pavlo", 17)
third = People("Principal", "Volodimr", 45)
print(first - second)
print(first - 1)
print(first - float(1))

print(first.battle(second))

print(f"{third.name}! You are back, nice to meet you")
print(f"and also")
print(third - first)











