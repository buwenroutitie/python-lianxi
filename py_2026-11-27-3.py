def average(scores):
    total = 0
    for score in scores:
        total = total + score
    return total/len(scores)
print(average([78, 92, 65, 88]))
print(average([100, 50]))