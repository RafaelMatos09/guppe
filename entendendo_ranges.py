"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges sao utilizados para gerar sequencias numericas, nao de forma aleatoria,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada nao inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo forma 1

for num in range(11):
    print(num)

# forma 2
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada nao inclusive (inicio padrão 0, e passo de 1 em 1)

# Exemplo forma 2
for num in range(1, 11):
    print(num)

# Forma 3

ramge(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo forma 3
for num in range(5, 55, 2):
    print(num)

# Forma 4 (Inversa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada nao inclusive (inicio especificado pelo usuario, e passo especificado pelo usuario)

#Exemplo forma 4
for num in range(10, 0, -1):
    print(num)
"""
# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)