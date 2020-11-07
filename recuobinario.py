from random import randint
from Maquina import *


# Define os novos intervalos de tempo conforme o algoritmo de recuo binário exponencial
def gerarintervalo_recuobinario(maquina, intervalo):
    global termina
    for i in range(0, n):
        if maquina[i].intervalo == intervalo and maquina[i].flag == 0:
            if maquina[i].colidiu == 1:
                if maquina[i].c < 10:
                    novointervalo = randint(maquina[i].intervalo, maquina[i].intervalo + 2 ** maquina[i].c - 1)
                elif maquina[i].c < 16:
                    novointervalo = randint(maquina[i].intervalo, maquina[i].intervalo + 1023)
                else:
                    termina = 1
                    return
                maquina[i].intervalo = novointervalo
                maquina[i].colidiu = 0
                maquina[i].transmitindo = 0


# Inicializa as Máquinas
def criarmaquinas_recuobinario(maquina):
    for i in range(0, n):
        maquina.append(Maquina())
        maquina[i].numero = i + 1


# Verifica se há colisões
def verificacolisao_recuobinario(maquina):
    global colisoes
    global verifica
    verifica = 0
    for i in range(0, n):
        for j in range(1, n):
            if i != j:
                if maquina[i].intervalo == maquina[j].intervalo:
                    if maquina[i].transmitindo == 1 and maquina[j].transmitindo == 1:
                        maquina[i].colidiu = 1
                        maquina[i].c += 1
                        verifica = 1
                        break


# Simula uma transmissão
def transmissao_recuobinario(maquina, i):
    maquina[i].transmitindo = 1


def main_recuobinario(t):
    global n
    global termina
    global verifica
    n = t  # Número de Máquinas
    totaldecanais = 0  # Número de canais de tempos gastos
    tempo = 51.2 * (10 ** -6)  # Tempo de colisão
    maquina = []  # Vetor de Máquinas
    totaldetransmissoes = 0  # Total de transimissoes sem colisoes realizadas
    criarmaquinas_recuobinario(maquina)
    intervalo = 2  # Canal de Tempo que esta acontecendo a simulação
    termina = 0  # Recebe 1 se c >= 16 , de qualquer estação
    verifica = 0 # variavel utilizada para verificar se houve alguma colisao naquele canal de tempo
    while termina == 0:
        if verifica == 0:
            totaldecanais += 1
        # Transmite e verifica se colidiu
        for i in range(0, n):
            if maquina[i].flag == 0 and maquina[i].intervalo == intervalo:
                transmissao_recuobinario(maquina, i)
        verificacolisao_recuobinario(maquina)
        # Verifica se alguma máquina consiguiu transmitir sem colisões
        for j in range(0, n):
            if maquina[j].colidiu == 0 and maquina[j].transmitindo == 1:
                maquina[j].flag = 1
                maquina[j].transmitindo = 0
                totaltempo = totaldecanais * tempo
                totaldetransmissoes += 1
                if totaldetransmissoes == 1:
                    print(f'\nForam gastos {totaltempo} s para realizar uma transmissão')
                elif totaldetransmissoes == n:
                    print(
                        f'\nForam gastos {totaltempo} s para realizar todas as {totaldetransmissoes} transmissões')
                    return totaltempo
        # Gera novos intervalos que as maquinas vão tentar transmitir ,e repete o mesmo canal de tempo se houve colisão
        gerarintervalo_recuobinario(maquina, intervalo)
        if verifica == 0:
            intervalo += 1
