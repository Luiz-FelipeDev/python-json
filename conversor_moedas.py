import json
from urllib.request import urlopen


with urlopen(" https://economia.awesomeapi.com.br/last/USD-BRL") as response:
    source = response.read()
    
    
data = json.loads(source)

def funcao_conversora():
    valor_conversao = float(input('Digite o valor em reais que deseja converter para dolar: '))
    valor_dolar = float(data['USDBRL']['bid'])
    dolares_americanos = valor_conversao/valor_dolar
    return '{:.2f}$'.format(dolares_americanos)
    
print(funcao_conversora())