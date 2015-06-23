#!/usr/bin/env python3

import unittest
from treesnake import *

class BstTests(unittest.TestCase):
    def  test_is_bst(self):
        import random
        tree = BinarySearchTree()
        values = []

        for i in range(1000):
            value = random.randint(-9999999, 9999999)
            values.append(value)
            node = BinaryTreeNode(value)
            tree.insert(node)
        self.assertTrue(tree.is_bst())

#        for value in values[200:300:2]:
#            tree.delete(value)
#        self.assertTrue(tree.is_bst())


if __name__ == "__main__":
    unittest.main()

