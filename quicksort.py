"""Implementação do algoritmo de ordenação quicksort e dos métodos de escolha do pivô"""

import random
from typing import Callable


def pivot_first(array: list):
    """Retorna o primeiro elemento da lista"""

    return array[0]


def pivot_middle(array: list):
    """Retorna o elemento do meio da lista"""

    return array[len(array) // 2]


def pivot_mean(array: list):
    """Retorna a média do primeiro, último e elemento do meio da lista"""

    return (array[0] + array[len(array) // 2] + array[-1]) / 3


def pivot_random(array: list):
    """Retorna um elemento aleatório da lista"""

    return random.choice(array)


def pivot_median(array):
    """Retorna a mediana da lista"""

    def quickselect(array: list, k: int):
        """Retorna o k-ésimo menor elemento de uma lista"""

        def partition(array: list, low: int, high: int):
            """Particiona um array em relação a um pivô"""

            pivot = array[high]
            i = low - 1
            for j in range(low, high):
                if array[j] <= pivot:
                    i += 1
                    array[i], array[j] = array[j], array[i]
            array[i + 1], array[high] = array[high], array[i + 1]
            return i + 1

        low = 0
        high = len(array) - 1

        while True:
            if low == high:
                return array[low]
            pivot_index = random.randint(low, high)
            pivot_index = partition(array, low, high)

            if k == pivot_index:
                return array[k]
            if k < pivot_index:
                high = pivot_index - 1
                continue
            low = pivot_index + 1

    size = len(array)
    middle = size // 2
    if size % 2 == 1:
        return quickselect(array, middle)
    return (quickselect(array, middle - 1) + quickselect(array, middle)) / 2


def pivot_find(array: list):
    """?????"""

    # TODO: Implementar função
    return array


def quicksort_iterative(array: list, pivot_fn: Callable) -> list:
    """Ordena uma lista de forma iterativa usando o algoritmo quicksort"""

    def partition(array: list, low: int, high: int, pivot_fn: Callable) -> int:
        """Particiona um array em relação a um pivô"""

        pivot = pivot_fn(array=array)
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    if len(array) <= 1:
        return array

    stack = [(0, len(array) - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(array=array, low=low, high=high, pivot_fn=pivot_fn)
            stack.append((pivot_index + 1, high))
            stack.append((low, pivot_index - 1))
    return array


# def quicksort_recursive(array: list, pivot_fn: Callable) -> list:
#     """Ordena uma lista usando o algoritmo quicksort"""

#     if len(array) <= 1:
#         return array
#     pivot = pivot_fn(array)
#     left = [x for x in array if x < pivot]
#     middle = [x for x in array if x == pivot]
#     right = [x for x in array if x > pivot]
#     return (
#         quicksort_recursive(left, pivot_fn)
#         + middle
#         + quicksort_recursive(right, pivot_fn)
#     )
