from BinaryTree import BinaryTree

if __name__ == '__main__':
    print("Restrictions")
    print("Please close the bracket for the whole expression")
    while True:

        teststring = '((15 / (7 -(1 + 1) ) ) * 3 ) - (2 + (1 + 1))'
        # postfix =['15', '7', '1', '1', '+', '-', '/', '-', '3', '*', '2', '1',  '1','+',  '+', '-']

        print("\nPlease Enter the Input String Math Operation")
        inputString = input("Enter input: ")
        bt = BinaryTree(teststring).constructTree()
        print("Answer: " +str(bt.calculate())+"\n")
        print ("Binary Tree: \n")
        bt.printTree()



