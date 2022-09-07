operation = ["+", "-", "*", "/"]


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.value = self.calculateValue()

    def calculateValue(self):
        if self.data not in operation and self.left == null and self.right == null:
            return self.data
        switch = {
            '+': self.add(),
            '-': self.subs(),
            '*': self.prod(),
            '/': self.div()
        }
        return switch.get(self.data, 0)

    def add(self):
        return self.left.value + self.right.value

    def subs(self):
        return self.left.value - self.right.value

    def prod(self):
        return self.left.value * self.right.value

    def div(self):
        return self.left.value / self.right.value
