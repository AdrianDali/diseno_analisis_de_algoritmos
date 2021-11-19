from matplotlib import pyplot as plt
import random
import math

import matplotlib

# def funcion_distancia_dos_puntos( x1, x2,  y1, y2):
#   print(pow((x2-x1),2 ))
#  resultado = math.sqrt((pow(((x2-x1)),2))+(pow(((y2-y1)),2)))
# return resultado


def distancia(p1, p2):  # pare p1=[100, 34] p2=[27, 37]
    dis = math.sqrt((pow(((p2[0]-p1[0])), 2))+(pow(((p2[1]-p1[1])), 2)))
    return dis


if __name__ == "__main__":
    pares = []
    print(distancia([100, 34], [27, 37]))
    #draw_circle = plt.Circle((0.5, 0.5), 0.3,fill=False)

    for i in range(20):
        pares.append([random.randint(1, 100), random.randint(1, 100)])
    print(pares)


    for par in pares:
        plt.scatter(par[0], par[1], s=3, c="k")


    menor = 99999
    d = 0
    par_menor = []
    for i in range(len(pares)):
        for j in range(len(pares)):
            d = distancia(pares[i], pares[j])
            if d < menor and d != 0.0:
                menor = d
                par_menor.clear()
                par_menor.append(pares[i])
                par_menor.append(pares[j])
               
          
    print(menor)
    print(par_menor[0], par_menor[1])
    circle1 = plt.Circle((par_menor[0]),color = 'r', fill=False)
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_patch(circle1)
    plt.show()