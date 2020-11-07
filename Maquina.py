class Maquina:
    def __init__(self):
        self.numero = 0
        self.intervalo = 2
        self.flag = 0  # Flag para verificar se máquina ainda precisa transimitir
        self.transmitindo = 0
        self.colidiu = 0
        self.c = 0