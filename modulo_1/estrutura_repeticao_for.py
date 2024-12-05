texto = input("Digite um texto qualquer: ")
AEIOU = "AEIOU"

for letra in texto:
   if letra.upper() in AEIOU:
       print(letra, end=" ")

print()

for numero in range(11):
    print(numero, end=" ")
else:
    print()

for numero in range(0, 91, 9):
    print(numero, end=" ")

print()

for numero in range(1, 101):
    if numero % 2 == 0:
        continue
    print(numero, end=" ")
