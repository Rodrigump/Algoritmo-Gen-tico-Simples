import os
import random

letras = "AaBbCcDdEeFfGhHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz .!?,"
palavra = input()
no_pop = 10
crossover = 0.7
mutacao = 0.01

def calcula_fitness (individuo):
    soma = 0
    for i in range(len(individuo)):
        if(individuo[i] == palavra[i]):
            soma=soma+1
    return (soma / len(individuo))

def gera_individuo ():
    a = []
    for i in range(len(palavra)):
        aux = random.randint(0,len(letras)-1)
        a.append(letras[aux])
    return a

def getMelhor():
    aux = -1
    index = 0
    for i in range(no_pop):
        if(fitnesses[i] > aux):
            aux = fitnesses[i]
            index = i
    return index

populacao = []
fitnesses = []

def imprime(v, w):
    for i in range(len(v)):
        print(v[i],end="",flush=True)
    print("\t",w)

for i in range(no_pop):
    ind = gera_individuo()
    populacao.append(ind)
    fitnesses.append(calcula_fitness(ind))
    
def roleta(fitpop):
    soma = 0
    for i in range(len(fitpop)):
        soma = soma + fitpop[i]
    valor = soma * random.uniform(0,1)
    for i in range(len(fitpop)):
        valor = valor - fitpop[i]
        if(valor < 0):
            return i
    
    return len(fitpop)-1

def genetico ():
    global populacao
    global fitnesses
    retorno = fitnesses[getMelhor()]
    imprime(populacao[getMelhor()], fitnesses[getMelhor()])
    novapop = []
    novafitness = []
    while(len(novapop) < no_pop):
        pai1 = populacao[roleta(fitnesses)]
        pai2 = populacao[roleta(fitnesses)]
        filho1 = []
        filho2 = []
        prob_co = random.uniform(0,1)
        if(prob_co < crossover):
            mascara = []
            for i in range(len(pai1)):
                mascara.append(random.randint(0,1))
            for i in range(len(pai1)):
                if(mascara[i]==0):
                    filho1.append(pai1[i])
                    filho2.append(pai2[i])
                else:
                    filho1.append(pai2[i])
                    filho2.append(pai1[i])
        else:
            filho1 = pai1
            filho2 = pai2
        for i in range(len(filho1)):
            prob_mut = random.uniform(0,1)
            if(prob_mut < mutacao):
                index = random.randint(0,len(palavra)-1)
                letra = palavra[index]
                filho1[i] = letra 
        for i in range(len(filho2)):
            prob_mut = random.uniform(0,1)
            if(prob_mut < mutacao):
                index = random.randint(0,len(palavra)-1)
                letra = palavra[index]
                filho2[i] = letra 
                
        novapop.append(filho1)
        novafitness.append(calcula_fitness(filho1))
        novapop.append(filho2)
        novafitness.append(calcula_fitness(filho2))
    populacao = novapop
    fitnesses = novafitness
    return retorno
    
i=1
parada = 0
while((i<1000000) and (parada < 1.000)):
    it = str(i) + "\t"
    print(it,end="",flush=True)
    parada = genetico()
    i=i+1

os.system("pause")