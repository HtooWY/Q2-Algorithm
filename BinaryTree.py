from Node import Node
import re


class BinaryTree:
    def __init__(self, input_string):
        self.input_string = input_string
        # self.node = self.constructTree(0)

    @staticmethod
    def validateString(input_string):
        input_string = input_string.replace(" ", "")
        flag = 0
        if input_string.count(')') == input_string.count('('):
            flag += 1

        return True

    def inorder(self):
        self.input_string = self.input_string.replace(" ", "")
        result = re.findall(r'\d+|\+|\-|\*|\/', self.input_string)
        print(result)

    def preorder(self):
        return

    def postorder(self):
        return

    def constructTree(self, index):
        parenteses = 0

        preorder_index = 0

        # build a hashmap to store value -> its index relations
        inorder_index_map = {}
        for index, value in enumerate(inorder):
            inorder_index_map[value] = index

        return array_to_tree(0, len(preorder) - 1)

    def array_to_tree(left, right):
        nonlocal preorder_index
        # if there are no elements to construct the tree
        if left > right: return None

        # select the preorder_index element as the root and increment it
        root_value = preorder[preorder_index]
        root = Node(root_value)

        preorder_index += 1

        # build left and right subtree
        # excluding inorder_index_map[root_value] element because it's the root
        root.left = array_to_tree(left, inorder_index_map[root_value] - 1)
        root.right = array_to_tree(inorder_index_map[root_value] + 1, right)

        return root

    def calculateResult(self):
        return Node(1, 2, 3)
