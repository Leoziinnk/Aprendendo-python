# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 08:50:38 2023

@author: leona
"""
v1 = input("Insira a quantidade de votos do candidato 1: ")
v2 = input("Insira a quantidade de votos do candidato 2: ")
v3 = input("Insira a quantidade de votos do candidato 3: ")
v1_int = int(v1)
v2_int = int(v2)
v3_int = int(v3)

total_votos = v1_int + v2_int + v3_int 

porcentagem1= int((v1_int/total_votos)*100)
porcentagem2= int((v2_int/total_votos)*100)
porcentagem3= int((v3_int/total_votos)*100)

asterisco1 = '*' * int((porcentagem1/5))
asterisco2 = '*' * int((porcentagem2/5))
asterisco3 = '*' * int((porcentagem3/5))

print(asterisco1," ",porcentagem1,"%","\n",asterisco2," ",porcentagem2,"%","\n")
print(asterisco3," ", porcentagem3, "%")