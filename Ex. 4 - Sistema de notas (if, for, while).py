#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado).
#Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
notas = []
soma = 0
valores_acima_media = []
valores_abaixo_sete = []
while True:
    valor = input("Digite um valor: ")
    if valor == "-1":
        print("Fim. Até a próxima!")
        break
    else:
        valor = float(valor)
        notas.append(valor)
        while True:
            valor = input("Digite um valor: ")
            valor = float(valor)
            if valor == -1:
                break
            if valor != -1:
                notas.append(valor)
        for i in range(len(notas)):
            soma += notas[i]
        notas_inversas = notas[::-1]
        media = soma/(len(notas))
        for nota in notas:
            if nota > media:
                valores_acima_media.append(nota)
            if nota < 7:
                valores_abaixo_sete.append(nota)
        print("A quantidade de valores dados foi de:",len(notas))
        print("Os valores são: ", *notas)
        print("As notas inversas são: ")
        for notasinversas in (notas_inversas):
            print(notasinversas)
        print(f'A soma dos valores é: {soma}')
        print(f'A média dos valores é: {media:.2f}')
        print(f'Os valores acima da média são: {valores_acima_media}')
        print(f'Os valores abaixo de 7 são: {valores_abaixo_sete}')
        print("Fim. Até a próxima!")
        break