import sys
import unittest

from dsalgo.BST_Traversal_Algorithms import Node, BinarySearchTree

class BstTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(BstTest, self).__init__(*args, **kwargs)
        self.tree = BinarySearchTree()
        self.arr = [120, 40, 400, 20, 100, 30]

        for i in self.arr:
	        self.tree.create(arr[i])

    def test_display(self):
        print ("Inorder Traversal: ",self.tree.inorder(self.tree.get_root()))
        print ("Preorder Traversal: ",self.tree.preorder(self.tree.get_root()))
        print ("Postorder Traversal: ",self.tree.postorder(self.tree.get_root()))


if __name__ == '__main__':
    unittest.main()
    sys.exit(0)