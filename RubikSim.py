# !/usr/bin/python
# -*- coding: utf-8 -*-

# Indices cubo[]
#                   0   1   2
#                   3   4   5
#                   6   7   8
#
#   9   10  11      18  19  20      27  28  29      36  37  38
#   12  13  14      21  22  23      30  31  32      39  40  41
#   15  16  17      24  25  26      33  34  35      42  43  44
#
#                   45  46  47
#                   48  49  50
#                   51  52  53


__author__ = 'Marcos Pérez Martín'
__title__ = 'RubikSim'
__date__ = '29/05/2019'
__version__ = '1.0'

from termcolor import colored
import random

r = "red"
b = "blue"
g = "green"
y = "yellow"
c = "cyan"
w = "white"

colores = [y, r, b, g, c, w]
cubo = []
secuencia = []


def print_cubo(cubo):
    print("\n")

    # Cara TOP

    print(" " * 16, end="")
    print(colored("  ", "white", "on_" + cubo[0]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[1]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[2]), end="")
    print("\n")
    print(" " * 16, end="")
    print(colored("  ", "white", "on_" + cubo[3]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[4]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[5]), end="")
    print("\n")
    print(" " * 16, end="")
    print(colored("  ", "white", "on_" + cubo[6]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[7]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[8]), end="")
    print("\n\n")

    # Caras LEFT, FRONT, RIGHT, BACK

    # Cara LEFT Fila 1
    print(" " * 2, end="")
    print(colored("  ", "white", "on_" + cubo[9]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[10]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[11]), end="")

    # Cara FRONT Fila 1
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[18]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[19]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[20]), end="")

    # Cara RIGHT Fila 1
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[27]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[28]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[29]), end="")

    # Cara BACK Fila 1
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[36]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[37]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[38]), end="")
    print("\n")

    # Cara LEFT Fila 2
    print(" " * 2, end="")
    print(colored("  ", "white", "on_" + cubo[12]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[13]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[14]), end="")

    # Cara FRONT Fila 2
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[21]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[22]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[23]), end="")

    # Cara RIGHT Fila 2
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[30]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[31]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[32]), end="")

    # Cara BACK Fila 2
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[39]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[40]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[41]), end="")
    print("\n")

    # Cara LEFT Fila 3
    print(" " * 2, end="")
    print(colored("  ", "white", "on_" + cubo[15]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[16]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[17]), end="")

    # Cara FRONT Fila 3
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[24]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[25]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[26]), end="")

    # Cara RIGHT Fila 3
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[33]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[34]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[35]), end="")

    # Cara BACK Fila 3
    print(" " * 4, end="")
    print(colored("  ", "white", "on_" + cubo[42]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[43]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[44]), end="")
    print("\n\n")

    # Cara DOWN

    print(" " * 16, end="")
    print(colored("  ", "white", "on_" + cubo[45]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[46]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[47]), end="")
    print("\n")
    print(" " * 16, end="")
    print(colored("  ", "white", "on_" + cubo[48]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[49]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[50]), end="")
    print("\n")
    print(" " * 16, end="")
    print(colored("  ", "white", "on_" + cubo[51]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[52]), end="")
    print("  ", end="")
    print(colored("  ", "white", "on_" + cubo[53]), end="")
    print("\n\n")


def inicia_cubo(cubo):
    # Inicializo la lista de elementos del cubo montado
    for i in range(9):
        cubo.append(w)
    for i in range(9, 18):
        cubo.append(c)
    for i in range(18, 27):
        cubo.append(g)
    for i in range(27, 36):
        cubo.append(r)
    for i in range(36, 45):
        cubo.append(b)
    for i in range(45, 54):
        cubo.append(y)

    return cubo


def F(cubo):

    posic_orig = [17, 14, 11, 45, 46, 47, 24, 21, 18, 25,
                  19, 26, 23, 20, 6, 7, 8, 33, 30, 27]
    posic_nuevas = [6, 7, 8, 11, 14, 17, 18, 19, 20, 21,
                    23, 24, 25, 26, 27, 30, 33, 45, 46, 47]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]

    return("F")


def F2(cubo):
    F(cubo)
    F(cubo)
    return("F2")


def Fp(cubo):

    posic_orig = [27, 30, 33, 8, 7, 6, 20, 23, 26, 19, 25,
                  18, 21, 24, 47, 46, 45, 11, 14, 17]
    posic_nuevas = [6, 7, 8, 11, 14, 17, 18, 19, 20, 21,
                    23, 24, 25, 26, 27, 30, 33, 45, 46, 47]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("F'")


def R(cubo):

    posic_orig = [26, 23, 20, 47, 50, 53, 42, 39, 36, 6,
                  7, 8, 33, 30, 27, 34, 28, 35, 32, 29]
    posic_nuevas = [8, 5, 2, 20, 23, 26, 47, 50, 53, 36,
                    39, 42, 27, 28, 29, 30, 32, 33, 34, 35]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("R")


def R2(cubo):
    R(cubo)
    R(cubo)
    return("R2")


def Rp(cubo):

    posic_orig = [36, 39, 42, 2, 5, 8, 20, 23, 26, 53,
                  50, 47, 29, 32, 35, 28, 34, 27, 30, 33]
    posic_nuevas = [8, 5, 2, 20, 23, 26, 47, 50, 53, 36,
                    39, 42, 27, 28, 29, 30, 32, 33, 34, 35]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("R'")


def L(cubo):

    posic_orig = [44, 41, 38, 51, 48, 45, 18, 21, 24, 0,
                  3, 6, 15, 12, 9, 16, 10, 17, 14, 11]
    posic_nuevas = [0, 3, 6, 38, 41, 44, 45, 48, 51, 18,
                    21, 24, 9, 10, 11, 12, 14, 15, 16, 17]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("L")


def L2(cubo):
    L(cubo)
    L(cubo)
    return("L2")


def Lp(cubo):

    posic_orig = [18, 21, 24, 6, 3, 0, 44, 41, 38, 45,
                  48, 51, 11, 14, 17, 10, 16, 9, 12, 15]
    posic_nuevas = [0, 3, 6, 38, 41, 44, 45, 48, 51, 18,
                    21, 24, 9, 10, 11, 12, 14, 15, 16, 17]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("L'")


def U(cubo):

    posic_orig = [11, 10, 9, 38, 37, 36, 27, 28, 29, 18,
                  19, 20, 6, 3, 0, 7, 1, 8, 5, 2]
    posic_nuevas = [38, 37, 36, 29, 28, 27, 18, 19, 20, 9,
                    10, 11, 0, 1, 2, 3, 5, 6, 7, 8]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("U")


def U2(cubo):
    U(cubo)
    U(cubo)
    return("U2")


def Up(cubo):

    posic_orig = [29, 28, 27, 20, 19, 18, 9, 10, 11, 36,
                  37, 38, 2, 5, 8, 1, 7, 0, 3, 6]
    posic_nuevas = [38, 37, 36, 29, 28, 27, 18, 19, 20, 9,
                    10, 11, 0, 1, 2, 3, 5, 6, 7, 8]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("U'")


def D(cubo):

    posic_orig = [15, 16, 17, 24, 25, 26, 35, 34, 33, 2,
                  1, 0, 51, 48, 45, 52, 46, 53, 50, 47]
    posic_nuevas = [24, 25, 26, 33, 34, 35, 0, 1, 2, 15,
                    16, 17, 45, 46, 47, 48, 50, 51, 52, 53]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("D")


def D2(cubo):
    D(cubo)
    D(cubo)
    return("D2")


def Dp(cubo):

    posic_orig = [33, 34, 35, 2, 1, 0, 17, 16, 15, 24,
                  25, 26, 47, 50, 53, 46, 52, 45, 48, 51]
    posic_nuevas = [24, 25, 26, 33, 34, 35, 0, 1, 2, 15,
                    16, 17, 45, 46, 47, 48, 50, 51, 52, 53]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("D'")


def B(cubo):

    posic_orig = [35, 32, 29, 2, 1, 0, 15, 12, 9, 53,
                  52, 51, 42, 39, 36, 43, 37, 44, 41, 38]
    posic_nuevas = [2, 1, 0, 9, 12, 15, 53, 52, 51, 29,
                    32, 35, 36, 37, 38, 39, 41, 42, 43, 44]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("B")


def B2(cubo):
    B(cubo)
    B(cubo)
    return("B2")


def Bp(cubo):

    posic_orig = [9, 12, 15, 51, 52, 53, 29, 32, 35, 0,
                  1, 2, 38, 41, 44, 37, 43, 36, 39, 42]
    posic_nuevas = [2, 1, 0, 9, 12, 15, 53, 52, 51, 29,
                    32, 35, 36, 37, 38, 39, 41, 42, 43, 44]
    cubo_aux = cubo[:]

    for i in range(20):
        cubo[posic_nuevas[i]] = cubo_aux[posic_orig[i]]
    return("B'")


def mezcla_cubo(cubo):
    n = random.randint(30, 100)

    for movimiento in range(n):
        mov = random.choice([F, Fp, F2,
                             R, Rp, R2,
                             L, Lp, L2,
                             U, Up, U2,
                             D, Dp, D2,
                             B, Bp, B2])
        x = mov(cubo)
        # print(movimiento+1, ":", x)
        secuencia.append(x)
        # print_cubo(cubo)

    print("Total:", n, "movimientos.")
    print("Secuencia:", (" ".join(secuencia)))


def mover_cubo(cubo):
    while(1):
        print("Introduce el movimiento a realizar")
        print("F, F', F2, R, R', R2, L, L', L2")
        print("U, U', U2, D, D', D2, B, B', B2")
        codigo = input("O deja en blanco para salir: ")

        if(codigo == "F"):
            F(cubo)
            print_cubo(cubo)

        elif(codigo == "F'" or codigo == "F`" or codigo == "F´"):
            Fp(cubo)
            print_cubo(cubo)

        elif(codigo == "F2"):
            F2(cubo)
            print_cubo(cubo)

        elif(codigo == "R"):
            R(cubo)
            print_cubo(cubo)

        elif(codigo == "R'" or codigo == "R`" or codigo == "R´"):
            Rp(cubo)
            print_cubo(cubo)

        elif(codigo == "R2"):
            R2(cubo)
            print_cubo(cubo)

        elif(codigo == "L"):
            L(cubo)
            print_cubo(cubo)

        elif(codigo == "L'" or codigo == "L`" or codigo == "L´"):
            Lp(cubo)
            print_cubo(cubo)

        elif(codigo == "L2"):
            L2(cubo)
            print_cubo(cubo)

        elif(codigo == "U"):
            U(cubo)
            print_cubo(cubo)

        elif(codigo == "U'" or codigo == "U`" or codigo == "U´"):
            Up(cubo)
            print_cubo(cubo)

        elif(codigo == "U2"):
            U2(cubo)
            print_cubo(cubo)

        elif(codigo == "D"):
            D(cubo)
            print_cubo(cubo)

        elif(codigo == "D'" or codigo == "D`" or codigo == "D´"):
            Dp(cubo)
            print_cubo(cubo)

        elif(codigo == "D2"):
            D2(cubo)
            print_cubo(cubo)

        elif(codigo == "B"):
            B(cubo)
            print_cubo(cubo)

        elif(codigo == "B'" or codigo == "B`" or codigo == "B´"):
            Bp(cubo)
            print_cubo(cubo)

        elif(codigo == "B2"):
            B2(cubo)
            print_cubo(cubo)

        elif(codigo == ""):
            break

        else:
            print("Error en la entrada")


def main():
    print(__title__)
    while(1):
        print("Menú principal")
        print("\t1. Ver cubo")
        print("\t2. Mezcla aleatoria")
        print("\t3. Introducir cubo")
        print("\t4. Mover cubo")
        menu_principal = int(input("Selecciona una opción: "))

        if(menu_principal == 1):
            print("VER CUBO")
            print_cubo(cubo)

        elif(menu_principal == 2):
            print("MEZCLA ALEATORIA")
            mezcla_cubo(cubo)
            print_cubo(cubo)

        elif (menu_principal == 3):
            print("INTRODUCIR CUBO")

        elif (menu_principal == 4):
            print("MOVER CUBO")
            mover_cubo(cubo)

if __name__ == '__main__':
    cubo = inicia_cubo(cubo)
    main()
