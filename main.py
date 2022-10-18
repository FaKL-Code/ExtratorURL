url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'

print(url)

interrogacao = url.find('?')

url_base = url[:interrogacao]
print(url_base)

url_parametros = url[interrogacao + 1:]
print(url_parametros)