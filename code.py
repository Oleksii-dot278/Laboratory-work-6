from datetime import datetime
class People:
    max_studing = 4
    def __init__(self, profesion, name, age) -> None:
        self.profesion = profesion
        self.name = name
        self.age = age
    
    @property
    def live_untill(self):
        return datetime.today().year - self.age + self.max_studing
    
    @property
    def is_adult(self):
        return self.age >= 18
    
    def add_one_year(self):
        self.age += 1
        return f"{self.profesion} studing for 1 year"


first = People("Teacher", "Andriy", 23)
second = People("Student", "Pavlo", 17)

print(f"This {first.profesion} will work until {first.live_untill} year")
print(f"Is {first.name} an adult? {first.is_adult}")

print(f"This {second.profesion} will study until {second.live_untill} year")
print(f"Is {second.name} an adult? {second.is_adult}")






