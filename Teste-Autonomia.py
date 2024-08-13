pot = consumo = voltagem = etot = 0

consumo = float(input('Digite o consumo da aeronave: '))
velocidade = float(input('Digite a velocidade da aeronave: '))

pot = consumo*24 #potencia = corrente * voltagem
etot = 22*24 #energia total = capacidade * voltagem

autonomia = etot/pot 
distancia = velocidade * autonomia
print(autonomia)
print(distancia)