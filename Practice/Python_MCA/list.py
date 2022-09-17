# print the outline of a binary tree in a single line
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return node(data)
    else:
        if root.data <= data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root


def printleft(root):
    if root is not None:
        if root.left is not None:
            print(root.data, end=" ")
            printleft(root.left)
        elif root.right is not None:
            print(root.data, end=" ")
            printleft(root.right)


def printleaf(root):
    if root is not None:
        printleaf(root.left)
        if root.left is None and root.right is None:
            print(root.data, end=" ")
        printleaf(root.right)


def printright(root):
    if root is not None:
        if root.right is not None:
            printright(root.right)
            print(root.data, end=" ")
        elif root.left is not None:
            printright(root.left)
            print(root.data, end=" ")


def main():
    root = None
    root = insert(root, 1)
    root = insert(root, 2)
    root = insert(root, 3)
    root = insert(root, 4)
    root = insert(root, 5)
    root = insert(root, 6)
    root = insert(root, 7)
    root = insert(root, 8)
    root = insert(root, 9)
    root = insert(root, 10)
    root = insert(root, 11)
    root = insert(root, 12)
    root = insert(root, 13)
    root = insert(root, 14)
    root = insert(root, 15)
    print(root.data, end=" ")
    printleft(root.left)
    printleaf(root)
    printright(root.right)


main()
