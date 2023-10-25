from dataclasses import dataclass

@dataclass
class TreeNode:
    value: int
    left_child: 'Node' = None
    right_child: 'Node' = None

@dataclass
class BinaryTree:
    root: TreeNode = None
    def bad_insert(self, value1, value2):
        self.root.left_child = TreeNode(value1)
        self.root.right_child = TreeNode(value2)
    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left_child is not None:
                self._insert_recursive(current_node.left_child, value)
            else:
                current_node.left_child = TreeNode(value)
        elif value > current_node.value:
            if current_node.right_child is not None:
                self._insert_recursive(current_node.right_child, value)
            else:
                current_node.right_child = TreeNode(value)
        else:
            # Value already exists in the tree, handle as per your requirement.
            pass

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current_node, value):
        if not current_node:
            return False
        if current_node.value == value:
            return True
        elif value < current_node.value:
            return self._search_recursive(current_node.left_child, value)
        else:
            return self._search_recursive(current_node.right_child, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, current_node, value):
        if current_node is None:
            return current_node # If the tree is empty or the node is not found, return None.
       # Recursive calls for ancestors of the node to be deleted.
        if value < current_node.value:
            current_node.left_child = self._delete_recursive(current_node.left_child, value)# Recur down the left subtree if the value is smaller.
        elif value > current_node.value:
            current_node.right_child = self._delete_recursive(current_node.right_child, value) # Recur down the left subtree if the value is greator.
        else:
            # Node with only one child or no child
            if current_node.left_child is None:
                temp_node = current_node.right_child
                del current_node
                return temp_node
            elif current_node.right_child is None:
                temp_node = current_node.left_child
                del current_node
                return temp_node

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            current_node.value = self._find_min_value(current_node.right_child)

            # Delete the inorder successor
            current_node.right_child = self._delete_recursive(current_node.right_child, current_node.value)

        return current_node

    def _find_min_value(self, node):
        current = node
        while current.left_child is not None:
            current = current.left_child
        return current.value
        
    def lowest_common_ancestor(self, node1, node2):
        return self.lowest_common_ancestor_recursive(self.root, node1, node2)
        
    def lowest_common_ancestor_recursive(self, ancestor, node1, node2):
        ancestor = self.root
        if node1 or node2 == self.root:
            return self.root
        else:
            if self._search_recursive(ancestor, node1.value) is True and self._search_recursive(ancestor, node2.value) is True:
                if node1.value < ancestor.value and node2.value < ancestor.value:
                    self.lowest_common_ancestor_recursive(ancestor.left_child, node1, node2)
                elif node1.value > ancestor.value and node2.value > ancestor.value:
                    self.lowest_common_ancestor_recursive(ancestor.right_child, node1, node2)
                else:
                    return ancestor.value
            else:
                return print("Error: No common ancestor found")
                
    def deleteTree(self):
        while self.root is not None:
            self.delete(self.root.value)

    def in_order_traversal(self):
        self._in_order_recursive(self.root)
        print()

    def _in_order_recursive(self, current_node):
        if current_node is not None:
            self._in_order_recursive(current_node.left_child)
            print(current_node.value, end=' ')
            self._in_order_recursive(current_node.right_child)

def isBST(tree):
    return _isBST_recursive(tree.root)

def _isBST_recursive(current_node):

    if current_node is not None:
        if current_node.left_child is not None:
            if current_node.left_child.value < current_node.value:
                return _isBST_recursive(current_node.left_child)
            else:
                return False
        else:
            pass
    if current_node is not None:
        if current_node.right_child is not None:
            if current_node.right_child.value > current_node.value:
                return _isBST_recursive(current_node.right_child)
            else:
                return False
        else:
            pass
    return True


# Example usage:
if __name__ == "__main__":
    binary_tree = BinaryTree()
    elements = [44, 17, 88, 8, 32, 65, 97,54,82,93,78,80]

    for element in elements:
        binary_tree.insert(element)
    print(binary_tree.in_order_traversal())
    print(isBST(binary_tree))
    binary_tree.deleteTree()
    print("deleted")
    print(binary_tree.in_order_traversal())

    binary_tree2 = BinaryTree()
    binary_tree2.insert(15)
    binary_tree2.bad_insert(20, 10)
    print(binary_tree2.in_order_traversal())
    print(isBST(binary_tree2))

    print(binary_tree.lowest_common_ancestor(8, 32) # Output: 17
    print(binary_tree.lowest_common_ancestor(17, 93) # Output: 44
    print(binary_tree.lowest_common_ancestor(88, 65) # Output: 88
    print(binary_tree.lowest_common_ancestor(5, 78) # Output: "Error: no common ancestor found."
          
    """
    print(binary_tree.search(65))  # Output: True
    print(binary_tree.search(9))  # Output: False
    print("Original Binary Search Tree:")
    print(binary_tree.search(65))  # Output: True

    # Deleting a node with one child
    binary_tree.delete(65)
    print("Binary Search Tree after deleting 65:")
    print(binary_tree.search(65))  # Output: False

    # Deleting a node with no children
    binary_tree.delete(8)
    print("Binary Search Tree after deleting 8:")
    print(binary_tree.search(8))   # Output: False

    # Deleting a node with two children
    binary_tree.delete(88)
    print("Binary Search Tree after deleting 88:")
    print(binary_tree.search(88))  # Output: False """""
