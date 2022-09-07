from BinaryTree import BinaryTree

if __name__ == '__main__':
    print("Restrictions")
    print("Please close the bracket for the whole expression\n")
    while True:
        #((15 / (7 − (1 + 1) ) ) × -3 ) − (2 + (1 + 1))
        teststring = '((15 / (7 -(1 + 1) ) ) * -3 ) - (2 + (1 + 1))'
        postfix =['15', '7', '1', '1', '+', '-', '/', '-', '3', '*', '2', '1',  '1','+',  '+', '-']
        prefix =
        print("Please Enter the Input String Math Operation")
        inputString = input("Enter input: ")

        bt = BinaryTree(teststring)
        bt.inorder()
        print(postfix)



