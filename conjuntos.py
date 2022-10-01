"""
- Conjuntos em qualquer linguagem de programação, estamos fazendo referencias a teoria dos conjuntos
da matematica.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Set  (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice. ou seja, conjuntos não são idexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preucupar
com chaves, valores e itens dúplicados.

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (set) e Mapas (Dicionários) em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

    # Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionad um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

dados = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]

# Listas aceitam valores duplicados, então temos 10 elementos
lista = list(dados)
print(f'Lista {lista} com {len(lista)}  elementos')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos')

# Dicionarios não aceitam chaves duplicados, entao temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')

# Conjunto não aceitam valores duplicados, entao temos 8 elementos
conjunto = set(dados)
print(f'Conjunto:  {conjunto} com {len(conjunto)} elementos')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu
# e os visitantes informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicasm, temos.

# O que você faria? Faria um loop na lista ... ?

# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
print(s)

# Revemover elementos em um conjunto
s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # NÃO é indice! Informamos o valor a ser devolvido

print(s)

# OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado

# Forma 2

s.discard(2)

print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado.

s = {1, 2, 3}
print(s)

# Copiando um conjunto para outro ...

# Forma 1 - Deep Copy

novo = s.copy()

novo.add(4)
print(novo)

# Forma 2 - Shallow Copy
novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos Matematicos de Conjuntos

# Imagine que temos dois conjuntos: um contendo estudantes do curso Pythone um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
#{'Marcos', 'Guilherme', 'Ellen', 'Gustavo', 'Pedro', 'Fernando', 'Ana', 'Patricia', 'Julia'}
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Veja que alguns alunos que estudam Python também estudam Java.

# Gerar um conjunto de estudantes que estão ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

# Soma*, Valor Máximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))  # Fazer a soma
print(max(s))  # Maximo Valor
print(min(s))  # Menor valor
print(len(s))  # Quantidade de elementos (largura)





