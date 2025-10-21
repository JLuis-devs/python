from math import factorial

from scipy.optimize import bracket

Ex036 = "Exercício 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.\n Pergunte o\
valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do\
salário ou então o empréstimo será negado."
Ex037 = "Exercício 037: Escreva um programa em que leia um número inteiro qualquer e peça para o usuário \
escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal."
Ex038 = "Exercício 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:\
– O primeiro valor é maior\n– O segundo valor é maior\n– Não existe valor maior, os dois são iguais"
Ex039 = "Exercício 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,\
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.\
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."
Ex040 = "Exercício 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:"
Ex041 = "Exercício 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:"
Ex042 = "Exercício 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:"
Ex043 = "Exercício 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:"
Ex044 = "Exercício 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:"
Ex045 = "Exercício 045: Crie um programa que faça o computador jogar Jokenpô com você."
Ex046 = "Exercício 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles."
Ex047 = "Exercício 047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50."
Ex048 = "Exercício 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500."
Ex049 = "Exercício 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for."
Ex050 = "Exercício 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o."
Ex051 = "Exercício 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão."
Ex052 = "Exercício 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo."
Ex053 = "Exercício 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços."
Ex054 = "Exercício 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores."
Ex055 = "Exercício 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos."
Ex056 = "Exercício 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos."
Ex057 = "Exercício 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto."
Ex058 = "Exercício 058: Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."
Ex059 = "Exercício 059: Crie um programa que leia dois valores e mostre um menu na tela:"
Ex060 = "Exercício 060: Faça um programa que leia um número qualquer e mostre o seu fatorial."
Ex061 = "Exercício 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while."
Ex062 = "Exercício 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos."
Ex063 = "Exercício 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci."
Ex064 = "Exercício 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)."
Ex065 = "Exercício 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores."
Ex066 = "Exercício 066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag)."
Ex067 = "Exercício 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."
Ex068 = "Exercício 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."
Ex069 = "Exercício 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:"
Ex070 = "Exercício 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:"
Ex071 = "Exercício 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues."
Inout = f"{'#'*100}\n"

Resp = "\nRESPOSTA:\n"

#--------------------------------------------------------------------------------------------------------------------------------------
# EXERCISES ONE WORLD
#---------------------------------------------------------------------------------------------------------------------------------------#
Fim = 1
while Fim != 0:
    n = int(input('\nDigite de 36 a 71 para ver os exercícios ou 0 para encerrar\nQual Exercício executar? '))
    if n == 0:
        print("Volte Sempre!")
        Fim = 0
    elif 36<= n <= 71:
        match n:
            case 36:
                print(Inout, Inout, Ex036, Inout, Inout, Resp)
                def iniciar():
                 def valor(mensagem,tipo):
                    while True:
                        try:
                            entrada = tipo(input(mensagem))
                            if entrada != 0:
                                return a
                            else:
                                print("Zero não é válido")
                                continue
                        except ValueError:
                            print("valor invalido")

                 nome1 = valor("Qual o seu nome: ", str)
                 nome1 = nome1.capitalize()
                 casa = valor(f"Qual valor da casa, {nome1}? ",float)
                 sal = valor(f"{nome1}, qual o seu salário? ",float)
                 anos = valor(f"Em quantos anos pretende pagar, {nome1}? ",int)


                 def verificador():
                    regra = casa/(12*anos)
                    if regra <= sal*0.3:
                        print(f"Empréstimo aprovado, parcela R$ {regra:.2f}")
                    else:
                        print(f"Empréstimo negado, aumente o numero de anos para {casa/(12*sal*0.3):.2f} ou diminua o valor da casa!")
                    if input("Simular um novo Empréstimo? (S/N): ").upper() == "S":
                        iniciar()
                    else:
                        print("Volte sempre!")
                 verificador()
                iniciar()
            case 37:
                print(Inout, Inout, Ex037, Inout, Inout, Resp)
                while True:
                    try:
                        numero_base = int(input("Digite um número: "))
                        print("Opções de conversão: \n1 para binário,\n2 para octal\n3 para hexadecimal.")
                        base = int(input("Qual base de conversão desejada: "))
                        base_nome =["binário","octal","hexadecimal"]
                        if base == 1:
                            numero_conv = bin(numero_base)
                        elif base == 2:
                            numero_conv = oct(numero_base)
                        elif base == 3:
                            numero_conv = hex(numero_base)
                        else:
                            print("Entrada invalida")
                            continue
                        print(f"O número {numero_base} na base {base_nome[base-1]} é {numero_conv[2:]}")
                        break
                    except ValueError:
                        print("Digite um número inteiro!")
            case 38:
                print(Inout,Inout,Ex038,Inout,Inout,Resp)
                Num1 = int(input("Digite o primeiro numero: "))
                Num2 = int(input("Digite o segundo numero: "))
                if Num1 == Num2:
                    print("Os dois valores são iguais")
                elif Num1>Num2:
                    print("O Primeiro valor é maior")
            case 39:
                print(Inout,Inout,Ex039,Inout,Inout,Resp)
                import datetime
                while True:
                    try:
                        ano_nascimento = int(input("Digite um ano: "))
                        ano_atual = datetime.date.today().year
                        alistamento = ano_atual - ano_nascimento
                        if ano_nascimento > ano_atual:
                            print(f"Digite um ano inferior ou igual a {ano_atual}")
                            continue
                        elif alistamento <18:
                            print(f"Você ainda não poderá se alistar, falta {18-alistamento} anos para o alistamento.")
                        elif alistamento >18:
                            print(f"Você deveria ter se alistado a {alistamento-18} anos atrás.")
                        else:
                            print("É hora de se alistar")
                        break

                    except ValueError:
                        print("Digite um número!")
                        continue
            case 40:
                print(Inout,Inout,Ex040,Inout,Inout,Resp)
                while True:
                    try:
                        av1 = float(input("Digite a 1° nota: "))
                        av2 = float(input("Digite a 2° nota: "))
                        media = (av1+av2)/2
                        if av1 < 0 or av2 < 0:
                            print("Digite um Valor maior ou igual a zero!")
                            continue
                        elif media >= 7:
                            resultado = "Aprovado"
                        elif media >= 5.0:
                            resultado = "Recuperação"
                        else:
                            resultado = "Reprovado"
                        print(f"Você foi {resultado} com média {media}")
                    except ValueError:
                        print("Digite um número")
                    print("Calcular média de outro aluno?\n( S para continuar ou Qualquer Tecla para sair)")
                    if input("Resposta: ").upper() != "S" != "Sim":
                        break
            case 41:
                print(Inout,Inout,Ex041,Inout,Inout,Resp)

                def funcao_idade():
                    while True:
                        try:
                            idade = int(input('Digite a idade: '))
                            if idade <= 0:
                              print("Digite uma idade maior que 0")
                              continue
                            elif idade <= 9:
                                categoria = "Mirim"
                            elif idade <= 14:
                                categoria = "Infantil"
                            elif idade <= 19:
                                categoria = "Júnior"
                            elif idade <= 25:
                                categoria = "Sênior"
                            else:
                                categoria = "Master"
                            print(f"Categoria é {categoria}")
                            break
                        except ValueError:
                            print("Entrada inválida!")
                            continue


                funcao_idade()
            case 42:
                print(Inout,Inout,Ex042,Inout,Inout,Resp)
                lado =[]
                for a in range(3):
                    while True:
                        try:
                            medida = float(input(f"Qual medida do {a+1} lado: "))
                            if medida <= 0:
                                print("Digite um número maior que zero")
                                continue
                            else:
                                lado.append(medida)
                                break
                        except ValueError:
                            print("Entrada invalida, digite um número maior que zero.")
                            continue

                lado.sort()
                triangulo = "Isósceles"
                if lado[0]+lado[1]>lado[2]:
                    if lado[0] == lado[1] == lado[2]:
                        triangulo = "Equilátero"
                    elif lado[0] != lado[1] != lado[2]:
                        triangulo = "Escaleno"
                    print(f"É um triangulo do tipo {triangulo}")
                else:
                    print("Não forma triângulo")
            case 43:
                print(Inout,Inout,Ex043,Inout,Inout,Resp)
                while True:
                    try:
                        peso=float(input("Qual o seu peso em Kg?  "))
                        altura=float(input("QUal a sua altura em centímetro: "))
                        if peso <=0 or altura <= 0:
                            print("Digite um número maior que zero")
                            continue
                        imc = peso / ((altura / 100) ** 2)

                    except ValueError:
                        print("Entrada invalida, digite um número maior que zero")
                        continue
                    resultado = "Erro"
                    maior = 24.9 * ((altura / 100) ** 2)
                    menor = 18.5 * ((altura / 100) ** 2)

                    if imc < 18.5:
                        resultado = "Abaixo do peso!"
                    elif 18.5 <= imc < 25:
                        resultado = "Peso ideal!"
                    elif 25 <= imc < 30:
                        resultado = "Sobrepeso!"
                    elif 30 <= imc < 40:
                        resultado = "Obesidade!"
                    else:
                        resultado = "Obesidade Mórbida!"
                    print(f"O seu IMC é {imc:.2f} e seu status é: {resultado}")
                    print(f"Seu peso ideal é entre {menor:.2f} kg até {maior:.2f} kg")

                    if input("Deseja ver outro resultado? (S - Sim ) ").upper() != "S":
                        break
            case 44:
                print(Inout,Inout,Ex044,Inout,Inout,Resp)
                while True:
                    try:
                        produto = float(input("Qual valor do produto? R$ "))
                        if produto <= 0:
                            print("Entrada invalida digite um valor maior que zero!")
                            continue
                    except ValueError:
                        print("Entrada invalida digite um número maior que zero!")
                        continue
                    def forma_pag():
                        print("Formas de Pagamento: ")
                        print("Digite 0 para à vista dinheiro/cheque: 10% de desconto")
                        print("Digite 1 para à vista no cartão: 5% de desconto")
                        print("Digite 2 para 2x no cartão: preço formal")
                        print("Digite o numero de parcelas que deseja no cartão, com taxa de 20% de juros ")
                        while True:
                            try:
                                forma_pagamento = int(input("Qual a forma de pagamento? "))
                                credito = "credito"
                                if forma_pagamento == 0:
                                    juros = 0.9
                                    forma_pagamento = 1
                                    credito ="Avista"
                                elif forma_pagamento == 1:
                                    juros =  0.95
                                elif forma_pagamento == 2:
                                    juros = 1
                                elif forma_pagamento >= 3:
                                    juros = 1.2
                                else:
                                    print("Entrada invalida escolha uma das opções.")
                                    continue

                                print(f"O valor do produto ficará: {produto*juros} ")
                                print(f"Número de x{forma_pagamento} parcelas de {produto*juros/forma_pagamento}, {credito}.")
                                if input("Deseja mudar a forma de Pagamento? (S - continua): ").upper() == "S":
                                    break
                            except ValueError:
                                print("Entrada invalida, digite um número de 1 a 4!")
                                continue

                    forma_pag()

                    if input("Digite S para simular um novo valor: ").upper() != "S":
                        break
            case 45:
                import random
                print(Inout,Inout,Ex045,Inout,Inout,Resp)
                Jogar = "Y"
                while Jogar == "Y":
                    n = random.randint(0,2)
                    jogo = ["Papel","Pedra","Tesoura"]
                    print("Bem vindo ao Jokenpô!")
                    print("Regras:")
                    print(" 1° regra: Pedra vence Tesoura")
                    print(" 2° regra: Papel vence Pedra")
                    print(" 3° regra: Tesoura vence Papel")
                    print("Já fiz minha escolha!")
                    print("Faça sua escolha digitando o número ou nome:")
                    print(" 1  -  Papel\n  2  -  Pedra\n  3  -  Tesoura")
                    while True:
                        escolha = input("Qual opção você escolhe: ")

                        #tratamento
                        if  escolha.isnumeric() and 0<int(escolha)<4:
                             escolha = jogo[int(escolha)-1]
                        elif escolha.capitalize() in jogo:
                            escolha = escolha.capitalize()
                        else:
                            print("Valor inválido")
                            continue
                        print("Minha escolha foi: ", jogo[n])

                        if escolha == jogo[n]:
                            print("Empatamos!")
                        else:
                            match (escolha,jogo[n]):
                                case ("Pedra","Tesoura") | ("Tesoura","Papel")|("Papel","Pedra"):
                                    print(f"{escolha} ganha de {jogo[n]}!")
                                    print("Parabéns você Ganhou")
                                case _:
                                    print(f"{jogo[n]} ganha de {escolha}!")
                                    print("Eu ganhei")
                        break
                Jogar = input("Jogar novamente? (Y - continua): ").upper()
            case 46:
                print(Inout,Inout,Ex046,Inout,Inout,Resp)
                from time import sleep
                for a in range(10,-1,-1):
                    print(a)
                    sleep(1)
                print("Acabou seu tempo!")
            case 47:
                print(Inout,Inout,Ex047,Inout,Inout,Resp)
                lista = []
                for n in range(2,50,2):
                    lista.append(n)
                print(lista)
            case 48:
                print(Inout,Inout,Ex048,Inout,Inout,Resp)
                indic = 1
                somaTotal = 0
                while True:
                    numero = 3 * indic
                    if numero <= 500 :
                        somaTotal = somaTotal + numero
                        indic = indic + 1
                    else:
                        break
                print(f"O valor da soma é {somaTotal}.")
                print(f"O valor da soma é {indic}.")
                print(f"O valor da soma é {numero}.")
            case 49:
                print(Inout,Inout,Ex049,Inout,Inout,Resp)
                def tabuada():
                    while True:
                        print("Tabuada")
                        num = int(input("Digite o numero: "))
                        for n1 in range(10):
                            print(f"{num} + {n+1:2} = {num+(n+1):2})", end="    |    ")
                            print(f"{num} - {n+1:2} = {num-(n+1):2})", end="    |    ")
                            print(f"{num} X {n+1:2} = {num*(n+1):4})", end="    |    ")
                            print(f"{num} / {n+1:2} = {num/(n+1):.2f}", end="    |    ")
                        if input("Deseja a tabuada de outro número? (S - Sim)").upper() != "S":
                            break

                tabuada()
            case 50:
                print(Inout,Inout,Ex050,Inout,Inout,Resp)
                soma = 0
                for n in range(6):
                    while True:
                        try:
                            digite = int(input(f"Digite o {n+1}° número: "))
                            if digite % 2 == 0:
                                soma = soma + digite
                            break

                        except ValueError:
                            print("Entrada invalida")
                print(f"A soma dos número pares é: {soma}")
            case 51:
                print(Inout,Inout,Ex051,Inout,Inout,Resp)
                while True:
                    PA = []
                    try:
                        primeiro_termo = int(input("Digite o primeiro termo: "))
                        raz = int(input('Digite o valor da razão: '))

                        for n2 in range(10):
                            a = int(primeiro_termo + n * raz)
                            PA.append(a)
                        print(f"Progressão Aritmética - PA: {PA}")
                    except ValueError:
                        print("Valor invalido digite número inteiro")
                        continue
                    if input("Deseja continuar? ( S - Continue) ").upper() != "S":
                        break
            case 52:
                print(Inout,Inout,Ex052,Inout,Inout,Resp)
                def numeroprimo():
                    while True:
                        num =int(input("Digite o número: "))
                        primo = "não é primo"
                        div = []
                        limite = int(num ** 0.5)
                        for n3 in range(1,limite):
                            if num%n3 == 0:
                                div.append(n3)
                                div.append(num // n3)
                        if len(div) == 2:
                            primo = "é Primo"
                        print(f"Este número {primo}, tem {len(div)} divisores, é divisível por {sorted(div)}")
                        if input("Verificar outro número? (S - Continuar) ").upper() != "S":
                            print("Volte Sempre!")
                            break

                numeroprimo()
            case 53:
                print(Inout,Inout,Ex053,Inout,Inout,Resp)
                palavra = input("Digite uma palavra: ")
                resultado = "É palíndromo"
                for n in range(len(palavra)):
                    if palavra[n] != palavra[-(1+n)]:
                        resultado = "Não é palíndromo"
                        break
                print(resultado)
            case 54:
                print(Inout,Inout,Ex054,Inout,Inout,Resp)
                pessoas = []
                maioridade = []
                menoridade = []
                for n in range (7):
                    nome = input(f"Qual o nome da {n + 1}° Pessoa: ")

                    while True:
                        ano = input(f"Em que ano a {nome} nasceu?: ")
                        if ano.isdigit() == True and int(ano) <= 2025:
                            ano = int(ano)
                            pessoas.append((nome,ano))
                            if ano < 2008:
                                maioridade.append((nome,ano))
                            else:
                                menoridade.append((nome,ano))
                            break
                        else:
                             print("Digite um valor inteiro e menor que 2025 ")

                print(f"Pessoas que são maior de idade {len(maioridade)}:")
                for nome,ano in maioridade:
                    print(f"Nome: {nome:<20}, Nasceu em: {ano:<10}")
                print(f"----------------------------------------------------------------")
                print(f"Pessoas que são menor de idade {len(menoridade)}, seus nomes:")
                for nome, ano in menoridade:
                    print(f"Nome: {nome:<20}, Nasceu em: {ano:<10}")
                print(pessoas)
            case 55:
                print(Inout,Inout,Ex055,Inout,Inout,Resp)

                #Recibimento de dados
                peso5pessoas =[]
                for n in range (5):
                    while True:
                        try:
                            peso5pessoas.append(float(input(f"Qual o Peso da {n+1}° Pessoa em kg:  ")))
                            break
                        except ValueError:
                            print('Digite somente número.')

                # Apresentação de dados
                print(f"O maior peso: {max(peso5pessoas)} Kg.\nO menor peso: {min(peso5pessoas)} Kg.")
            case 56:
                print(Inout,Inout,Ex056,Inout,Inout,Resp)
                homem_velho = "Não tem Homem no cadastro"
                maior_idade = 0
                mulheres = 0
                idade_grupo = 0
                for n in range(4):
                    while True:
                        try:
                            nome = input("Digite seu nome: ")
                            idade = int(input("Digite sua idade: "))
                            sexo = input("Qual seu sexo H - Homem ou M - Mulher: ").upper()

                            if idade <= 0 or sexo not in ["M","H"]:
                                print("Dado inválido tente novamente!")
                                continue
                            elif sexo == "M" and idade < 20:
                                mulheres = mulheres + 1

                            elif sexo == "H" and maior_idade < idade:
                                maior_idade = idade
                                homem_velho = nome
                            idade_grupo = idade_grupo + idade
                            break
                        except ValueError:
                            print("Entrada Invalida!")
                            continue
                print(f"Média de Idade é {idade_grupo/4} anos")
                print(f"O home mais velho é: {homem_velho}")
                print(f"Mulher com menos de 20 anos: {mulheres}")
            case 57:
                print(Inout,Inout,Ex057,Inout,Inout,Resp)
                while True:
                    sexo = input("Digite o sexo: (M - Masculino / F - Feminino): ").strip().upper()
                    if sexo in ["M","F"]:
                        print(f"Entrada Valida, sexo {sexo} registrado.")
                        break
                    else:
                        print("Digite uma entrada Valida! M ou F")
            case 58:
                print(Inout,Inout,Ex058,Inout,Inout,Resp)
                import random
                aleatorio = random.randint(0,11)
                palpites = 0
                while True:
                    palpites += 1
                    if int(input("Digite um Número de 0 a 10: ")) == aleatorio:
                        print(f"Parabéns você Acertou, tentativas {palpites}")
                        break
                    else:
                        print(f"Você errou! tentativas {palpites}")
            case 59:
                print(Inout,Inout,Ex059,Inout,Inout,Resp)
                print("Opções:")
                print("[1] -- somar\n[2] -- multiplicar\n[3] -- maior\n[4] -- novos números\n[5] -- sair do programa")
                while True:
                    try:
                        Valor1= int(input("Digite o primeiro valor: "))
                        Valor2= int(input("Digite o segundo valor: "))
                        opcao = int(input("Digite uma opção: "))
                        if opcao not in range(1,6):
                            print("Opção invalida")
                        elif opcao == 1:
                            print(f"Soma de {Valor1} + {Valor2} = {Valor1+Valor2}")
                        elif opcao == 2:
                            print(f"Multiplicação de {Valor1} * {Valor2} = {Valor1*Valor2}")
                        elif opcao == 3:
                            print(f"O maior é: {max(Valor1,Valor2)}")
                        elif opcao == 4:
                            print("Opção escolhida: novos números")
                            continue
                        else:
                            print("Até Logo!")
                            break
                    except ValueError:
                        print("Entrada invalida")
                        continue
            case 60:
                print(Inout,Inout,Ex060,Inout,Inout,Resp)
                Valor1 = int(input("Digite o valor: "))
                n = Valor1
                fator = 1
                print(f"Valor {factorial(Valor1)}")
                while n >= 1:
                    fator  *= n
                    n -= 1

                print(f"O fatorial de {Valor1} é {fator}")
                print(f"Valor {factorial(Valor1)}")
            case 61:
                print(Inout,Inout,Ex061,Inout,Inout,Resp)
                while True:
                    PA = []
                    try:
                        primeiro_termo = int(input("Digite o primeiro termo: "))
                        raz = int(input('Digite o valor da razão: '))
                        n = 0
                        while n < 10:
                            a = int(primeiro_termo + n * raz)
                            n += 1
                            PA.append(a)
                        print(f"Progressão Aritmética - PA: {PA}")
                    except ValueError:
                        print("Valor invalido digite número inteiro")
                        continue
                    if input("Deseja continuar? ( S - Continue) ").upper() != "S":
                        break
            case 62:
                print(Inout, Inout, Ex062, Inout, Inout, Resp)
                cont = True
                while cont:
                    PA = []
                    try:
                        primeiro_termo = int(input("Digite o primeiro termo: "))
                        raz = int(input('Digite o valor da razão: '))
                        termos = int(input('Quantos termos você deseja ver? '))
                        n = 0
                        while True:
                            for n in range(0,termos):
                                a = int(primeiro_termo + n * raz)
                                n += 1
                                PA.append(a)
                            print(f"Progressão Aritmética - PA: {PA}")
                            maistermos = int(input("Quantos termos a mais deseja visualizar?(0 - Encerra): ").strip())
                            if maistermos <= 0:
                                cont = False
                                break
                            else:
                                termos += maistermos
                    except ValueError:
                        print("Valor invalido digite número inteiro")
                        continue

                        break
            case 63:
                print(Inout,Inout,Ex063,Inout,Inout,Resp)
                n = int(input("Digite um número: "))
                totallist = [0,1]
                a = 0
                while a < n:
                    total = totallist[-2]+totallist[-1]
                    totallist.append(total)
                    a += 1
                    print(total, end=", ")
                print(totallist)
            case 64:
                print(Inout,Inout,Ex064,Inout,Inout,Resp)
                contador = 0
                soma = 0
                n = 0
                while n != 999:
                    try:
                        print(f"Soma atual {soma}, quantidade de números digitados: {contador}")
                        n = int(input("Digite um número: "))
                        soma += n
                        contador +=1
                    except ValueError:
                        print("Digite um número!")
                print("Até em breve!")
            case 65:
                print(Inout,Inout,Ex065,Inout,Inout,Resp)
                loop = 1
                valores =[]
                soma = 0
                cont = "S"
                while True:
                        try:
                            num = int(input(f"Digite o {loop}° Valor ou zero p/ encerrar: ").strip())
                            if num != 0:
                                loop += 1
                                valores.append(num)
                                soma += num
                            else:
                                print("Encerrando")
                                loop -=1
                                break
                        except ValueError:
                            continue
                print(f"A soma {soma}.\n"
                      f"Quantidade de número digitados: {loop}.\n"
                      f"Média inteira: {soma//loop}.")
            case 66:
                print(Inout,Inout,Ex066,Inout,Inout,Resp)
                somaTotal = n = 0
                while True:
                    try:
                        valor = int(input("Digite um valor (999 - encerra) : "))
                        if valor == 999:
                          print("Encerrando o programa, até logo!")
                          break
                        else:
                            somaTotal += valor
                            n += 1
                    except ValueError:
                        print("Entrada invalida, digite um número!")
                        continue
                print(f" A soma dos {n} números digitados foi {somaTotal}  ")
            case 67:
                print(Inout,Inout,Ex067,Inout,Inout,Resp)
                while True:
                    try:
                        print("TABUADA + - X /")
                        numero = int(input("Qual o número da tabuada: "))
                        break
                    except ValueError:
                        print("Entrada inválida, digite um número!")
                        continue
                print(f"TABUADA DO {numero}")
                for num in range (1,11):
                    print(f"|| {numero:5} + {num:2} = {numero+num:5} | {numero:5} - {num:2} = {numero-num:5} |",end= '')
                    print(f"{numero:5} * {num:2} = {numero*num:5} | {numero*num:5} / {num:2} = {numero:5} ||")
            case 68:
                print(Inout,Inout,Ex068,Inout,Inout,Resp)
                import random
                def funcaojogo():
                 while True:
                    vitoria = 0
                    while True:
                     try:
                        possibilidade = ["par","impar"]
                        valor = random.randint(0,100)

                        #usuario_escolhe
                        posuser =""
                        while posuser not in possibilidade:
                            posuser = input("Escolha par ou impar: ").lower().strip()
                            if posuser not in possibilidade:
                                print("Digite par ou impar")

                        computador = "impar" if posuser == "par" else "par"
                        print(f"então serei {computador}")
                        valoruser = int(input("um valor: "))

                        if (valoruser + valor)%2 == 0:
                            resultado = "par"
                        else:
                            resultado = "impar"
                        if posuser == resultado:
                                print("Você venceu!")
                                vitoria +=1
                                continue
                        else:
                                print("Eu venci!")
                                print(f"Você teve {vitoria} vitorias consecutivas!")
                                break

                     except ValueError:
                         print("Entrada inválida, digite novamente")
                         continue
                funcaojogo()
                if input("Deseja jogar novamente? (S - Sim)").upper() in ["S","Sim"]:
                    funcaojogo()
            case 69:
                print(Inout,Inout,Ex069,Inout,Inout,Resp)
                sex = ["m","masculino","homem","f","feminino","mulher"]
                pessoas = []
                maior18 = mulher20 = homem = 0
                while True:
                    try:
                        nome = str(input("Qual o seu nome? "))
                        idade = int(input("Qual a sua idade? "))
                        if idade < 0:
                            print("Idade invalida")
                            continue
                        sexo = ""
                        while sexo not in sex:
                            sexo = input("Qual o seu sexo?(M - Masculino/ F - Feminino) ").strip().lower()
                            if sexo not in sex:
                                print("Entrada invalida")
                        pessoa = (nome,idade,sexo)
                        if idade > 18:
                            maior18 +=1
                        if sexo in ["f","feminino","mulher"] and idade < 20:
                            mulher20 +=1
                        elif sexo in ["m","masculino","homem"]:
                            homem +=1
                    except ValueError:
                        print("Entrada inválida!")
                        continue
                    if input("Cadastro concluído?(S - Sim) ").upper() == "S":
                        break
                print(f"Pessoas com mais de 18 anos: {maior18}")
                print(f"Quantidade de homens cadastrados: {homem}")
                print(f"Mulheres com menos de 20 anos: {mulher20}")
            case 70:
                print(Inout,Inout,Ex070,Inout,Inout,Resp)
                produtonome = []
                produtovalor=[]
                total_compra=0
                while True:
                    try:
                        caixa_nome = input("Qual é o produto? ")
                        caixa_valor = float(input("Digite o valor do produto: "))
                        if caixa_valor > 0:
                            total_compra += caixa_valor
                            produtonome.append(caixa_nome)
                            produtovalor.append(caixa_valor)
                            if input("Deseja passar um novo produto?(S - Sim) ").upper() != "S":
                                break
                    except ValueError:
                        print("Digite valor válido!")
                        continue
                print(f"O valor total da compra é R$ {total_compra:.2f}")
                print(f"São {sum(1 for n in produtovalor if n>1000)} produtos acima de R$1000")
                print(f"O produto mais barato: {produtonome[produtovalor.index(min(produtovalor))]}")
            case 71:
                print(Inout,Inout,Ex071,Inout,Inout,Resp)
                while True:
                    try:
                        saque = int(input("Qual o valor do saque? R$ ").strip())
                        if saque <= 0:
                            print("Digite um valor maior que zero")
                            continue
                        listanotas = [100,50,20,10,5,2,1]
                        notas=[]
                        n = 0
                        while True:
                            if saque >= 1:
                                inteiro = saque//listanotas[n]
                                notas.append(inteiro)
                                saque = saque%listanotas[n]
                                n += 1
                            else:
                                print("Saque finalizado!")
                                break
                    except ValueError:
                        print("Valor inválido, saque mínimo R$ 1,00")
                        continue
                    print(" Cédulas entregues::")
                    for i in range(len(notas)):
                        if notas[i] !=0:
                            print(f" {notas[i]} nota(s) de R$ {listanotas[i]},00.")
                    if input("Deseja realizar um novo saque? (S - Sim)").strip().upper() != "S":
                        break
