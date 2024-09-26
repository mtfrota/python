"""
CONSTANTE = "Variáveis" que não vão mudar
muitas condições no mesmo if (ruim)
        < - COntagem de complexidade (ruim)
"""

velocidade = 60 # velocidade atual do carro
local_carro = 100 # local em que o carro está na estrada

RADA_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGER = 1 # A distância onde o radar pegar

VEL_CARRO_PASS_RADAR_1 = velocidade > RADA_1

if VEL_CARRO_PASS_RADAR_1:
    print('Velocidade carro passou do radar 1 ')

if local_carro >= (LOCAL_1 - RADAR_RANGER) and local_carro <= (LOCAL_1 + RADAR_RANGER) and velocidade > RADA_1:
    print('Carro multado em radar 1') 


