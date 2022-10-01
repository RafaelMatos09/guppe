"""
Módulo Collection - Counter {Contador}

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Counter que é
parecido com um dicionario, contendo como chave o elemento da lista passada como parâmetro e como valor a
quantidade de ocorrencias desse elemento.

# Realizando o import

from collections import Counter
# Podemos utilizar qualquer iterável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 1, 1, 1, 4, 4, 4, 4, 5, 5, 5, 43]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)
# Counter({1: 6, 3: 4, 4: 4, 2: 3, 5: 3, 43: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como o valor a quantidade de ocorências

# Exemplo 2

rint(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

# Realizando o import

from collections import Counter

# Exemplo 3

texto = """Next.js é uma estrutura da web de desenvolvimento front-end React de código aberto criada por Vercel que 
permite funcionalidades como renderização do lado do servidor e geração de sites estáticos para aplicativos da web 
baseados em React. """

palavras = texto.split()

#print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

