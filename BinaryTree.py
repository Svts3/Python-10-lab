class BinaryTree:
    def __init__(self, x, y):
        self.left = None
        self.right = None
        self.x = x
        self.y = y

    def push(self, x, y):
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
            self.print_all_positive_y(root.left)
            if root.y > 0:
                print(root.x, root.y, sep=", ")
            self.print_all_positive_y(root.right)

    def top_down_tree_traversal(self, root):
        if root:
            print(root.x, root.y, sep=", ")
            self.top_down_tree_traversal(root.left)
            self.top_down_tree_traversal(root.right)

    def get_list_of_keys(self):
        list_of_keys = []
        if self.y < 0 and self.x < 0:
            list_of_keys.append(self)
        if self.left:
            list_of_keys += self.left.get_list_of_keys()
        if self.right:
            list_of_keys += self.right.get_list_of_keys()
        return list_of_keys

    def search_by_key(self, y):
        found = []
        if self.y == y:
            found.append(self)
        if self.left:
            found += self.left.search_by_key(y)
        if self.right:
            found += self.right.search_by_key(y)
        return found

    def find_minimal_node(self):
        if self.left is None:
            return self
        return self.left.find_minimal_node()

    def delete_node(self, key):
        if key < self.y:
            if self.left:
                self.left = self.left.delete_node(key)
        elif key > self.y:
            if self.right:
                self.right = self.right.delete_node(key)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            min_val = self.right.find_minimal_node()
            self.y, self.x = min_val.y, min_val.x
            self.right = self.right.delete_node(min_val.y)

        return self

    def delete_all_negatives(self):
        list_of_keys = self.get_list_of_keys()
        for i in list_of_keys:
            if i in list_of_keys:
                self.delete_node(i.y)
