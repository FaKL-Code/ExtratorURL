import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return f'{self.url}'
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
        
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")
        
        url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é válida.")
        
    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        return self.url[:indice_interrogacao]
    
    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        return self.url[indice_interrogacao+1:]
    
    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            return self.get_url_parametros()[indice_valor:]
        else:
            return self.get_url_parametros()[indice_valor:indice_e_comercial]
        
    def __eq__(self, other):
        return self.url == other.url
        
extrator_url = ExtratorURL("bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)
