"""
Implement a binary tree using Python, and show its usage with some examples.
"""


class TreeNode:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))
    
    def traverse_pre_order(self):
        if self is None:
            return []
        return([self.key] +
               TreeNode.traverse_pre_order(self.left) +
               TreeNode.traverse_pre_order(self.right))
    
    def traverse_post_order(self):
        if self is None:
            return []
        return(TreeNode.traverse_post_order(self.left) +
               TreeNode.traverse_post_order(self.right) +
               [self.key])
    
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + "*")
            return
        
        # If the node is the leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
        
        # If the Node has children
        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left, space, level+1)
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self) -> str:
        return "Binary Tree <{}>".format(self.to_tuple())
    
    def __repr__(self) -> str:
        return "Binary Tree <{}>".format(self.to_tuple())
    
    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node


if __name__ == '__main__':
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = TreeNode.parse_tuple(tree_tuple)
    print(tree)
    print("Height: {}".format(tree.height()))
    print("Size: {}".format(tree.size()))
    print("In-order traversal: {}".format(tree.traverse_in_order()))

    tree2 = TreeNode.parse_tuple((1, 2, (4, 3, 5)))
    print(tree2)
    print("Height: {}".format(tree2.height()))
    print("Size: {}".format(tree2.size()))
    print("In-order traversal: {}".format(tree2.traverse_in_order()))
