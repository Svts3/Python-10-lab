class BinaryTree:
    def __init__(self, x, y):
        self.root = None
        self.left = None
        self.right = None
        self.x = x
        self.y = y

    def push(self, x, y):
        if self.root is None:
            self.root = BinaryTree(x, y)
        if self.y > y:
            if self.left is None:
                self.left = BinaryTree(x, y)
            else:
                self.left.push(x, y)
        elif self.y < y:
            if self.right is None:
                self.right = BinaryTree(x, y)
            else:
                self.right.push(x, y)

    def print_all_positive_y(self, root):
        if root is not None:
            self.print_all_positive_y(root.right)
            if root.y > 0:
                print(root.x, root.y, sep=", ")
            self.print_all_positive_y(root.left)

    def top_down_tree_traversal(self, root):
        if root:
            print(root.x, root.y, sep=", ")
            self.top_down_tree_traversal(root.left)
            self.top_down_tree_traversal(root.right)


    def delete_nodes_with_x_and_y(self, root):
        if root is None:
            return None
        root.left = self.delete_nodes_with_x_and_y(root.left)
        root.right = self.delete_nodes_with_x_and_y(root.right)
        if root.left is None and root.right is None:
            return root
        if root.left and root.left.y < 0 and root.left.x < 0:
            new_root = root.right
            temp = root
            root = None
            del temp
            return new_root

        if root.right and root.left.y < 0 and root.left.x < 0:
            new_root = root.left
            temp = root
            root = None
            del temp
            return new_root

        return root
