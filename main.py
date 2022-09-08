from BinaryTree import BinaryTree

if __name__ == '__main__':
    print("Restrictions")
    print("Please close the bracket for the whole expression\n")
    while True:
        #((15 / (7 − (1 + 1) ) ) × -3 ) − (2 + (19 + 1))
        teststring = '((15 / (7 -(1 + 1) ) ) * 3 ) - (2 + (1 + 1))'
        postfix =['15', '7', '1', '1', '+', '-', '/', '-', '3', '*', '2', '1',  '1','+',  '+', '-']

        print("Please Enter the Input String Math Operation")
        inputString = input("Enter input: ")

        bt = BinaryTree(teststring).constructTree()
        # bt.inorder()
        # bt= BinaryTree.constructTree(teststring)
        print(bt.calculate())



