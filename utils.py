def quicksort(array):
    if len(array) < 2:
        return array

    pivo = array[0]
    menores = [i for i in array[1:] if i <= pivo]
    maiores = [i for i in array[1:] if i > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)


def bubblesort(array):
    tamanho = len(array)

    for i in range(tamanho):
        for j in range(0, tamanho-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array


def busca_binaria(array, item):
    comeco = 0
    final = len(array)-1

    while comeco <= final:
        meio = (comeco + final)//2
        tentativa = array[meio]

        if tentativa == item:
            return meio
        if tentativa > item:
            final = meio - 1
        else:
            comeco = meio + 1

    return None


def busca_linear(array, item):
    for i, elemento in enumerate(array):
        if elemento == item:
            return i
    return None
