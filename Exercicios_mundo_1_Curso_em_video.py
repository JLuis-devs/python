listaExercicios = [
'Digite de 1 a 115 para ver os exercícios ou 0 para encerrar\nQual Exercício executar? ',
'Exercício Python  001: Crie um programa que escreva "Olá, mundo!" na tela.',
'Exercício Python  002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.',
'Exercício Python  003: Crie um programa que leia dois números e mostre a soma entre eles.',
'Exercício Python  004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.',
'Exercício Python  005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.',
'Exercício Python  006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.',
'Exercício Python  007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.',
'Exercício Python  008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.',
'Exercício Python  009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.',
'Exercício Python  010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares nela pode comprar.',
'Exercício Python  011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área \n e a quantidade de tinta necessária para pintá-la,\nsabendo que cada litro de tinta pinta uma área de 2 metros quadrados.',
'Exercício Python  012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto".',
'Exercício Python  013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.',
'Exercício Python  014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.',
'Exercício Python  015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e \n a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.',
'Exercício Python  016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.',
'Exercício Python  017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.',
'Exercício Python  018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'
'Exercício Python  019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\n Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.',
'Exercício Python  020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.\nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.',
'Exercício Python  021: Faça um programa em que abra e reproduza o áudio de um arquivo MP3.',
'Exercício Python  022: Crie um programa que leia o nome completo de uma pessoa e mostre:\n– O nome com todas as letras maiúsculas e minúsculas.\n– Quantas letras ao todo (sem considerar espaços).\n– Quantas letras tem o primeiro nome.',
'Exercício Python  023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.',
'Exercício Python  024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".',
'Exercício Python  025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.',
'Exercício Python  026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece \n a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.',
'Exercício Python  027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro\n e o último nome separadamente.',
'Exercício Python  028: Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.',
'Exercício Python  029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,\n mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.',
'Exercício Python  030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.',
'Exercício Python  031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.',
'Exercício Python  032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.',
'Exercício Python  033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.',
'Exercício Python  034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\nPara salários superiores a R$1250,00, calcule um aumento de 10%.\nPara os inferiores ou iguais, o aumento é de 15%.',
'Exercício Python  035: Desenvolva um programa que leia o comprimento de três retas\n e diga ao usuário se elas podem ou não formar um triângulo.']
#--------------------------------------------------------------------------------------------------------------------------------------
# EXERCISES ONE WORLD
#---------------------------------------------------------------------------------------------------------------------------------------#
def printNomeExercício(n):
    print("\n"*2,linha*2,"\n"*2)
    print(listaExercicios[n])
    print('\n'*2,'#'*30,'\n'*2)
    print("RESPOSTA:\n")














Fim = 1


while Fim != 0:
    n = int(input(listaExercicios[0]))
    if n == 0:
        print("Volte Sempre!")
        Fim = 0
    elif 1<= n <= 35:
        match n:
            #Exercício Python 001: Crie um programa que escreva "Olá, mundo!" na tela.
            case 1:
                printNomeExercício(n)
                print("Hellow, World")

            #Exercício Python 002: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
            case 2:
                printNomeExercício(n)
                nome = input("QUal o seu nome? ")
                print(f"Seja bem vindo(a) {nome}")

            #Exercício Python 003: Crie um programa que leia dois números e mostre a soma entre eles.
            case 3:
                printNomeExercício(n)
                n1 = int(input("Digite o valor 1: "))
                n2 = int(input("Digite o valor 2: "))
                print("O valor da soma: ",n1+n2)
            
            #Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
            case 4:
                printNomeExercício(n)
                v1 = input("Digite algo: ")
                print(f"O que você digitou é Numérico: {v1.isnumeric()}.")
                print(f"O que você digitou é alfanumérico: {v1.isalnum()}.")
                print(f"O que você digitou é caixa alta: {v1.isupper()}.")
                print(f"O que você digitou é caixa baixa: {v1.islower()}.")
                print(f"O que você digitou tem espaço vazio: {v1.isspace()}.")
                print(f"O que você digitou é Numérico: {v1.isdecimal()}.")
                print(f"O que você digitou é digito: {v1.isdigit()}.")
                print(type(v1))

            #Exercício Python  005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
            case 5:
                printNomeExercício(n)
                n1 = int(input("Digite um número: "))
                print(f"O número que você digitou foi {n1}.\n O antecessor dele é {n1-1} e o seu sucessor é {n1+1}!")
            
            #Exercício Python  006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
            case 6:
                print(Inout,Inout,Ex006,Inout, Inout,Resp)
                n1 = float(input("Digite um número: "))
                print(f"O dobro deste número é: {n1*2}.\n O triplo é {n1*3} e a raiz quadrada {n1**0.5}.")
            
            #Exercício Python  007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
            case 7:
                printNomeExercício(n)
                n1=float(input("Digite a Primeira nota: "))
                n2=float(input("Digite a Segunda nota: "))
                n3 = (n1+n2)/2
                print(f"A média do aluno foi {n3}, Sendo a primeira nota igual a {n1} e a segunda {n2}.")
            
            #Exercício Python  008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
            case 8:
                printNomeExercício(n)
                n1 = float(input("Digite a medida em metros: "))
                print(f"A medida de {n1} metros é {n1*100}cm e {n1*1000}mm.")
            
            #Exercício Python  009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
            case 9:
                printNomeExercício(n)
                n1 = int(input("Digite o Valor: "))
                for i in range(10):
                    print(f"{n1}X{i+1} = {n1*(i+1)}.")
            
            #Exercício Python  010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares nela pode comprar.
            case 10:
                printNomeExercício(n)
                valor = float(input("Qual Valor em R$ "))
                print(f"Você consegue comprar {valor/5.47:.2f} Dollars.")
            
            #Exercício Python  011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área \n e a quantidade de tinta necessária para pintá-la,\nsabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
            case 11:
                printNomeExercício(n)
                lg = float(input("Largura da parede: "))
                cp = float(input("Altura da parede: "))
                print(f"Será necessário {lg*cp/2} litros para {lg*cp} metros quadrados de parede.")
            
            #Exercício Python  012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto".
            case 12:
                printNomeExercício(n)
                n1 = float(input("Digite o valor do produto: "))
                print(f"Avista você tem 5% de desconto.\n Valor com desconto R$ {n1*0.95:2}.")
            
            #Exercício Python  013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
            case 13:
                printNomeExercício(n)
                Aum = float(input("Quantos porcento de aumento: "))
                sal = float(input("Qual o seu sálario atual: "))
                print(f"Seu novo salário com {Aum}% de aumento é R$ {sal*(100+Aum)/100:.2f}.")
            
            #Exercício Python  014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
            case 14:
                printNomeExercício(n)
                temp1 = float(input("Digite a temperatura em graus °C: "))
                temp2 = 1.8*temp1+32
                print(f"Sua temperatura em {temp2} °F.")
            
            #Exercício Python  015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e \n a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
            case 15:
                printNomeExercício(n)
                km = int(input("Quantos Km foi rodado: "))
                Dia = int(input("Quantos dias: "))
                tot = (Dia*60)+(km*0.15)
                print(f"O valor do aluguel foi:\n {Dia} dias R${Dia*60}\n {km}km R${km*0.15}")
                print(f"Valor Total R$ {tot}.")
            
            #Exercício Python  016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
            case 16:
                printNomeExercício(n)
                num1 = float(input("Digite um número: "))
                print(f"A porção inteira deste número é {num1:0f}.")
            
            #Exercício Python  017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
            case 17:
                printNomeExercício(n)
                ca = float(input("Digite o cateto adjacente: "))
                co = float(input("Digite o cateto oposto: "))
                hp = (ca**2 + co**2)**0.5
                print(f"A hipotenusa deste triangulo é: {hp:2f}.")
            
            #Exercício Python  018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.'
            case 18:
                import math
                printNomeExercício(n)
                ang = float(input("Digite o angulo em graus: "))
                print(f"Seno: {math.sin(ang):2f}\nCosseno: {math.cos(ang):2f}\nTangente: {math.tan(ang):2f}.")
            
            #Exercício Python  019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\n Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
            case 19:
                import random
                printNomeExercício(n)
                nome = [input(f"Digite o nome do {i+1}° aluno: ") for i in range (4)]
                escolhido = random.choice(nome)
                print(f"O aluno escolhido foi: {escolhido}")
                while True:
                    a = input("Quer continuar o sorteio(S/N)? ")
                    a = a.capitalize()
                    if a == "N" or a == "NAO" or a =="NÃO":
                        print("Até a próxima!")
                        break
                    elif a == "S" or a == "SIM":
                        escolhido = random.choice(nome)
                        print(f"O aluno escolhido foi: {escolhido}")
                    else:
                        print("Valor inválido")
            
            #Exercício Python  020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.\nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
            case 20:
                import random
                printNomeExercício(n)
                numero = int(input("Quantos alunos participaram do sorteio: "))
                Continuar = "S"
                if numero != 0:
                    nome =[input(f"Qual o nome do {i+1}° aluno: ") for i in range(numero)]
                    while Continuar in ["S","SIM"]:
                        random.shuffle(nome)
                        print(f"A ordem será: {nome}")
                        while True:
                            Continuar = input("Deseja sortear novamente(S\\N)? ").upper()
                            if Continuar in ["S","SIM","NAO","NÃO","N"]:
                                    break
                            else:
                                print("Valor Inválido!")

                    print("Volte Sempre!")
                else:
                    print("Não terá sorteio")

            #Exercício Python  021: Faça um programa em que abra e reproduza o áudio de um arquivo MP3.
            case 21:
                from playsound3 import playsound
                printNomeExercício(n)
                playsound('/media/luis/27a6a487-1e65-498d-8948-f25bfab74219/EXTRA/Musica/Luiz Poderoso Chefão/01- Cheiro da Karolina.mp3')
            
            #Exercício Python  022: Crie um programa que leia o nome completo de uma pessoa e mostre:\n– O nome com todas as letras maiúsculas e minúsculas.\n– Quantas letras ao todo (sem considerar espaços).\n– Quantas letras tem o primeiro nome.
            case 22:
                printNomeExercício(n)
                nome = input("Digite o nome: ")
                nomelimpo = nome.strip()
                print(f"Nome em maiúsculo: {nome.upper()}.\n Nome em minúsculo: {nome.lower()}.\n"
                      f"Seu nome tem {len(nome) - nome.count(" ")} letras.\n"
                      f"Quantas letras tem o primeiro nome: {nomelimpo[0:nomelimpo.find(' ')]}\n"
                      f"tamanho da string {len(nome)}")
            
            #Exercício Python  023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
            case 23:
                printNomeExercício(n)
                num = input("Digite o número: ")
                while True:
                    if len(num) == 4:
                        print(f"Unidade: {num[0]}\n")
                        print(f"Dezena: {num[1]}\n")
                        print(f"Centena: {num[2]}\n")
                        print(f"Milhar: {num[3]}\n")
                    else:
                        print("Digite um valor entre 0 a 9999")
            
            #Exercício Python  024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
            case 24:
                printNomeExercício(n)
                cidade = input("Digite o nome da cidade: ").strip()
                primeiro_nome = cidade[0:cidade.find(" ")]
                if primeiro_nome.upper() == "SANTO":
                    print("O nome desta cidade começa com Santo")
                else:
                    print(f"Não começa e tem como primeiro nome: {primeiro_nome}")

            #Exercício Python  025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
            case 25:
                printNomeExercício(n)
                nome = input("Digite o nome: ").strip().upper()
                if nome.count("SILVA"):
                    print("Tem silva no nome.")
                else:
                    print("Não tem Silva no nome.")
            
            #Exercício Python  026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece \n a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
            case 26:
                printNomeExercício(n)
                frase = input("Digite a frase: ").strip().upper()
                vezes = frase.count("A")
                pvez = frase.find("A")
                uvez = frase.rfind("A")
                print(f"A frase contém {vezes} letra A, com a primeira na posição {pvez} e a ultima {uvez}.")

            #Exercício Python  027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro\n e o último nome separadamente.
            case 27:
                printNomeExercício(n)
                nome = input("Digite o nome: ").strip().capitalize()
                ultnome = nome[nome.rfind(" "):len(nome)+1]
                print(f"Primeiro nome: {nome[0:nome.find(" ")]}\nUltimo nome: {ultnome.capitalize()}")
            
            #Exercício Python  028: Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
            case 28:
                import random
                printNomeExercício(n)
                num = random.randint(0,5)
                while True:
                    escolhido = int(input("Qual número eu pensei: "))
                    if escolhido == num:
                       print("Você acertou!")
                    else:
                       print(f"Você Perdeu!\n O número escolhido: {num}")

                    brinca = input("Quer brincar novamente?(S/N) ").upper()
                    if brinca == "N":
                        break
                    elif brinca == "S":
                        print("Vamos lá!")
                        num = random.randint(0, 5)
                    else:
                        print("Opção errada, Vai brincar novamente comigo!")
           
            #Exercício Python  029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,\n mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
            case 29:
                printNomeExercício(n)
                Vel = int(input("Qual a sua velocidade (km/h): "))
                if Vel > 80:
                    print(f"Você foi multado!\nEstá a {Vel - 80}km/h do limite da via.")
                    print(f"Valor da Multa é R${Vel - 80 * 7}.")
                else:
                    print("Permaneça com a velocidade até 80km/h")
           
            #Exercício Python  030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
            case 30:
                printNomeExercício(n)
                num1 = int(input("Digite um número: "))
                if num1 % 2 == 0:
                    print("Este Número é Par")
                elif num1 % 2 == 1:
                    print("Este Número é Impar")
           
            #Exercício Python  031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
            case 31:
                printNomeExercício(n)
                dist = int(input("Qual a distancia em Km: "))
                if dist > 200:
                    print(f"O valor do km é 45 centavos e no total {dist*0.45} reais.")
                else:
                    print(f"O valor do km é 50 centavos e no total {dist*0.5} reais.")
            #Exercício Python  032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.           
            case 32:
                printNomeExercício(n)
                ano = int(input("Digite um ano: "))
                if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                    print(f"O ano de {ano} é bissexto!")
                else:
                    print(f"O ano {ano} não é bissexto!")

            #Exercício Python  033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
            case 33:
                printNomeExercício(n)
                n = [int(input(f"Digite o {i + 1}° número: ")) for i in range(3)]
                n.sort()
                print(f"O maior número é: {n[2]}")
                print(f"O menor número é: {n[0]}")
            
            #Exercício Python  034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.\nPara salários superiores a R$1250,00, calcule um aumento de 10%.\nPara os inferiores ou iguais, o aumento é de 15%.    
            case 34:
                printNomeExercício(n)
                sal = float(input("Qual o seu salário: "))
                if sal > 1250:
                    taxa = 0.1
                else:
                    taxa = 0.15
                print(f"Seu salário novo é R${sal*(taxa+1):.2f}, teve {taxa:.2%} de aumento.")

            #Exercício Python  035: Desenvolva um programa que leia o comprimento de três retas\n e diga ao usuário se elas podem ou não formar um triângulo.
            case 35:
                printNomeExercício(n)
                l =[float(input(f"Digite o comprimento da {i+1}° reta: ")) for i in range(3)]
                l.sort()
                if l[2] < l[1]+ l[0]:
                    print("As três retas podem formar um triangulo")
                else:
                    print("As três retas não podem formar um triangulo")
    else:
        print("Digite um valor valido!")




