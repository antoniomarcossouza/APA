"""Módulo com funções auxiliares para o projeto"""

import random
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
