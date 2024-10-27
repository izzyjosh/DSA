from typing import Any

class BinarySearchTree:
  
  def __init__(self, data: Any) -> None:
    self.data = data
    self.left = None
    self.right = None
    
  def insert(self, node, data: Any) -> Any:
    if node is None:
      return BinarySearchTree(data)
      
    if node.data == data:
      return node
      
    if node.data <= data:
      node.right = self.insert(node.right, data)
    else:
      node.left = self.insert(node.left, data)
    return node
    
  def inorder_transversal(self, root):
    if root:
      inorder_transversal(root.left)
      print(root.data, end=" ")
      
    inorder_transversal(root.right)
    
root = BinarySearchTree(10)
print(root.data)
data2 = root.insert(root, 20)
print(data2.data.data)

