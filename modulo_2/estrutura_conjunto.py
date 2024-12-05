numeros = {1, 2, 3, 4, 5, 6}

numeros = list(numeros)

print(numeros[0])

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)
conjunto_b.difference(conjunto_a)
conjunto_a.symmetric_difference(conjunto_b)
