
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
        stack = []
        node = self.first_node
        last_node = None

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if last_node and node < last_node:
                    return False
                last_node = node
                node = node.right

        return True


