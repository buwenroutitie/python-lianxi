scores = [100, 80, 83, 38, 38]
total = 0
for i in scores:
    total = total + i
avg = total/len(scores)
if avg >= 80:
    print(f"优秀，平均分为{avg}")
else:
    print(f"及格，平均分为{avg}")