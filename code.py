class People:
    total_csv = int(0)
    total_objects = int(0)
    def __init__(self, profesion, name, age) -> None:
        self.profesion = profesion
        self.name = name
        self.age = age
        People.total_objects += 1

    @classmethod
    def from_csv(cls, csv_data:str):
        cls.total_csv += 1
        profesion, name, age = csv_data.split(",")
        return cls(profesion, name, age)
    
    def is_name_capitalized(self):
        return self.name[0].isupper()


first = People.from_csv("Teacher,Andriy,23")
second = People("Student", "pavlo", 17)

print(f"{first.name}, if this name capitalized? {first.is_name_capitalized()}")
print(f"{second.name} if this name Capitalized? {second.is_name_capitalized()}")







