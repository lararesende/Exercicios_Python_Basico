
cpf_digitado = input("Digite um cpf: ")
cpf_digitado = cpf_digitado\
    .replace(".", "") \
    .replace("-", "") \
    .replace(" ", "")
entrada_e_sequencial = cpf_digitado == cpf_digitado[0] * len(cpf_digitado)
if cpf_digitado.isdigit() and entrada_e_sequencial == False:
    if len(cpf_digitado) == 11:
        digitos=cpf_digitado[0:9]
        digitos_separados = list(digitos)
        a, b, c, d, e, f, g, h, i = (digitos_separados)
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        e = int(e)
        f = int(f)
        g = int(g)
        h = int(h)
        i = int(i)
        soma1= (10*(a*10 + b*9 + c*8 + d*7 + e*6 + f*5 + g*4 + h*3 + i*2))%11
        if soma1 < 10:
            decimo_digito = soma1
        else:
            decimo_digito = 0

        j = decimo_digito
        soma2 = soma1= (10*(a*11 + b*10 + c*9 + d*8 + e*7 + f*6 + g*5 + h*4 + i*3 + j*2))%11
        if soma2 < 10:
            decimo_primeiro_digito = soma2
        else:
            decimo_primeiro_digito = 0
        if int(cpf_digitado[9]) != decimo_digito or int(cpf_digitado[10]) != decimo_primeiro_digito or len(cpf_digitado) != 11:
            print("O cpf digitado não é válido")
        else:
            print(f'O cpf digitado é valido.')
    else:
        print("O número digitado não é um cpf")
else:
    print("O cpf digitado é inválido")
"""
ou

cpf = input("Digite um cpf: ")
cpf = cpf\
    .replace(".", "") \
    .replace("-", "") \
    .replace(" ", "")
entrada_e_sequencial = cpf == cpf[0] * len(cpf)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
nove_digitos = cpf[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito_1 in nove_digitos:
    resultado_digito_1 += int(digito_1) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
print(digito_1)
digito_1str=str(digito_1)

contador_regressivo_2 = 11
dez_digitos=nove_digitos + digito_1str
resultado_digito_2 = 0
for digito_2 in dez_digitos:
    resultado_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
print(digito_2)

if int(cpf[9]) != digito_1 or int(cpf[10]) != digito_2:
    print("O cpf digitado não é válido")
else:
    print("O cpf é válido")
"""
