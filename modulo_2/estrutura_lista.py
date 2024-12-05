lista = ["maça","banana", "uva"]
lista = []

letras = list("Python")
numeros = list(range(10))

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz[0] # retorna [1, 2, 3]
matriz[0][0] # retorna [1]
matriz[-1][-1] # retorna [9]

lista = ["p", "y", "t", "h", "o","n"]

lista[2:] # ["t", "h", "o","n"]
lista[:2] # ["p", "y"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o","n"]
lista[::-1] # ['n', 'o', 'h', 't', 'y', 'p']

carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
quadrados = [numero ** 2 for numero in numeros]