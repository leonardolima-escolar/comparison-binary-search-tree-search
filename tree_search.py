import timeit
import numpy as np
from PrettyPrint import PrettyPrintTree


from tree import ArvoreBinaria

ppt = PrettyPrintTree(
    lambda x: [x.esquerda, x.direita] if x else [],
    lambda x: str(x.valor) if x else ""
)


np.random.seed(633)


def gerar_arvore_aleatoria(tamanho):
    S = np.random.randint(low=0, high=100000, size=tamanho)
    tree = ArvoreBinaria()

    for i in S:
        tree.inserir(i)

    return tree


arvore_aleatoria = gerar_arvore_aleatoria(10000)

print("Iniciando busca na árvore...")

inicio = timeit.default_timer()
for i in range(1000000):
    arvore_aleatoria.buscar(i)
fim = timeit.default_timer()

print(fim-inicio)
