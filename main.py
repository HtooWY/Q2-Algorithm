from BinaryTree import BinaryTree

if __name__ == '__main__':
    print("Q2 - Algorithm")
    print("Restriction: Input string must be basic math operations + - x ÷ ( ) on whole numbers.")
    while True:
        print("\nPlease Enter the Input String Math Operation")
        inputString = input("Enter input: ")
        if BinaryTree.validateString(inputString):

            bt = BinaryTree(inputString).constructTree()
            print("\nAnswer: " + str(bt.calculate()) + "\n")
            print("Binary Tree: \n")
            bt.printTree()
        else:
            print("Input string is invalid.\n")
