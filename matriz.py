import random


class Matriz:
    def __init__(self, dim):
        self.INI: int = 0
        self.MIN_RAND: int = 1
        self.MAX_RAND: int = 9
        self.dim: int = dim
        self.matriz: list[list[int]] = [[self.INI] * self.dim for _ in range(self.dim)]

    # def __str__(self): # dunder str necesita un return y no sé cómo hacerlo con este tipo
    #     for i in range(len(self.matriz)):
    #         print(self.matriz[i])

    def imprimir(self):
        for i in range(len(self.matriz)):
            print(self.matriz[i])

    def rellenar_aleatorio(self):
        for i in range(self.dim):
            for j in range(self.dim):
                self.matriz[i][j] = random.randint(self.MIN_RAND, self.MAX_RAND)

