"""Módulo com funções auxiliares para o projeto"""
import os
import random
import sys
import time
from typing import Callable

import pandas as pd

from quicksort import quicksort_iterative


def shuffle_percentage(array: list, percentage: int) -> list:
    """Shuffles a percentage of the list"""

    # Calcula o número de elementos a serem desordenados
    number_of_elements = int(len(array) * percentage / 100)

    # Escolhe os índices e elementos para desordenar
    indices_to_shuffle = random.sample(range(len(array)), number_of_elements)
    elements_to_shuffle = [array[i] for i in indices_to_shuffle]

    # Desordena os elementos e coloca de volta na lista
    random.shuffle(elements_to_shuffle)
    for i, index in enumerate(indices_to_shuffle):
        array[index] = elements_to_shuffle[i]

    return array


def create_unordered_list(number_of_elements: int, percentage: int) -> list:
    """Retorna uma lista desordenada de tamanho number_of_elements"""

    return shuffle_percentage(
        array=list(range(0, number_of_elements)), percentage=percentage
    )


def save_results(results: dict):
    """Salva os resultados em um arquivo csv"""

    df = pd.DataFrame([results])

    file_path = f"./data/{results['method']}.csv"
    file_dir = os.path.dirname(file_path)

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)

    if not os.path.isfile(file_path):
        df.to_csv(file_path, index=False)
        sys.exit()
    df.to_csv(file_path, mode="a", index=False, header=False)


def run_test(array: list, pivot_method: Callable, shuffle_amount: int) -> None:
    """Executa o quicksort e retorna o tempo de execução"""

    start = time.time()
    array = quicksort_iterative(array=array, pivot_fn=pivot_method)
    end = time.time()

    save_results(
        results={
            "method": pivot_method.__name__,
            "list_size": len(array),
            "shuffle_percentage": shuffle_amount,
            "time_seconds": float(f"{end - start:.4f}"),
        }
    )
