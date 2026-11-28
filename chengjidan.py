import sys
lines = []
from PIL import Image, ImageDraw, ImageFont
FONT = "C:/windows/Fonts/msyh.ttc"
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

try:
    students = []
    with open("students.txt", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split()
            name = parts[0]
            scores = []
            for p in parts[1:]:
                scores.append(int(p))
            students.append(Student(name, scores))
except FileNotFoundError:
    print("找不到 students.txt，请确认它和 chengjidan.py 在同一个文件夹")
    sys.exit()
except ValueError:
    print("students.txt 里有不是数字的内容，请检查分数那一列")
    sys.exit()
except UnicodeDecodeError:
    print("students.txt 的编码不是 UTF-8，请用 VS Code 另存为 UTF-8")
    sys.exit()

if len(students) == 0:
    print("students.txt 里没有读到任何学生，请检查文件内容")
    sys.exit()

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

    student.rank = rank
    student.status = status
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

n = len(students)
W, H = 640, 480 + n * 36
img = Image.new("RGB", (W, H), "white")
draw = ImageDraw.Draw(img)

font_title = ImageFont.truetype(FONT, 32)
font_body = ImageFont.truetype(FONT, 24)

draw.text((40, 24), "高一（3）班 周测成绩单", font=font_title, fill="black")

draw.text((40, 100), "姓名", font=font_body, fill="black")
draw.text((160, 100), "平均分", font=font_body, fill="black")
draw.text((280, 100), "名次", font=font_body, fill="black")
draw.text((400, 100), "状态", font=font_body, fill="black")

draw.line((40, 168 + n * 36, 600, 168 + n * 36), fill="black", width=2)

y = 192 + n * 36
for student in students:
    draw.text((40, y), student.name, font=font_body, fill="black")
    draw.text((160, y), f"{student.average()}", font=font_body, fill="black")
    draw.text((280, y), f"{student.rank}", font=font_body, fill="black")
    draw.text((400, y), student.status, font=font_body, fill="black")
    y = y + 36

draw.line((40, 276, 600, 276), fill="black", width=2)

stats = [
    f"班级平均分：{total/len(students)}",
    f"最高分：{best.name} {best.average()}",
    f"最低分：{worst.name} {worst.average()}",
    f"及格人数：{pass_count}/{len(students)}",
    f"及格率：{round(rate,1)}%",
]

y = 300
for stat in stats:
    draw.text((40, y), stat, font=font_body, fill="black")
    y = y + 36

img.save("chengjidan.png")
print("图片已保存：chengjidan.png")

