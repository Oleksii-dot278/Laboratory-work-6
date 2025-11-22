class People:
    def __init__(self, profesion, name, age) -> None:
        self.profesion = profesion
        self.name = name
        self.age = age
    
    def add_one_year(self):
        self.age += 1
        return f" This {self.profesion} has exiriense 1 year"

    @staticmethod
    def call_people():
        return "Helpers"


first = People("Teacher", "Andriy", 23)
second = People("Student", "Pavlo", 17)
third =  People("Principal", "Oksana", 43)


print(f"Hello {third.name}, and you are a {third.profesion}, if you need a help, you can call {first.call_people()}, or use class metode {People.call_people()} and also, don't forget about {first.name}, he is a profesional {first.profesion}")

print(f"Hello {second.name}, and this is your first day at college, your {first.profesion} is {first.name} be patient and calm")




