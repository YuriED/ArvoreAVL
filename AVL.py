import time
import random


class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def update_height(self, node):
        if not node:
            return 0
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, root, key):
        if not root:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)

        balance = self.balance_factor(root)

        # Left-Left Case
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # Right-Right Case
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # Left-Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Right-Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def insert_bulk(self, keys):
        for key in keys:
            self.root = self.insert(self.root, key)

    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def main():
    # Gerar arquivo com 100.000 números aleatórios
    with open("dados.txt", "w") as file:
        for _ in range(100000):
            file.write(str(random.randint(1, 1000000)) + "\n")

    # Ler os números do arquivo
    with open("dados.txt", "r") as file:
        numbers = [int(line.strip()) for line in file]

    # Usando AVL Tree
    avl_tree = AVLTree()

    start_time = time.time()
    avl_tree.insert_bulk(numbers)
    avl_sorted_result = avl_tree.inorder_traversal(avl_tree.root)
    avl_time = time.time() - start_time

    # Usando Quicksort
    start_time = time.time()
    quick_sorted_result = quicksort(numbers)
    quicksort_time = time.time() - start_time

    # Comparar os resultados
    print(f"Tempo AVL Tree: {avl_time:.4f} segundos")
    print(f"Tempo Quicksort: {quicksort_time:.4f} segundos")
    print(f"AVL Tree está ordenado corretamente: {avl_sorted_result == quick_sorted_result}")


if __name__ == "__main__":
    main()
