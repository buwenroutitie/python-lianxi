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
    Student("李四", [50, 62, 53]),
    Student("王五", [90, 93, 96]),
]

print("姓名\t平均分\t名次\t状态")
for student in students:
    avg = student.average()

    rank = 1
    for other in students:
        if other.average() > avg:
            rank = rank + 1

    if avg >= 60:
        status = "及格"
    else:
        status = "不及格"

    print(f"{student.name}\t{avg}\t{rank}\t{status}")

total = 0
for student in students:
    total = total + student.average()
print(f"班级平均分:{total/len(students)}")

best = students[0]
worst = students[0]
for student in students:
    if student.average() > best.average():
        best = student
    if student.average() < worst.average():
        worst = student
print(f"最高分:{best.name} {best.average()}")
print(f"最低分:{worst.name} {worst.average()}")

pass_count = 0
for student in students:
    if student.average() >= 60:
        pass_count = pass_count + 1
print(f"及格人数:{pass_count}/{len(students)}")

rate = pass_count/len(students)*100
print(f"及格率:{round(rate,1)}%")