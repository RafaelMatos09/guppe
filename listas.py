"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem dinâmico e tambem de podermos colocar QUALQUER tipo de dado.

Linguagem C/Java: Arrays
  - Possuem tamanho e tipo de dado fixo:
  Ou seja, nestas linguagens se voçê criar uma array do tipo int e com tamanho 5, este array
  será SEMPRE do tipo inteiro e podera ter SEMPRE no maximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo: Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo: Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são apresentadas por colchetes: []

# Podemos facilmente checar se determinado valor está contido na lista

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', '', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

num = 18
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

# Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas


Para adicionar elementos em listas, utilizamos a função append


print(lista1)
lista1.append(42)
print(lista1)
#OBS: Com append, nós só conseguimos adicionar um elemento por vez
# lista1.append(12, 34, 56) # Erro

lista1.append([8, 3, 1])# Coloca a lista como elemento único (sublista)
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])# Coloca cada elemento da lista como valor adicional a lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição de indice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição de indice
# OBS: Isso não substitui o valor inicial. O mesmo será deslocado para a direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

#lista6 = lista1 + lista2
lista1.extend(lista2)
print(lista1)

# Podemos facilmente inverter uma lista

# Forma 1
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

# Forma 2
print(lista1[::-1])
print(lista2[::-1])

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista2))

# Podemos remover facilmente o ultimo elemento de uma lista
# OBS: O pop não somente remove o ultimo elemento mas tambem o retorna
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo indice
# OBS: Os elementos a direita deste indice serao deslocados para a esquerda.
# OBS: Se não houver elmento no indece informado, teremoos o erro IndexError
lista5.pop(2)
print(lista5)

# Podemos remover todos os elementos ( zerar a lista)
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrão, o split separa os elemenotos da linha pelo espaço entre elas

# Exemplo 2

curso = 'Programação,em, Python:, Essencial'
print(curso)
curso = curso.split(',')
print(curso)

# Convertendo uma lista em uma string

lista6 = ['Programação', 'em', 'Python', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

# Abaixo estamos falando: Pega a lista6, coloca $ entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

# Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados

lista6 = [1, 2.34, True, 'Geek', 'd', [1, 2, 3], 456673232]
print(lista6)
print(type(lista6))

# Iterando sobre listas

# Exemplo 1 - Utilizando for

soma = ''
for elemento in lista2:
    print(elemento)
    soma = soma + elemento
print(soma)

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variaveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

# Fazemos acesso aos elementos de forma indexada

#            0         1         2        3
cores = [ 'verde', 'amarelo', 'azul', 'branco']

print(cores[0]) # verde
print(cores[1]) # amarelo
print(cores[2]) # azul
print(cores[3]) # branco

#  Fazer acesso aos elementos de fora indexada
# Para entender melhor o indece negativo, pense na lista como um circulo,onde
# final de um elemento esta ligado ao inicio da lista

print(core[-1]) # branco
print(core[-2]) # azul
print(core[-3]) # amarelo
print(core[-4]) # verde
#print(core[-5]) # Erro, pois não exite indice 5

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

# Gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)

print(lista)

# Outros métodos não tão importantes mas tambem úteis

#  Encontrar o índice de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]

# Em qual indice da lista esta o valor 6?
print(numeros.index(6))

# Em qual indice da lista esta o valor 9?
print(numeros.index(9))

# print(numeros.index[19]) # Gera ValueError
# OBS: Caso não tenha este elemento na lista, será apresentando erro

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(5))

#Podemos fazer busca dedntro de um range, ou seja, qual indice começar a buscar
print(numeros.index(5, 1)) # buscando a partir do índice 1
print(numeros.index(5, 2)) # buscando a partir do índice 2
print(numeros.index(5, 3)) # buscando a partir do índice 3
#print(numeros.index(5, 4)) # buscando a partir do índice 4
# OBS: Caso não tenha este elemento na lista, será apresentando erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numero.index(8, 3, 6)) # Buscar o indice do valor 8, entre os indices 3 e 6

# Revisao do slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = ['1', '2', '3', '4']

print(lista[1:]) # Iniciando no indice 1 e pegando todos os elementos restantes

# Trabalhando com slice de lista com parâmetro 'fim'

print(lista[:2]) # começa em 0, pega té o indice 2 - 1

print(lista[:4]) # começa em 0, pega té o indice 4 - 1

print(lista[:3]) # começa em 1, pega té o indice 3 - 1

# Trabalhando com slice de lista com o parâmetro 'passo'

print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2

print(lista[::2])  # Começa em 0, vai até o final, de 2 em 2

# Ivertendo valores em uma lista

nomes = ['Geek', 'University']

nomes[0], nomes[0] = nomes[1], nomes[0]

print(nomes)

nomes = ['Geek', 'University']

nome.reverse()
print(nomes)

# Soma *, Valor Maximo*, Valor Minimoo*, Tamanho

# Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]

print(sum(lista)) # soma
print(max(lista)) # maximo valor
print(min(lista)) # minimo valor
print(len(lista)) # Tamanho da lista

# Transformar uma lista em tupla

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Descompacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferente de elementos na lista ou variaveis para receber os dados teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1

lista = [1, 2, 3]
print(lista)

nova = lista.copy()

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# Ficaram totalmente idependentes, ou seja, modificando uma lista, nao afeta a outra. Isso em
# Python é chamado de Deep Copy (Copia Profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista # Cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# apos realizar modifica~ao em uma das listas, essa modficação se refletiu em ambas as listas.
# isso em python é chamado de Shallow copy.

"""



