
class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __lt__(self, other):
        return self.value < other

    def __gt__(self, other):
        return self.value > other

    def __eq__(self, other):
        return self.value == other

class BinaryTree:
    def __init__(self):
        self.first_node = None
        self.length = 0


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
                    node.right = BinaryTreeNode(value)
                    self.length += 1
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = BinaryTreeNode(value)
                    self.length += 1

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
        pass

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

class RedBlackNode(BinaryTreeNode):
    Red = 0
    Black = 1
    def __init__(*args, **kwargs):
        BinaryTreeNode.__init__(self, *args, **kwargs)
        self.color = kwargs["color"]

class RedBlackTree(BinaryTree):
    def insert(self, value):
        pass

    def delete(self, value):
        pass


