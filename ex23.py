vel = int(input("Diga a velocidade do carro: "))
calculo_multa = vel - 80
res = calculo_multa * 5
if vel > 80:
    print("Multado em", res)
