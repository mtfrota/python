"""
- Exercício 
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""

list = ['Maria', 'Helena', 'Luiz']
indices = range(len(list))
list.append('João')

for indice in indices:
    print(indice, list[indice], type(list[indice]))