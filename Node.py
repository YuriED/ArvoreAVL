import time
import ast  # Módulo para literal_eval, que avalia uma string como expressão Python válida

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

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
        if root is None:
            return AVLNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        self.update_height(root)

        balance = self.balance_factor(root)

        # Casos de rotação
        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def in_order_traversal(self, root):
        result = []
        if root:
            result += self.in_order_traversal(root.left)
            result.append(root.key)
            result += self.in_order_traversal(root.right)
        return result

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# Função para ler os dados do arquivo
def read_data_from_file(filename):
    try:
        with open(filename, 'r') as file:
            # Avalia a string como uma expressão Python válida (literal_eval)
            return ast.literal_eval(file.read())
    except FileNotFoundError:
        print(f"Erro: O arquivo '{filename}' não foi encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao ler o arquivo '{filename}': {e}")
        return []

# Nome do arquivo contendo os dados
filename = "dados100_mil.txt"

# Lê os dados do arquivo
data = read_data_from_file(filename)

if not data:
    print("Não foi possível obter dados do arquivo. Verifique se o arquivo está no caminho correto e contém números válidos.")
else:
    # Cria uma árvore AVL
    avl_tree = AVLTree()

    # Insere os dados na árvore AVL e mede o tempo
    avl_start_time = time.time()
    for number in data:
        avl_tree.root = avl_tree.insert(avl_tree.root, number)
    avl_end_time = time.time()
    avl_time = avl_end_time - avl_start_time

    # Imprime os dados da árvore AVL em ordem e mede o tempo
    avl_print_start_time = time.time()
    avl_ordered_data = avl_tree.in_order_traversal(avl_tree.root)
    avl_print_end_time = time.time()
    avl_print_time = avl_print_end_time - avl_print_start_time

    # Imprime os resultados para a árvore AVL
    print(f"Tempo para inserir dados na AVL: {avl_time} segundos")
    print(f"Tempo para imprimir dados ordenados na AVL: {avl_print_time} segundos")

    # Ordena os dados usando Quicksort e mede o tempo
    quicksort_start_time = time.time()
    sorted_data = quicksort(data)
    quicksort_end_time = time.time()
    quicksort_time = quicksort_end_time - quicksort_start_time

    # Imprime os resultados para o Quicksort
    print(f"Tempo para ordenar dados usando Quicksort: {quicksort_time} segundos")


# ... (Código anterior)

if not data:
    print("Não foi possível obter dados do arquivo. Verifique se o arquivo está no caminho correto e contém números válidos.")
else:
    # Cria uma árvore AVL
    avl_tree = AVLTree()

    # Insere os dados na árvore AVL e mede o tempo
    avl_start_time = time.time()
    for number in data:
        avl_tree.root = avl_tree.insert(avl_tree.root, number)
    avl_end_time = time.time()
    avl_time = avl_end_time - avl_start_time

    # Imprime os dados da árvore AVL em ordem e mede o tempo
    avl_print_start_time = time.time()
    avl_ordered_data = avl_tree.in_order_traversal(avl_tree.root)
    avl_print_end_time = time.time()
    avl_print_time = avl_print_end_time - avl_print_start_time

    # Imprime os resultados para a árvore AVL
    print(f"Tempo para inserir dados na AVL: {avl_time} segundos")
    print(f"Tempo para imprimir dados ordenados na AVL: {avl_print_time} segundos")

    # Imprime os valores em ordem
    print("Valores no arquivo em ordem:")
    for value in avl_ordered_data:
        print(value)

    # Ordena os dados usando Quicksort e mede o tempo
    quicksort_start_time = time.time()
    sorted_data = quicksort(data)
    quicksort_end_time = time.time()
    quicksort_time = quicksort_end_time - quicksort_start_time

    # Imprime os resultados para o Quicksort
    print(f"Tempo para ordenar dados usando Quicksort: {quicksort_time} segundos")
