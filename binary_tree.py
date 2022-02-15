from typing import Optional


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Node | None = None
        self.right: Node | None = None


def insert(node: Optional[Node], value: int) -> Optional[Node]:
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def inorder(node: Optional[Node]) -> None:
    if node is not None:
        inorder(node.left)
        print(node.value)
        inorder(node.right)


def search(node: Optional[Node], value: int) -> bool:
    if node is None:
        return False

    if node.value == value:
        return True
    elif node.value > value:
        return search(node.left, value)
    else:
        return search(node.right, value)


if __name__ == "__main__":
    root: Optional[Node] = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
    root = insert(root, 7)
    root = insert(root, 1)
    root = insert(root, 10)
    root = insert(root, 2)
    print(search(root, 7))
