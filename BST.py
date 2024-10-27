from typing import Any


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self) -> None:
        self.root = None

    def insert(self, key: Any) -> Any:
        # helper method for managin insert
        def _insert(root: Node, key: Any) -> Node:
            if root is None:
                return Node(key)
            elif key <= root.key:
                root.left = _insert(root.left, key)
            else:
                root.right = _insert(root.right, key)
            return root

        if self.root == None:
            self.root = Node(key)
            return self.root
        else:
            return _insert(self.root, key)

    def inorder(self, node: Node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)


bst = BinarySearchTree()
bst.insert(20)
bst.insert(30)
bst.insert(40)
bst.insert(50)

bst.inorder(bst.root)
