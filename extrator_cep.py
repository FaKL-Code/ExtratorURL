import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile(r"\d{5}-\d{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
