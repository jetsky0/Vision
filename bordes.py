import sys,pygame
import Image
#from sys import argv
from math import*
import numpy
from time import*
import math

# python bordes.py gris.png

#Tomar como base la imagen obtenida en el programa de escala de grises, aplicar convolucion y detectar bordes en la imagen

def main():
    imagen = conv()

def conv():
    ima = Image.open("gris.png")
    imagen = ima.load()
    ancho,alto = ima.size
    mat_x = ([-1,0,1],[-2,0,2],[-1,0,1])
    mat_y = ([1,2,1],[0,0,0],[-1,-2,-1]) 
    for i in range(ancho):
        for j in range(alto):
            sumx=0.0
            sumy = 0.0
            for m in range(len(mat_x[0])):
                for h in range(len(mat_y[0])):
                    try:
                        mul_x= mat_x[m][h] * imagen[i+m, j+h][0]
                        mul_y= mat_y[m][h] * imagen[i+m, j+h][0]
                    except:
                        mul_x=0
                        mul_y=0
                    sumx=mul_x+sumx
                    sumy=mul_y+sumy
            valorx = pow(sumx,2)
            valory = pow(sumy,2)
            grad = int(math.sqrt(valorx + valory))
            if grad <= 0:
                grad = 0
            elif grad >= 255:
                grad = 255
            imagen[i,j] = (grad, grad, grad)
    nueva = 'bordes.png'
    otra = ima.save(nueva)
    return nueva

if __name__ == "__main__":
    main()
