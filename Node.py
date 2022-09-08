operator = ["+", "-", "*", "/"]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.value = None

    def inorder(self):
        if self.left is not None:
            self.left.inorder()
        print(self.data)
        if self.right is not None:
            self.right.inorder()

    def insert(self, node):
        if self.left is None:
            self.left = node
        elif self.right is None:
            self.right = node

    def printTree(self, level=0, arrow='->'):
        if self:
            if self.right:
                self.right.printTree(level + 1, ' /‾‾‾')
            print(' ' * 4 * level + arrow + '['+ self.data+']')
            if self.left:
                self.left.printTree(level + 1, ' \\___')


    def height(self):
        if not self:
            return -1
        leftHeight = -1 if not self.left else self.left.height()
        rightHeight = -1 if not self.right else  self.right.height()
        return max(leftHeight, rightHeight) + 1

    def maxWidth(self):
        maxWidth = 0
        height = self.height()


    def calculate(self):
        if self.data not in operator and not self.left and not self.right:
            return self.data
        # switch = {
        #     '+': self.add(),
        #     '-': self.subs(),
        #     '*': self.prod(),
        #     '/': self.div()
        # }
        # return switch.get(self.data, 0)
        if self.data==operator[0]:
            return self.add()
        elif self.data == operator[1]:
            return self.subs()
        elif self.data == operator[2]:
            return  self.prod()
        elif self.data == operator[3]:
            return self.div()

    def add(self):

        leftvalue = 0 if not self.left else self.left.calculate()
        rightvalue = 0 if not self.right else self.right.calculate()
        print("add")
        print(leftvalue)
        print(rightvalue)
        print("\n")
        return int(leftvalue) + int(rightvalue)

    def subs(self):

        leftvalue = 0 if not self.left else self.left.calculate()
        rightvalue = 0 if not self.right else self.right.calculate()
        print("subs")
        print(leftvalue)
        print(rightvalue)
        print("\n")
        return int(leftvalue) - int(rightvalue)

    def prod(self):

        leftvalue = 0 if not self.left else self.left.calculate()
        rightvalue = 0 if not self.right else self.right.calculate()
        print("prod")
        print(leftvalue)
        print(rightvalue)
        print("\n")
        return int(leftvalue) * int(rightvalue)

    def div(self):

        leftvalue = 0 if not self.left else self.left.calculate()
        rightvalue = 0 if not self.right else self.right.calculate()
        print("div")
        print(leftvalue)
        print(rightvalue)
        print("\n")
        return int(leftvalue) / int(rightvalue)