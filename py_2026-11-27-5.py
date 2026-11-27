class Student():
    def __init__(self,name,scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for s in self.scores:
            total = total + s
        return total/len(self.scores)

    def highest(self):
        best = self.scores[0]
        for s in self.scores:
            if s > best:
                best = s
        return best
    
zhang = Student("张三", [78, 92, 65, 88])
print(zhang.name, zhang.average())
print(zhang.highest())