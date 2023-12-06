salario = int(input("Escreva o salário do funcionário: "))
aumento_10 = (salario*(10/100))+salario
aumento_15 = (salario*(15/100))+salario

if salario > 1250:
    print(aumento_10)
else:
    print(aumento_15)