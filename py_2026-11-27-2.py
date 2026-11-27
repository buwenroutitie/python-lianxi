total = 0
scores = [78, 92, 65, 88]
for score in scores:
    total = total + score
ave = total/len(scores)
print(f"总分:{total}\n平均分:{ave}")