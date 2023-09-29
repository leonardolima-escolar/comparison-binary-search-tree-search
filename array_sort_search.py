import numpy as np
import timeit

from utils import bubblesort, busca_binaria, busca_linear, quicksort


np.random.seed(633)
S = np.random.randint(low=0, high=100000, size=10000)


print("Iniciando busca linear...")

inicio = timeit.default_timer()
for i in range(10000):
    busca_linear(S, i)

fim = timeit.default_timer()

print(fim-inicio)

print("Bubblesort...")

inicio = timeit.default_timer()

S_bs = bubblesort(S.copy())

fim = timeit.default_timer()

print(fim-inicio)

print("Quicksort...")

inicio = timeit.default_timer()
S = quicksort(S)

fim = timeit.default_timer()

print(fim-inicio)

print("Iniciando busca binária...")

inicio = timeit.default_timer()
for i in range(1000000):
    busca_binaria(S, i)

fim = timeit.default_timer()

print(fim-inicio)
