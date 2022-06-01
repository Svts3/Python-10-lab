from BinaryTree import BinaryTree


def main():
    binary_tree = BinaryTree(1, 12)
    binary_tree.push(2, 6)
    binary_tree.push(7, 5)
    binary_tree.push(7, -5)
    binary_tree.push(-7, -10)
    binary_tree.push(-12, -52)
    binary_tree.push(7, 76)
    binary_tree.delete_nodes_with_x_and_y(binary_tree)
    binary_tree.go_through_tree_from_up_to_down(binary_tree)

if __name__ == '__main__':
    main()
