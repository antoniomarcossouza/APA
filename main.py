"""Script to run the quicksort algorithm"""

import argparse
def parse_arguments():
    """Parse the arguments passed to the script"""

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
        default="pivot_middle",
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

    number_of_elements = args.elements
    percentage_to_shuffle = args.shuffle
