# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  M a t e u s
# -6-5-4-3-2-1

# nome = 'Mateus'
# # print(nome[2])
# # print(nome[-4])
# print('t' in nome)
# print('z' in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')
    
