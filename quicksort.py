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


def pivot_median(array: list):
    """Retorna o k-ésimo mínimo da lista"""

    # TODO: Implementar função
    return array


def pivot_find(array: list):
    """?????"""

    # TODO: Implementar função
    return array


def quicksort(array: list, pivot_fn: Callable) -> list:
    """Ordena uma lista usando o algoritmo quicksort"""

    if len(array) <= 1:
        return array
    pivot = pivot_fn(array)
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left, pivot_fn) + middle + quicksort(right, pivot_fn)
