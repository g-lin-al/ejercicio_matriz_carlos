from constantes import Cons
from matriz import Matriz


class Main:
    def imprimir_menu(self) -> None:
        print("." * Cons.ESTRELLAS_NUM)
        print(f"{Cons.OPCION_MATRIZ_1}- Crear matriz 1.")
        print(f"{Cons.OPCION_MATRIZ_2}- Crear matriz 2 (matriz 1 debe estar creada).")
        print(f"{Cons.OPCION_MOSTRAR}- Mostrar cualquier matriz.")
        print(f"{Cons.OPCION_MULTIPLICAR}- Multiplicar matrices.")
        print(f"{Cons.OPCION_SALIR}- SALIR.")
        print("." * Cons.ESTRELLAS_NUM)

    def pedir_opcion(self) -> int:
        opcion: int = -1
        opcion = int(input("¿Opción?: "))
        return opcion

    def multiplicar_matrices(self, mat_1: Matriz, mat_2: Matriz) -> Matriz:
        c: Matriz = Matriz(len(mat_1.matriz))
        for i in range(len(mat_1.matriz)):
            for j in range(len(mat_2.matriz)):
                c.matriz[i][j] = ((mat_1.matriz[i][0] * mat_2.matriz[0][j]) +
                                  (mat_1.matriz[i][1] * mat_2.matriz[1][j]) +
                                  (mat_1.matriz[i][2] * mat_2.matriz[2][j]))
        return c

    def run(self):
        opcion: int = -1
        opcion_letra: str = ""
        dim: int = 0
        a: Matriz = Matriz(dim)
        b: Matriz = Matriz(dim)

        while opcion != Cons.OPCION_SALIR:
            self.imprimir_menu()
            opcion = self.pedir_opcion()
            if opcion == Cons.OPCION_MATRIZ_1:
                dim = int(input("¿Dimensión?: "))
                a = Matriz(dim)
                a.rellenar_aleatorio()
                print("Matriz creada aleatoriamente:")
                print(a)
            elif opcion == Cons.OPCION_MATRIZ_2:
                b = Matriz(dim)
                b.rellenar_aleatorio()
                print(f"Matriz creada aleatoriamente de dimensión {dim}:")
                print(b)
            elif opcion == Cons.OPCION_MOSTRAR:
                print("Introducir letra \"a\" para mostrar la matriz 1.")
                print("Introducir letra \"b\" para mostrar la matriz 2.")
                opcion_letra = input("¿Letra?: ")
                if opcion_letra == Cons.OPCION_A:
                    print(a)
                elif opcion_letra == Cons.OPCION_B:
                    print(b)
                else:
                    print("--- ERROR --- Opción no reflejada.")
            elif opcion == Cons.OPCION_MULTIPLICAR:
                print(self.multiplicar_matrices(a, b))
            elif opcion == Cons.OPCION_SALIR:
                print("Cerrando aplicación...")
            else:
                print("--- ERROR --- Opción no reflejada. Introducir de nuevo.")


Main().run()
