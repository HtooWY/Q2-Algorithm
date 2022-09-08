from Node import Node
import re


class BinaryTree:
    def __init__(self, input_string):
        self.input_string = input_string
        self.input_string_list = self.inorder()
        self.root = None

    @staticmethod
    def validateString(input_string):
        input_string = input_string.replace(" ", "")
        flag = 0
        if input_string.count(')') == input_string.count('('):
            flag += 1

        return True

    def constructTree(self):
        left = False
        right = False
        root = False
        rootnode = None
        leftnode = None
        rightnode = None

        while self.input_string_list:
            n = self.input_string_list.pop()
            if n == ")":
                rootnode.insert(leftnode)
                rootnode.insert(rightnode)
                break
            # Inorder - Check the left node first
            if left == False and root == False:
                if n == '(':
                    leftnode = self.constructTree()
                else:
                    leftnode = Node(n)
                left = True
            # Inorder - Check the root node
            elif root == False:
                rootnode = Node(n)
                root = True
            # Inorder - Check the right node last
            elif right == False:
                if n == '(':
                    rightnode = self.constructTree()
                else:
                    rightnode = Node(n)
                right = True
        rootnode.insert(leftnode)
        rootnode.insert(rightnode)

        return rootnode

    def inorder(self):
        input_string = self.input_string.replace(" ", "")
        result = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', input_string)
        # Reverse the list for stack
        return result[::-1]

    def preorder(self):
        return

    def postorder(self):
        return
