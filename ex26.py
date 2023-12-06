produto = str(input("Insira o nome do produto: "))
quantidade = float(input("Digite a quantidade desejada: "))

refriPrecoInicial = 7
refri = quantidade * refri_preco_inicial


if quantidade <=5:
    print(refri - 2/100)
elif quantidade > 5 <=10:
    print(refri - 3/100)
elif quantidade > 10:
    print(refri - 5/100)

total = refri - desconto


str(print("Descrição: Refrigerante"))
float(print("quandidade: ", quantidade))
int(print("O preço unitário do produto é:", refri_preco_inicial))