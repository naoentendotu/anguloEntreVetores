# bibliotecas importadas
import numpy as np
import math
import matplotlib.pyplot as plt
import sys
import os

opcao = 'S'

while opcao == 'S':
    # receber vetores do usuário
    u = []
    for i in range(3):
        print('Digite o valor de u', i+1, ':')
        u.append(float(input()))
    v = []
    for i in range(3):
        print('Digite o valor de v', i+1, ':')
        v.append(float(input()))

    # calculo dos módulos
    mod1 = 0
    raiz1 = 0
    for i in range(3):
        raiz1 = (u[i]**2) + raiz1
        mod1 = np.sqrt(raiz1)

    mod2 = 0
    raiz2 = 0
    for i in range(3):
        raiz2 = (v[i]**2) + raiz2
        mod2 = np.sqrt(raiz2)

    # produto dos módulos
    prod_modulo = mod1 * mod2

    # produto dos vetores
    c_prod = []
    produto = 0
    for i in range(3):
        c_prod.append(u[i]*v[i])

    produto = sum(c_prod)

    # =====Calculo do Angulo=====#
    angulo = produto/prod_modulo
    angulo_graus = math.degrees(math.acos(angulo))

    # mostrar os vetores do usuário
    usem = str(u)[1:-1]
    vsem = str(v)[1:-1]

    print("Vetor u(", usem, ')')
    print("Vetor v(", vsem, ')')

    # mostrar o angulo entre os vetores
    print("θ =", '%.2f' % angulo_graus, '°')

# ======GRAFICO======#

    fig = plt.figure(figsize=(10, 10))
    ax = plt.axes(projection='3d')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_zlim([-10, 10])

    start = [0, 0, 0]
    ax.quiver(start[0], start[1], start[2], u[0], u[1], u[2])
    ax.quiver(start[0], start[1], start[2], v[0], v[1], v[2], color='red')

    plt.title('Ângulo entre vetores')
    plt.show()

    # voltar ao inicio do programa
    opcao = str(input('Deseja inserir novos valores? [S/N]')).upper().strip()
    if opcao == 'N':
        exit('Obrigada por utilizar programa!')
