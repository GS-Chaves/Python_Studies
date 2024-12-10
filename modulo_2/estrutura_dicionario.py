contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3333-2212"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3333-2121"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-1234"},
}

print(contatos["guilherme@gmail.com"]["telefone"]) # 3333-2221

carros = dict.fromkeys(["marca", "ano"], "vazio")

print(carros)

resultado = "idade" in contatos["guilherme@gmail.com"] # False
print(resultado)

resultado = "telefone" in contatos["guilherme@gmail.com"] # True
print(resultado)
