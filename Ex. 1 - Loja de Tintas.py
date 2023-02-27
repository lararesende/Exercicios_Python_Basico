#Faça um programa para uma loja de tintas. O programa deverá pedir o
#tamanho em metros quadrados da área a ser pintada. Considere que a
#cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é
#vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
#quantidades de latas de tinta a serem compradas e o preço total.
tamanho = input("Qual o tamanho, em metros quadrados, da área a ser pintada? ")
tamanho = tamanho.replace("m^2", "")
if tamanho.isdigit():
    tamanho = float(tamanho)
    litros = (tamanho / 3)
    latas = (litros / 18)
    if latas == round(latas):
        latas = latas
    else:
        latas = round(latas + 0.5)
    valor = latas*80
    valor = f'R${valor:_.2f}'
    valor = valor\
        .replace(".", ",")\
        .replace("_", ".")
    print(f'A quantidade de latas necessária será de {latas:.0f} latas, e o valor é de {valor} reais.')
else:
    print("Digite um tamanho válido")