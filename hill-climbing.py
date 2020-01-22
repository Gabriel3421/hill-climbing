
from random import randint
import time


import math

#formula dada no problema
def formula(x, y):
    return abs(x*math.sin(y*math.pi/4) + y*math.sin(x*math.pi/4))
#cria o vetor estado baseado no valor da formula e no x e y coletados
def estado(x,y):
    estado_atual = list()
    estado_atual.append(formula(x,y))
    estado_atual.append(x)
    estado_atual.append(y)
    return estado_atual
'''
Comparando todos os vizinhos do ponto atual onde a funçao está;
o metodo sorted() ordena os vetores em ordem crescente logo a ultima posiçao tem o maior valor e foi usado
bastante para organizar e retornar o maior valor que é para onde o algoritmo deve seguir
'''
def comp_y(x,y):
    estados = list()
    estados.append(estado(x,y+0.01))
    estados.append(estado(x,y-0.01))
    return sorted(estados)[1]

def comp_x(x,y):
    estados = list()
    estados.append(estado(x+0.01,y))
    estados.append(estado(x-0.01,y))
    return sorted(estados)[1]
 
def comp_x_y(x,y):
    estados = list()
    estados.append(estado(x+0.01,y+0.01))
    estados.append(estado(x-0.01,y+0.01))
    estados.append(estado(x+0.01,y-0.01))
    estados.append(estado(x-0.01,y-0.01))
    return sorted(estados)[3]
#compara todos os resultados e retorna o maior ou seja para onde o algoritmo deve ir
def comp_all(x,y):
    maior = list()
    maior.append(comp_x_y(x,y))
    maior.append(comp_x(x,y))
    maior.append(comp_y(x,y))
    return sorted(maior)[2]

estado_futuro =list() 
maior_estado = [0,0,0]

while(1):
    print("*________________________________*")
    #Gerando x e y aleatorio
    x=randint(0,20)
    y=randint(0,20)
    estado_atual = estado(x,y)
    #mostra como está iniciando o hill climbing
    print("Valor inicial: " + str(estado_atual[0])+ ", com x = "
        + str(estado_atual[1])+"e y = "+str(estado_atual[2]))
    k = 0
    while(1):
        estado_futuro = comp_all(estado_atual[1],estado_atual[2])
        if(estado_futuro[0] > estado_atual[0]):
            if estado_futuro[1] > 20:
                estado_futuro[1] = 20
            if estado_futuro[2] > 20:
                estado_futuro[2] = 20    
            estado_atual = estado_futuro
        else:
            if estado_atual > maior_estado:
                maior_estado = estado_atual
            break
        k= k +1
    #mosta o maior valor da iteraçao       
    print("Max: " + str(estado_atual[0])+ ", com x = "
        + str(estado_atual[1])+"e y = "+str(estado_atual[2]))
    #mostra o maior valor encontrado
    print("Max_tot: " + str(maior_estado[0])+ ", com x = "
        + str(maior_estado[1])+"e y = "+str(maior_estado[2]))
    #para melhor acompanhar vizualmente coloquei um sleep mas pode ser retirado para maior velocidade de resposta
    #time.sleep(3)
    '''
    SE VC QUISER ACHAR O MAXIMO DA FUNÇAO DEIXE FUNCIONANDO INFINITAMENTE ATÉ O MAIOR VALOR SE REPETIR MAIS
    Q 10 OU 100 VEZES NO MEU CASO FIZ ISSO E ACHEI O VALOR MAX DE 36.08965117434066  ENTAO POSSO MANDAR PARAR
    QUANDO CHEGAR NESSE VALOR
    '''
    if maior_estado[0] == 36.08965117434066:
       break

