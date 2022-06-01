from BinaryTree import BinaryTree


def main():
    binary_tree = BinaryTree(1, 12)
    binary_tree.push(2, 6)
    binary_tree.push(7, 5)
    binary_tree.push(7, -5)
    binary_tree.push(-7, -10)
    binary_tree.push(-12, -52)
    binary_tree.push(7, 76)
    binary_tree.push(7, 25)
    binary_tree.push(7, 90)
    binary_tree.top_down_tree_traversal(binary_tree)
    print("\n")
    binary_tree.print_all_positive_y(binary_tree)
    print("\n")
    binary_tree.delete_nodes_with_x_and_y(binary_tree)
    print("\n")
    binary_tree.top_down_tree_traversal(binary_tree)
if __name__ == '__main__':
    main()
