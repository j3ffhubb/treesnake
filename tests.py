#!/usr/bin/env python3
"""
This file is part of the treesnake project, Copyright Jeff Hubbard

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; version 3 of the License.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
"""

import collections
import random
import unittest
from treesnake import *

class BinaryTreeTests(unittest.TestCase):
    def test_search(self):
        tree = BinaryTree()
        vals = [random.randint(-9999, 9999) for x in range(50)]
        gen = (BinaryTreeNode(x) for x in vals)
        tree.first_node = next(gen)
        fifo = collections.deque()
        fifo.append(tree.first_node)

        while fifo:
            node = fifo.popleft()
            try:
                node_left = next(gen)
            except StopIteration:
                break
            node.left = node_left
            fifo.append(node_left)
            try:
                node_right = next(gen)
            except StopIteration:
                break
            node.right = node_right
            fifo.append(node_right)

        for val in vals:
            bfs = tree.bfs(val)
            preorder_dfs = tree.preorder_dfs(val)
            inorder_dfs = tree.inorder_dfs(val)
            for result in (bfs, preorder_dfs, inorder_dfs):
                self.assertIsNotNone(result)
                self.assertEqual(val, result.value)

        out_of_range = 1000000 # randint could not have generated this number

        for method in (tree.bfs, tree.preorder_dfs, tree.inorder_dfs):
            result = method(out_of_range)
            self.assertIsNone(result)

    def test_height(self):
        tree = BinaryTree()
        self.assertEqual(tree.height(tree.first_node), -1)
        tree.first_node = BinaryTreeNode(1)
        self.assertEqual(tree.height(tree.first_node), 0)
        tree.first_node.left = BinaryTreeNode(0)
        self.assertEqual(tree.height(tree.first_node), 1)


class BstTests(unittest.TestCase):
    def test_random_is_bst(self):
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

