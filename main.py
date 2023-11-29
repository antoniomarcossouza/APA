"""Código principal do projeto"""

import argparse

from utils import run_test, create_unordered_list
from quicksort import (
    pivot_first,
    pivot_middle,
    pivot_mean,
    pivot_random,
    pivot_median,
    pivot_find,
)


def parse_arguments():
    """Interpreta os argumentos passados para o programa"""

    parser = argparse.ArgumentParser(description="")

    parser.add_argument(
        "--elements",
        type=int,
        help="Número de elementos na lista",
    )
    parser.add_argument(
        "--shuffle",
        choices=[5, 25, 45],
        type=int,
        help="Porcentagem de elementos a serem desordenados",
    )
    parser.add_argument(
        "--pivot",
        choices=[
            "pivot_first",
            "pivot_middle",
            "pivot_mean",
            "pivot_random",
            "pivot_median",
            "pivot_find",
        ],
        help="Escolhe a função de de escolher o pivô para o quicksort",
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    pivot_function = {
        "pivot_first": pivot_first,
        "pivot_middle": pivot_middle,
        "pivot_mean": pivot_mean,
        "pivot_random": pivot_random,
        "pivot_median": pivot_median,
        "pivot_find": pivot_find,
    }[args.pivot]
    elements = args.elements
    shuffle = args.shuffle

    unordered_list = create_unordered_list(number_of_elements=elements, percentage=shuffle)
    run_test(array=unordered_list, pivot_method=pivot_function, shuffle_amount=shuffle)
