from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Optional[Node], value: int) -> Optional[Node]:
            if node is None:
                return Node(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    def inorder(self) -> None:
        def _inorder(node: Optional[Node]) -> None:
            if node is not None:
                _inorder(node.left)
                print(node.value)
                _inorder(node.right)

        _inorder(self.root)

    def search(self, value: int) -> None:
        def _search(node: Optional[Node], value: int) -> bool:
            if node is None:
                return False

            if node.value == value:
                return True
            elif node.value > value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        _search(self.root, value)

    def min_value(self, node: Optional[Node]) -> Optional[Node]:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value: int) -> None:
        def _remove(node: Optional[Node], value: int) -> Optional[Node]:
            if node is None:
                return node

            if node.value > value:
                node.left = _remove(node.left, value)
            elif node.value < value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                temp = self.min_value(node.right)
                node.value = temp.value
                node.right = _remove(node.right, temp.value)
            return node

        _remove(self.root, value)


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(6)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(1)
    binary_tree.insert(10)
    binary_tree.insert(2)
    binary_tree.inorder()
