# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
cond = 's'

while (cond != 'n'):
    num = input("digite um numero e obtenha a tabuada\n")
    num_int = int(num)
    
    for i in range(11):
       res = num_int*i
       print(num, "x", i, "=", res)
    
    cond = input("deseja obter outra tabuada?\n 's' 'n' \n")
    
if(cond == 'n'):
    print("programa encerrado!")   