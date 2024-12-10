def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem_2(nome):
    print(f"Bem Vindo, {nome}!")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Bem Vindo, {nome}!")

exibir_mensagem()
exibir_mensagem_2("Guilherme")
exibir_mensagem_3("Pedro")

def calcular_total(num):
    return sum(num)

def antecessor_sucessor(num):
    antecessor = num - 1
    sucessor = num + 1
    
    return antecessor, sucessor

print(calcular_total([2, 3, 5, 7, 11]))
print(antecessor_sucessor(10))

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    result = funcao(a, b)
    print(f"O resultado entre {a} e {b} é: {result}")

exibir_resultado(10, 10, somar)
