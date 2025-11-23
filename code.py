class People:
    def __init__(self, profesion, name, age) -> None:
        self.profesion = profesion
        self.name = name
        self.age = age
        self._secret_phrase = "private atribute"
        self.__secret_strong = "    You can't call it from outside"
    
    @property
    def secret_phrase(self):
        return f"We got this from property: {self._secret_phrase}"
    
    @property
    def secret_strong(self):
        return f"We got it from properties: {self.__secret_strong}"

    def _secret_methid(self):
        return "private metod, don't touch him"

    def __do_not_touch_it(self):
        return "Can't call from outside"
    


first = People("Principal", "oksana", 43)
second = People("Teacher", "Andriy", 23)

first._secret_phrase = "Changed private atribute"  


print(second._secret_phrase)

print(second._People__secret_strong)









