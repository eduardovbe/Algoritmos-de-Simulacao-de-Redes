from random import randint
from Maquina import *


# Define os novos intervalos de tempo conforme o algoritmo slotted ALOHA
def gerarintervalo_aloha(maquina, intervalo):
    for i in range(0, n):
        if maquina[i].intervalo == intervalo and maquina[i].flag == 0:
            novointervalo = randint(maquina[i].intervalo + 1, maquina[i].intervalo + 1023)
            maquina[i].intervalo = novointervalo
            maquina[i].colidiu = 0
            maquina[i].transmitindo = 0


# Inicializa as Máquinas
def criarmaquinas_aloha(maquina):
    for i in range(0, n):
        maquina.append(Maquina())
        maquina[i].numero = i + 1


# Verifica se há colisões
def verificacolisao_aloha(maquina):
    for i in range(0, n):
        for j in range(1, n):
            if i != j:
                if maquina[i].intervalo == maquina[j].intervalo:
                    if maquina[i].transmitindo == 1 and maquina[j].transmitindo == 1:
                        maquina[i].colidiu = 1


# Simula uma transmissão
def transmissao_aloha(maquina, i):
    maquina[i].transmitindo = 1


def main_aloha(t):
    global n
    n = t  # Número de Máquinas
    totaldecanais = 0  # Número de canais de tempos gastos
    tempo = 51.2 * (10 ** -6)  # Tempo de colisão
    maquina = []  # Vetor de Máquinas
    totaldetransmissoes = 0  # Total de transimissoes sem colisoes realizadas
    criarmaquinas_aloha(maquina)
    intervalo = 2
    while True:
        totaldecanais += 1
        for i in range(0, n):
            if maquina[i].flag == 0 and maquina[i].intervalo == intervalo:
                transmissao_aloha(maquina, i)
                # print(f"\nMáquina {i + 1} começou a tentar transmitir no canal de tempo {intervalo}")
        verificacolisao_aloha(maquina)
        for j in range(0, n):
            if maquina[j].colidiu == 0 and maquina[j].transmitindo == 1:
                maquina[j].flag = 1
                maquina[j].transmitindo = 0
                totaltempo = totaldecanais * tempo
                totaldetransmissoes += 1
                # print(f"Maquina {j + 1} concluiu em {intervalo}")
                if totaldetransmissoes == 1:
                    print(f'\nForam gastos {totaltempo} s para realizar uma transmissão')
                elif totaldetransmissoes == n:
                    print(
                        f'\nForam gastos {totaltempo} s para realizar todas as {totaldetransmissoes} transmissões')
                    return totaltempo
        gerarintervalo_aloha(maquina, intervalo)
        intervalo += 1
