from Node import Node
import re

class BinaryTree:
    def __init__(self, input_string):
        self.input_string = input_string
        self.input_string_list = self.inorder()
        self.root = None

    @staticmethod
    def validateString(input_string):
        regexp = re.compile(r'[A-Za-z!$&,:;=?@#|\'<>.^%!][^d+|\+|\-|\*|\/|\(|\)]')
        if regexp.search(input_string):
            return False
        return True

    def constructTree(self):
        left = False
        right = False
        root = False
        root_node = None
        left_node = None
        right_node = None

        while self.input_string_list:
            n = self.input_string_list.pop()
            if root and right:
                if not left_node:
                    self.input_string_list.append(n)
                break
            # Inorder - Check the left node first
            if not left and not root:
                if n == '(':
                    left_node = self.constructTree()
                elif n == 'NEG':
                    n = self.input_string_list.pop()
                    root_node = Node(n)
                    root = True
                    continue
                elif n == '-':
                    self.input_string_list.append(n)
                    self.input_string_list.append("NEG")
                    left_node = self.constructTree()

                else:
                    left_node = Node(n)
                left = True
            # Inorder - Check the root node
            elif not root:
                root_node = Node(n)
                root = True
            # Inorder - Check the right node last
            elif not right:
                if n == '(':
                    right_node = self.constructTree()
                elif n == '-':
                    self.input_string_list.append(n)
                    self.input_string_list.append("NEG")
                    right_node = self.constructTree()
                else:
                    right_node = Node(n)
                right = True

        root_node.insertLeft(left_node)
        root_node.insertRight(right_node)
        return root_node


    def inorder(self):
        result = re.findall(r'\d+|\+|\-|\*|\/|\(|\)', self.input_string)
        # Reverse the list for stack
        return result[::-1]

    def setNewBinaryTree(self, input_string):
        self.input_string = input_string
        self.input_string_list = self.inorder()