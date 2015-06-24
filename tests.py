#!/usr/bin/env python3

import unittest
from treesnake import *

class BstTests(unittest.TestCase):
    def test_random_is_bst(self):
        import random
        tree = BinarySearchTree()
        values = []

        for i in range(100000):
            value = random.randint(-9999999, 9999999)
            values.append(value)
            node = BinaryTreeNode(value)
            tree.insert(node)
        self.assertTrue(tree.is_bst())

        for value in values[200:900:3]:
            tree.delete(value)
        self.assertTrue(tree.is_bst())

    def test_empty_is_bst(self):
        tree = BinarySearchTree()
        self.assertTrue(tree.is_bst())

    def test_known_bad_is_not_bst(self):
        tree = BinarySearchTree()
        tree.first_node = node = BinaryTreeNode(10)
        node.left = BinaryTreeNode(5)
        node.right = node = BinaryTreeNode(15)
        node.left = BinaryTreeNode(6)  # This one is not valid
        node.right = BinaryTreeNode(20)
        self.assertFalse(tree.is_bst())

if __name__ == "__main__":
    unittest.main()

