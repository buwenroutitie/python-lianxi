class Student():
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for s in self.scores:
            total = total + s
        return total/len(self.scores)

students = [
    Student("张三", [78, 92, 65, 88]),
    Student("李四", [60, 70, 80]),
    Student("王五", [90, 93, 96]),
]

for student in students:
    print(student.name, student.average())

total = 0
for student in students:
    total = total + student.average()
print(total/len(students))

best = students[0]
for student in students:
    if student.average() > best.average():
        best = student
print(best.name, best.average())