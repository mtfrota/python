# Introdução a f-strings
# serve praticamente pra deixar 
# o codigo mais formatado, mais bonitinho

nome = 'Mateus Frota'
altura = 1.75
peso = 92
imc = peso / (altura * 2)

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} quilos e seu IMC é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)




