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

class BinaryTreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.left = left
        self.right = right
        self.parent = parent
        self.value = value

    def find_min(self):
        node = self
        while node.left:
            node = node.left
        return node

    def replace(self, node=None):
        if self.parent:
            if self == self.parent.left:
                self.parent.left = node
            else:
                self.parent.right = node
        if node:
            node.parent = self.parent

    def delete(self):
        if self.left and self.right:
            successor = self.right.find_min()
            self.value = successor.value
            successor.delete()
        elif self.left:
            self.replace(self.left)
        elif self.right:
            self.replace(self.right)
        else:
            self.replace(None)

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __eq__(self, other):
        return self.value == other

class BinaryTree:
    def __init__(self):
        self.first_node = None
        self._length = 0

    def __len__(self):
        return self._length

    def bft(self):
        """ Breadth-first traversal generator """
        fifo = collections.deque()
        fifo.append(self.first_node)
        while fifo:
            node = fifo.popleft()
            yield node
            if node.left:
                fifo.append(node.left)
            if node.right:
                fifo.append(node.right)

    def bfs(self, value):
        """ Breadth-first-search

            @value  The value to search for
            @return The node containing the value, or None if not found
        """
        for node in (x for x in self.bft() if x == value):
            return node
        return None

    def preorder_dft(self):
        """ Pre-order depth-first traversal generator """
        stack = []
        node = self.first_node
        while stack or node:
            yield node
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                node = node.right

    def preorder_dfs(self, value):
        """ Pre-order depth-first-search

            @value  The value to search for
            @return The node containing the value, or None if not found
        """
        for node in (x for x in self.preorder_dft() if x == value):
            return node
        return None

    def inorder_dft(self):
        """ In-order depth-first traversal generator """
        stack = []
        node = self.first_node
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right

    def inorder_dfs(self, value):
        """ In-order depth-first-search

            @value  The value to search for
            @return The node containing the value, or None if not found
        """
        for node in (x for x in self.inorder_dft() if x == value):
            return node
        return None


class BinarySearchTree(BinaryTree):
    def insert(self, value):
        node = self.first_node
        if not node:
            self.first_node = BinaryTreeNode(value)
            return
        while True:
            if node == value:  # Already in the tree
                break
            elif value > node:
                if node.right:
                    node = node.right
                else:
                    node.right = BinaryTreeNode(value, parent=node)
                    self._length += 1
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = BinaryTreeNode(value, parent=node)
                    self._length += 1

    def find(self, value):
        node = self.first_node
        while True:
            if not node:
                return None
            elif node == value:
                return node
            elif value > node:
                node = node.right
            else:
                node = node.left

    def delete(self, value):
        node = self.find(value)
        if node:
            node.delete()
            self._length -= 1
            return True
        else:
            return False

    def is_bst(self):
        if self.first_node is None:
            return True
        generator = self.inorder_dft()
        last = next(generator)
        for node in generator:
            if node.value < last.value:
                return False
            last = node
        return True

