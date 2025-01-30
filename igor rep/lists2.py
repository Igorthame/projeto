import random
lista=[]
lista2=[] 

lista= [random.randint(1, 100) for _ in range(10)]
lista2= [random.randint(1, 100) for _ in range(10)]

vetor3 = []

for i in range(3):
    for i in range(10):
     vetor3.append(lista[i])
     vetor3.append(lista2[i])

print("Vetor 1:", lista)
print("Vetor 2:", lista2)
print("Vetor 3 (intercalado intecalo 3 vezes):", vetor3)






