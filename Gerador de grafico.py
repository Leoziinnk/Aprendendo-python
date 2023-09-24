# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 09:15:15 2023

@author: leona
"""
import matplotlib.pyplot as plt

x=[]
y=[]
    
while True:     
   quantidade_dadosx= input("Insira a quantidade de dados x: ")
   quantidade_dadosy = input("Insira a quantidade de dados y: ")
       
   quantidade_dadosx_int= int(quantidade_dadosx)
   quantidade_dadosy_int= int(quantidade_dadosy)
       
   if(quantidade_dadosx_int==quantidade_dadosy_int):
         break;
   else:
        print("Erro: A quantidade de dados de x e y devem ser as mesmas")
            
for dadosx in range(quantidade_dadosx_int):
    dadosx_informados = input("Insira o dado de x: ")
    dadosx_informados_int = int (dadosx_informados)
    x.append(dadosx_informados_int)
                  
for dadosy in range (quantidade_dadosy_int):
    dadosy_informados = input("Insira o dado de y: ")
    dadosy_informados_int = int(dadosy_informados)
    y.append(dadosy_informados_int)
   
plt.plot(x,y)
plt.title("Gráfico")
plt.xlabel("Eixo x")
plt.ylabel("Eixo Y")
plt.show()