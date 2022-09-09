import pytest
from BinaryTree import BinaryTree
class TestMathOperations:
    @pytest.fixture
    def binarytree(self):
        return BinaryTree('1+2')

    # 1. Simple Operation
    def test_1(self, binarytree):
        binarytree.setNewBinaryTree('1+2')
        assert binarytree.constructTree().calculate() == 3

    # 2. Divide by Zero
    def test_2(self, binarytree):
        binarytree.setNewBinaryTree('0/0')
        assert binarytree.constructTree().calculate() == 'Invalid (Divided by Zero)'

    # ((15 / (7 -(1 + 1) ) ) * -3 ) - (2 + (1 + 1))
    def test_3(self, binarytree):
        binarytree.setNewBinaryTree('((15 / (7 -(1 + 1) ) ) * -3 ) - (2 + (1 + 1))')
        assert binarytree.constructTree().calculate() == -13

    # (((8*9)/3)+(22-3))-((88+32)/(4*2))
    def test_4(self, binarytree):
        binarytree.setNewBinaryTree('(((8*9)/3)+(22-3))-((88+32)/(4*2))')
        assert binarytree.constructTree().calculate() == 28

    # ((0+10)*9)+(20+(20/5))
    def test_5(self, binarytree):
        binarytree.setNewBinaryTree('((0+10)*9)+(20+(20/5))')
        assert binarytree.constructTree().calculate() == 114

    # ((((20/10)*(1+20))-((25/5)+(9-7)))-22)*((120/(13+7))*9)
    def test_6(self, binarytree):
        binarytree.setNewBinaryTree('((((20/10)*(1+20))-((25/5)+(9-7)))-22)*((120/(13+7))*9)')
        assert binarytree.constructTree().calculate() == 702

    #((((70-88)*(1+5))-((79/5)+(-9-7)))-22)*((-34/(13+7))*9)
    def test_7(self, binarytree):
        binarytree.setNewBinaryTree('((((70-88)*(1+-5))-((79/5)+(9-7)))-22)*((34/(13+7))*9)')
        assert binarytree.constructTree().calculate() == 492.66

    # (-90 - (22 / 2*(3 + 10))) - (-90 - (43 + (117 / 3)))
    def test_8(self, binarytree):
        binarytree.setNewBinaryTree('(-90-(65/(3+10)))-(-90-(43+(117/3)))')
        assert binarytree.constructTree().calculate() == 77

    # 90*(-229/1)
    def test_9(self, binarytree):
        binarytree.setNewBinaryTree('90*(-229/1)')
        assert binarytree.constructTree().calculate() == -20610

    # Validate Input string
    def test_10(self, binarytree):
        assert BinaryTree.validateString('(Normal String)') == False
