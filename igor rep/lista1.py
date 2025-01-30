import random

ve1 = [random.randint(1, 100) for _ in range(10)]
ve2 = [random.randint(1, 100) for _ in range(10)]

v3 = []


for i in range(10):
    v3.append(ve1[i])
    v3.append(ve2[i])


print("Vetor 1:", ve1)
print("Vetor 2:", ve2)
print("Vetor 3 (intercalado):", v3)
