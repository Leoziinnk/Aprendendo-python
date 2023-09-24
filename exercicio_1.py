# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 07:13:13 2023

@author: leoziinnk
"""
espetos= input("Insira quantos espetos foram vendidos: ")
preço_venda= input("Insira o preço da venda de cada espetinho:  ")
preço_carne = input("Insira o preço do kg da carne:  ")
 
espetos_int= int(espetos)
preço_venda_float = float (preço_venda)
preço_carne_float = float(preço_carne)

carne_kg = espetos_int * 0.2 
preço_carne_usada = carne_kg * preço_carne_float
valor_recebido = espetos_int * preço_venda_float
lucro = valor_recebido - preço_carne_usada

print("A quantidade de kg de carne utilizada foi: ", carne_kg,"kg\n")
print("O valor recebido pela venda dos espetos foi: ", valor_recebido,"\n")
print("O lucro das vendas foi de: ", lucro , "\n")