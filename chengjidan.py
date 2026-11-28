lines = []
PASS_LINE = 60
class Student():
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for s in self.scores:
            total = total + s
        return total/len(self.scores)

students = []
with open("students.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        name = parts[0]
        scores = []
        for p in parts[1:]:
            scores.append(int(p))
        students.append(Student(name, scores))

lines.append("姓名\t平均分\t名次\t状态")
for student in students:
    avg = student.average()

    rank = 1
    for other in students:
        if other.average() > avg:
            rank = rank + 1

    if avg >= PASS_LINE:
        status = "及格"
    else:
        status = "不及格"

    lines.append(f"{student.name}\t{avg}\t{rank}\t{status}")

total = 0
for student in students:
    total = total + student.average()
lines.append(f"班级平均分:{total/len(students)}")

best = students[0]
worst = students[0]
for student in students:
    if student.average() > best.average():
        best = student
    if student.average() < worst.average():
        worst = student
lines.append(f"最高分:{best.name} {best.average()}")
lines.append(f"最低分:{worst.name} {worst.average()}")

pass_count = 0
for student in students:
    if student.average() >= PASS_LINE:
        pass_count = pass_count + 1
lines.append(f"及格人数:{pass_count}/{len(students)}")

rate = pass_count/len(students)*100
lines.append(f"及格率:{round(rate,1)}%")

for line in lines:
    print(line)

with open("chengjidan.txt", "w", encoding="utf-8") as f:
    for line in lines:
        f.write(line + "\n")