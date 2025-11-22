class Subject:
    total_subjects = 0
    total_types = set()

    def __init__(self, name, difficult, time):
        self.name = name
        self.difficult = difficult
        self.time = time
        Subject.total_subjects += 1
        Subject.total_types.add(name)


data = [("math", 4, 15), ("chemistry", 3, 13), ("physics", 4, 14)]


subjects_list = []
for name, difficult, time in data:
    obj = Subject(name, difficult, time)
    subjects_list.append(obj)


print(f"Counter of subjects: {Subject.total_subjects}")
print(f"Their type: {Subject.total_types}")






