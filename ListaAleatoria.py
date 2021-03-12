import random

lista = [0]  * 40
for i in range(0,40,1):
    lista[i] = random.randint(0, 1000)

print(lista)