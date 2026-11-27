class Course():
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for s in self.scores:
            total = total + s
        return total/len(self.scores)

math = Course("数学", [90, 80, 70])
print(math.name, math.average())