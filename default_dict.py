"""
Módulo Collections - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionários

dicionario = {'curso': 'Programação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro'])  # ?? KeyErro

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que nao existe, essa chave será
criada e o valor default será atribuído.

OBS: Lamdas são funções sem nome, que podem ou não receber parametos de entrada
e retornar valores.
"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mais aqui não.

print(dicionario)