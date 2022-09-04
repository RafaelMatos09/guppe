"""
Loop for

Loop -> Estrutura de repetição
for -> Uma dessas estruturas

C ou Java

for(int i = 0; i < limitador; i++
  {
     //execução do loop
  }
Python

for item in interavel:
    //execuçao do loop

Utilizamos loops para iterar sobre sequencias ou sobre valores iteraveis

Exemplos de iteraveis:
- String
   nome = 'Geek University'
- Lista
    lista = [1, 2, 3, 4]
- Range
   numeros = range[1,10]

   #Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)


Enumerate:

(0, 'G'), (1, 'e'), (2, 'e'),  (3, 'k'), (4, ''), (5, 'U')...)

for indice, v in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor, podemos descartá-lo utilizando um nderline (_)

for valor in enumerate(nome):
    print(valor)

for n in range(1, qtd+1):
    print(f'imprimindo{n}')

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10) # Temos que transofrmar em uma lista


qtd = int(input('Quantas vezes esse loop deve rodar?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

https://apps.timwhitlock.info/emoji/tables/unicode

nome = 'Geek University'

for letra in nome:
     print(letra, end='')
"""

# Original: U+1f60D
# Modificado: U0001F60D


for _ in range(3):
    for num in range(1, 10):
        print(f'\U0001F60D' * num)
