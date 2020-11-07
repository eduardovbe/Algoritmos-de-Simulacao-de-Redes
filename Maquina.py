class Maquina:
    def __init__(self):
        self.numero = 0  # numero da máquina
        self.intervalo = 2  # Intervalo no qual a maquina ira transmitir
        self.flag = 0  # Flag para verificar se máquina ainda precisa transimitir
        self.transmitindo = 0  # verifica se esta transmitindo em um canal
        self.colidiu = 0  # verifica se colidiu em um canal de tempo
        self.c = 0  # Numero de colisoes seguidas (usado apenas no recuo binario)
