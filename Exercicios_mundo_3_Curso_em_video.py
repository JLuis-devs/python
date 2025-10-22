#from numpy.ma.core import not_equal

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
'Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.'
]

def printNomeExercício(n):
    print("\n"*2,linha*2,"\n"*2)
    print(listaExercicios[n])
    print('\n'*2,'#'*30,'\n'*2)
    print("RESPOSTA:\n")

#--------------------------------------------------------------------------------------------------------------------------------------
# EXERCISES THREE WORLD
#---------------------------------------------------------------------------------------------------------------------------------------#

Fim = 1
while Fim != 0:
    n = int(input('\nDigite de 36 a 71 para ver os exercícios ou 0 para encerrar\nQual Exercício executar? '))
    if n == 0:
        print("Volte Sempre!")
        Fim = 0
    elif 72<= n <= 117:
        match n:

            #Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
            case 72:
                print(Inout,Inout,Inout,Inout,Resp)
                def saudacaoworld():
                    print("Hello World!")
                def saudacao():
                    print(f"Welcome {nome}")
                def saud(noe):
                    print(f"bem vindo {noe}")
                def raizquadrada(a,b,c):
                    delta = lambda a,b,c: b**2 - 4*a*c
                    x1 = (-b+delta(a,b,c)**0.5)/(2*a)
                    x2 = (-b-delta(a,b,c)**0.5)/(2*a)
                    return [x1,x2]

                saudacaoworld()
                nome = input("What is your name?: ")
                saudacao()
                saud(nome)
                coeficientes={}
                for n in ["a","b","c"]:
                    coef = int(input(f"Qual é o coeficiente {n}: "))
                    coeficientes.update({n:coef})
                print(f"Os coeficientes a,b,c são respectivamente: {coeficientes['a']},{coeficientes['b']},{coeficientes['c']}")
                x = raizquadrada(coeficientes["a"],coeficientes["b"],coeficientes["c"])
                print(x)

            #Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
                #        a) Os 5 primeiros times.
                #        b) Os últimos 4 colocados.
                #        c) Times em ordem alfabética.
                #        d) Em que posição está o time da Chapecoense.
            case 73:
                printNomeExercício(n)
                x = "Python"
                y = "is"
                z = "awesome"
                print(x, y, z)

            #Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
            case 74:
                printNomeExercício(n)
            

            #Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
                #        A) Quantas vezes apareceu o valor 9.
                #        B) Em que posição foi digitado o primeiro valor 3.
                #        C) Quais foram os números pares.
            case 75:
                printNomeExercício(n)

            #Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
            case 76:
                printNomeExercício(n)
            
            #Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
            case 77:
                printNomeExercício(n)
            
            #Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
            case 78:
                printNomeExercício(n)
            
            #Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
            case 79:
                printNomeExercício(n)
            
            #Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
            #Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
            #         Depois disso, mostre:
            #        A) Quantos números foram digitados.
            #        B) A lista de valores, ordenada de forma decrescente.
            #        C) Se o valor 5 foi digitado e está ou não na lista.
            case 80:
                printNomeExercício(n)
            
            
            case 81:
                printNomeExercício(n)
            
            #Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
                        
            case 82:
                printNomeExercício(n)
            
            #Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
            case 83:
                printNomeExercício(n)
            
            #Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
            #         guardando tudo em uma lista. No final, mostre:
                #        A) Quantas pessoas foram cadastradas.
                #        B) Uma listagem com as pessoas mais pesadas.
                #        C) Uma listagem com as pessoas mais leves.
            case 84:
                printNomeExercício(n)
            
            #Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
            case 85:
                printNomeExercício(n)
            
            #Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
            case 86:
                printNomeExercício(n)
            
            #Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
                #        A) A soma de todos os valores pares digitados.
                #        B) A soma dos valores da terceira coluna.
                #        C) O maior valor da segunda linha.
            case 87:
                printNomeExercício(n)
            
            #Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
            case 88:
                printNomeExercício(n)
            
            #Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
            case 89:
                printNomeExercício(n)
            
            #Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
            case 90:
                printNomeExercício(n)
            
            #Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
            case 91:
                printNomeExercício(n)
            
            #Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
            case 92:
                printNomeExercício(n)
            
            #Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
            case 93:
                printNomeExercício(n)
            
            #Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
                #        A) Quantas pessoas foram cadastradas
                #        B) A média de idade
                #        C) Uma lista com as mulheres
                #        D) Uma lista de pessoas com idade acima da média.
            case 94:
                printNomeExercício(n)
            
            #Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
            case 95:
                printNomeExercício(n)
            
            #Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
            case 96:
                printNomeExercício(n)
            
            #Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
                #        Ex:
                #         escreva("Olá, Mundo!") Saída:
                #         Olá, Mundo!
                #        Veja o curso de Python PARTE 1 em https://www.youtube.com/playlist?list…
                #        Veja o curso de Python PARTE 2 em https://www.youtube.com/playlist?list…
                #         Veja o curso de Python PARTE 3 em https://www.youtube.com/watch?v=0LB3F…
                #         Veja a lista de exercícios de Python em https://www.youtube.com/playlist?list….
            case 97:
                printNomeExercício(n)
            
            #Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
                #        a) de 1 até 10, de 1 em 1
                #        b) de 10 até 0, de 2 em 2
                #        c) uma contagem personalizada.
            case 98:
                printNomeExercício(n)
            
            #Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
            case 99:
                printNomeExercício(n)
            
            #Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
            case 100:
                printNomeExercício(n)
            
            #Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
            case 101:
                printNomeExercício(n)
            
            #Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
            case 102:
                printNomeExercício(n)
            
            #Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
            case 103:
                printNomeExercício(n)
            
            #Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante "a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt("Digite um n: ").
            case 104:
                printNomeExercício(n)
            
            #Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
                #         – Quantidade de notas
                #         – A maior nota
                #         – A menor nota
                #         – A média da turma
                #         – A situação (opcional).
            case 105:
                printNomeExercício(n)
            
            #Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará. Importante: use cores.
            case 106:
                printNomeExercício(n)
            
            #Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.
            case 107:
                printNomeExercício(n)
            
            #Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
            case 108:
                printNomeExercício(n)
            
            #Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
            case 109:
                printNomeExercício(n)
            
            #Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
            case 110:
                printNomeExercício(n)
            
            #Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
            case 111:
                printNomeExercício(n)
            
            #Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(), mas com uma validação de dados para aceitar apenas valores que seja monetários.
            case 112:
                printNomeExercício(n)
            
            #Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
            case 113:
                printNomeExercício(n)
            
            #Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
            case 114:
                printNomeExercício(n)
            
            #Exercício Python 115a: Vamos criar um menu em Python, usando modularização.
            #Exercício Python 115b: Vamos ver como fazer acesso a arquivos usando o Python.
            #Exercício Python 115c: Vamos finalizar o projeto de acesso a arquivos em Python.
            case 115:
                printNomeExercício(n)

