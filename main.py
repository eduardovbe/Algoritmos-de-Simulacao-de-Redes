from aloha import *
from ppersistence import *
from recuobinario import *


def main():
    total = 0  # Total de tempo gastos na simulações
    print("Digite a Opção desejada:")
    print("1 - Slotted ALOHA")
    print("2 - CSMA p-persistente, com p = 1%")
    print("3 - algoritmo de recuo binário exponencial")
    op = int(input())
    if op == 1:
        print("Digite N (número de maquinas da simulação):")
        n = int(input())
        print("Digite o número de simulações desejadas:")
        x = int(input())
        for i in range(1, x + 1):
            print(f"\nSimulação {i}")
            total += main_aloha(n)
        print(f"\nMedia de tempo ate o final: {total / x}")
    elif op == 2:
        print("Digite N (número de maquinas da simulação):")
        n = int(input())
        print("Digite o número de simulações desejadas:")
        x = int(input())
        for i in range(1, x + 1):
            print(f"\nSimulação {i}")
            total += main_ppersistence(n)
        print(f"\nMedia de tempo ate o final: {total / x}")
    elif op == 3:
        print("Digite N (número de maquinas da simulação):")
        n = int(input())
        print("Digite o número de simulações desejadas:")
        x = int(input())
        for i in range(1, x + 1):
            print(f"\nSimulação {i}")
            total += main_recuobinario(n)
        print(f"\nMedia de tempo ate o final: {total / x}")
    else:
        print("opção invalida")
        main()


main()
