from math import factorial

#from scipy.optimize import bracket

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
'Exercício Python  035: Desenvolva um programa que leia o comprimento de três retas\n e diga ao usuário se elas podem ou não formar um triângulo.'
'Exercício Python  036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.',
'Exercício Python  037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.',
'Exercício Python  038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:\n– O primeiro valor é maior\n– O segundo valor é maior\n– Não existe valor maior, os dois são iguais.',
'Exercício Python  039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.',
'Exercício Python  040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:\n– Média abaixo de 5.0: REPROVADO\n– Média entre 5.0 e 6.9: RECUPERAÇÃO\n– Média 7.0 ou superior: APROVADO.',
'Exercício Python  041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:\n– Até 9 anos: MIRIM\n– Até 14 anos: INFANTIL\n– Até 19 anos: JÚNIOR\n– Até 25 anos: SÊNIOR\n– Acima de 25 anos: MASTER.',
'Exercício Python  042: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:\n– EQUILÁTERO: todos os lados iguais\n– ISÓSCELES: dois lados iguais, um diferente\n– ESCALENO: todos os lados diferentes.',
'Exercício Python  043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:\n– IMC abaixo de 18,5: Abaixo do Peso\n– Entre 18,5 e 25: Peso Ideal\n– 25 até 30: Sobrepeso\n– 30 até 40: Obesidade\n– Acima de 40: Obesidade Mórbida.',
'Exercício Python  044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:\n– à vista dinheiro/cheque: 10% de desconto\n– à vista no cartão: 5% de desconto\n– em até 2x no cartão: preço formal\n– 3x ou mais no cartão: 20% de juros.',
'Exercício Python  045: Crie um programa que faça o computador jogar Jokenpô com você.',
'Exercício Python  046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.',
'Exercício Python  047: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.',
'Exercício Python  048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.',
'Exercício Python  049: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.',
'Exercício Python  050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.',
'Exercício Python  051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.',
'Exercício Python  052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.',
'Exercício Python  053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.',
'Exercício Python  054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.',
'Exercício Python  055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.',
'Exercício Python  056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.',
'Exercício Python  057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto.',
'Exercício Python  058: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.',
'Exercício Python  059: Crie um programa que leia dois valores e mostre um menu na tela:\n[ 1 ] somar\n[ 2 ] multiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nSeu programa deverá realizar a operação solicitada em cada caso.',
'Exercício Python  060: Faça um programa que leia um número qualquer e mostre o seu fatorial.',
'Exercício Python  061: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.',
'Exercício Python  062: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.',
'Exercício Python  063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.',
'Exercício Python  064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).',
'Exercício Python  065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.',
'Exercício Python  066: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).',
'Exercício Python  067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.',
'Exercício Python  068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.',
'Exercício Python  069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:\nA) quantas pessoas tem mais de 18 anos.\nB) quantos homens foram cadastrados.\nC) quantas mulheres tem menos de 20 anos.',
'Exercício Python  070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:\nA) qual é o total gasto na compra.\nB) quantos produtos custam mais de R$1000.\nC) qual é o nome do produto mais barato.',
'Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.',
'Exercício Python  072: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.',
'Exercício Python  073: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:\na) Os 5 primeiros times.\nb) Os últimos 4 colocados.\nc) Times em ordem alfabética.\nd) Em que posição está o time da Chapecoense.',
'Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.',
'Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:\nA) Quantas vezes apareceu o valor 9.\nB) Em que posição foi digitado o primeiro valor 3.\nC) Quais foram os números pares.',
'Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.',
'Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.',
'Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.',
'Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.',
'Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.',
'Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.\n Depois disso, mostre:\nAv) Quantos números foram digitados.\n B) A lista de valores, ordenada de forma decrescente.\nC) Se o valor 5 foi digitado e está ou não na lista.',
'Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.',
'Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.',
'Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,\n guardando tudo em uma lista. No final, mostre:\nA) Quantas pessoas foram cadastradas.\n B) Uma listagem com as pessoas mais pesadas.\nC) Uma listagem com as pessoas mais leves.',
'Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.',
'Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.',
'Exercício Python 087: Aprimore o desafio anterior, mostrando no final:\nA) A soma de todos os valores pares digitados.\nB) A soma dos valores da terceira coluna.\nC) O maior valor da segunda linha.',
'Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.',
'Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.',
'Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.',
'Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.',
'Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.',
'Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.',
'Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:\nA) Quantas pessoas foram cadastradas\nB) A média de idade\nC) Uma lista com as mulheres\nD) Uma lista de pessoas com idade acima da média.',
'Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.',
'Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.',
'Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.\nEx:\n escreva("Olá, Mundo!") Saída:\n Olá, Mundo!\nVeja o curso de Python PARTE 1 em https://www.youtube.com/playlist?list…\nVeja o curso de Python PARTE 2 em https://www.youtube.com/playlist?list…\n Veja o curso de Python PARTE 3 em https://www.youtube.com/watch?v=0LB3F…\n Veja a lista de exercícios de Python em https://www.youtube.com/playlist?list….',
'Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:\na) de 1 até 10, de 1 em 1\nb) de 10 até 0, de 2 em 2\nc) uma contagem personalizada.',
'Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.',
'Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.',
'Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.',
'Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.',
'Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.',
'Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante "a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt("Digite um n: ").',
'Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:\n– Quantidade de notas\n – A maior nota\n – A menor nota\n – A média da turma\n– A situação (opcional).',
'Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará. Importante: use cores.',
'Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.',
'Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.',
'Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.',
'Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.',
'Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.',
'Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.',
'Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.',
'Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.',
'Exercício Python 115a: Vamos criar um menu em Python, usando modularização.',
'Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.',
'Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.']



def printNomeExercício(n):
    print('\n'*2,'#'*30,'\n'*2)
    print(listaExercicios[n])
    print('\n'*2,'#'*30,'\n'*2)
    print("RESPOSTA:\n")

#--------------------------------------------------------------------------------------------------------------------------------------
# EXERCISES TWO WORLD
#---------------------------------------------------------------------------------------------------------------------------------------#
Fim = 1
while Fim != 0:
    n = int(input('\nDigite de 36 a 71 para ver os exercícios ou 0 para encerrar\nQual Exercício executar? '))
    if n == 0:
        print("Volte Sempre!")
        Fim = 0
    elif 36<= n <= 71:
        match n:
            
            #Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.       
            case 36:
                printNomeExercício(n)
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
            
            #Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
            case 37:
                printNomeExercício(n)
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
            
            #Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:\n– O primeiro valor é maior\n– O segundo valor é maior\n– Não existe valor maior, os dois são iguais
            case 38:
                printNomeExercício(n)
                Num1 = int(input("Digite o primeiro numero: "))
                Num2 = int(input("Digite o segundo numero: "))
                if Num1 == Num2:
                    print("Os dois valores são iguais")
                elif Num1>Num2:
                    print("O Primeiro valor é maior")

            #Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
            case 39:
                printNomeExercício(n)
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
            
            #Exercício Python 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
                #        – Média abaixo de 5.0: REPROVADO
                #        – Média entre 5.0 e 6.9: RECUPERAÇÃO
                #        – Média 7.0 ou superior: APROVADO.
            case 40:
                printNomeExercício(n)
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
            
            #Exercício Python 41: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
                #        – Até 9 anos: MIRIM
                #        – Até 14 anos: INFANTIL
                #        – Até 19 anos: JÚNIOR
                #        – Até 25 anos: SÊNIOR
                #        – Acima de 25 anos: MASTER.
            case 41:
                printNomeExercício(n)

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
                        #Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou          que passou do prazo.

            #Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
            #        – EQUILÁTERO: todos os lados iguais
            #        – ISÓSCELES: dois lados iguais, um diferente
            #        – ESCALENO: todos os lados diferentes.
            case 42:
                printNomeExercício(n)
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
            
            #Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
            #        – IMC abaixo de 18,5: Abaixo do Peso
            #        – Entre 18,5 e 25: Peso Ideal
            #        – 25 até 30: Sobrepeso
            #        – 30 até 40: Obesidade
            #        – Acima de 40: Obesidade Mórbida.
            case 43:
                printNomeExercício(n)
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
            
                        #        – Não existe valor maior, os dois são iguais.

            #Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
            #        – à vista dinheiro/cheque: 10% de desconto
            #        – à vista no cartão: 5% de desconto
            #        – em até 2x no cartão: preço formal
            #        – 3x ou mais no cartão: 20% de juros.
            case 44:
                printNomeExercício(n)
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
            
                        #        – O segundo valor é maior

            #Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
            case 45:
                import random
                printNomeExercício(n)
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
            
                        #        – O primeiro valor é maior

            #Exercício Python 46: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
            case 46:
                printNomeExercício(n)
                from time import sleep
                for a in range(10,-1,-1):
                    print(a)
                    sleep(1)
                print("Acabou seu tempo!")
            
                        #Exercício Python 38: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

            #Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
            case 47:
                printNomeExercício(n)
                lista = []
                for n in range(2,50,2):
                    lista.append(n)
                print(lista)
            
                        #Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

            #Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
            case 48:
                printNomeExercício(n)
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
            
                        #Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

            #Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
            case 49:
                printNomeExercício(n)
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
            
            #Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
            case 50:
                printNomeExercício(n)
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
            
            #Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
            case 51:
                printNomeExercício(n)
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
            
            #Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
            case 52:
                printNomeExercício(n)
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
            
            #Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
            case 53:
                printNomeExercício(n)
                palavra = input("Digite uma palavra: ")
                resultado = "É palíndromo"
                for n in range(len(palavra)):
                    if palavra[n] != palavra[-(1+n)]:
                        resultado = "Não é palíndromo"
                        break
                print(resultado)
            
            #Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
            case 54:
                printNomeExercício(n)
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
            
            #Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
            case 55:
                printNomeExercício(n)

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
            
            #Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
            case 56:
                printNomeExercício(n)
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
            
            #Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
            case 57:
                printNomeExercício(n)
                while True:
                    sexo = input("Digite o sexo: (M - Masculino / F - Feminino): ").strip().upper()
                    if sexo in ["M","F"]:
                        print(f"Entrada Valida, sexo {sexo} registrado.")
                        break
                    else:
                        print("Digite uma entrada Valida! M ou F")
            
            #Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
            case 58:
                printNomeExercício(n)
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
            
            #Exercício Python 59: Crie um programa que leia dois valores e mostre um menu na tela:
                #        [ 1 ] somar
                #        [ 2 ] multiplicar
                #        [ 3 ] maior
                #        [ 4 ] novos números
                #        [ 5 ] sair do programa
                #        Seu programa deverá realizar a operação solicitada em cada caso.
            case 59:
                printNomeExercício(n)
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
            
            #Exercício Python 60: Faça um programa que leia um número qualquer e mostre o seu fatorial.
            case 60:
                printNomeExercício(n)
                Valor1 = int(input("Digite o valor: "))
                n = Valor1
                fator = 1
                print(f"Valor {factorial(Valor1)}")
                while n >= 1:
                    fator  *= n
                    n -= 1

                print(f"O fatorial de {Valor1} é {fator}")
                print(f"Valor {factorial(Valor1)}")
            
            #Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
            case 61:
                printNomeExercício(n)
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
            
            #Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.
            case 62:
                printNomeExercício(n)
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
            
            #Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
            case 63:
                printNomeExercício(n)
                n = int(input("Digite um número: "))
                totallist = [0,1]
                a = 0
                while a < n:
                    total = totallist[-2]+totallist[-1]
                    totallist.append(total)
                    a += 1
                    print(total, end=", ")
                print(totallist)
            
            #Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
            case 64:
                printNomeExercício(n)
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
            
            #Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
            case 65:
                printNomeExercício(n)
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
            
            #Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
            case 66:
                printNomeExercício(n)
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
            
            #Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
            case 67:
                printNomeExercício(n)
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
            
            #Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
            case 68:
                printNomeExercício(n)
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
            
            #Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
            #        A) quantas pessoas tem mais de 18 anos.
            #        B) quantos homens foram cadastrados.
            #        C) quantas mulheres tem menos de 20 anos.           
            case 69:
                printNomeExercício(n)
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
            
            #Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
                #        A) qual é o total gasto na compra.
                #        B) quantos produtos custam mais de R$1000.
                #        C) qual é o nome do produto mais barato.
            case 70:
                printNomeExercício(n)
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
            
            #Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
            case 71:
                printNomeExercício(n)
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

