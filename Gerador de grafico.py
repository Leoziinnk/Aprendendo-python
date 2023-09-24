# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 09:15:15 2023

@author: leoziink
"""
import matplotlib.pyplot as plt

x=[]
y=[]
    
while True:     
   quantidade_coordenadasx= input("Insira a quantidade de coordenadas x: ")
   quantidade_coordenadasy = input("Insira a quantidade de coordenadas y: ")
       
   quantidade_coordenadasx_int= int(quantidade_coordenadasx)
   quantidade_coordenadasy_int= int(quantidade_coordenadasy)
       
   if(quantidade_coordenadasx_int==quantidade_coordenadasx_int):
         break;
   else:
        print("Erro: A quantidade de coordenadas de x e y devem ser as mesmas")
            
for coordenadasx in range(quantidade_coordenadasx_int):
    coordenadasx_informados = input("Insira a coordenada de x: ")
    coordenadasx_informados_int = int (coordenadasx_informados)
    x.append(coordenadasx_informados_int)
                  
for coordenadasy in range (quantidade_coordenadasy_int):
    coordenadasy_informados = input("Insira o dado de y: ")
    coordenadasy_informados_int = int(coordenadasy_informados)
    y.append(coordenadasy_informados_int)
   
plt.plot(x,y)
plt.title("Gráfico")
plt.xlabel("Eixo x")
plt.ylabel("Eixo Y")
plt.show()
