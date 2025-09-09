# Your code here
class seven:
    def __init__(self, n):
        self.n = n

    def generator(self):
        for i in range(0, self.n + 1):
            if i % 7 == 0:
                yield i

div = seven(50)
print(list(div.generator()))