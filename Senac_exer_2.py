
#Exercício 1 - verifique maior idade


def maiorIdade(idade):
    if idade >= 18:
        print('Você é maior de idade!')
    else:
        print('Você é menor de idade!')

def exercicio1():
    while True:
        try:
            idade = int(input('Olá, quantos anos você têm? '))
            if idade > 0:
                break
            else:
                print('Digite uma idade maior do que zero.')
        except ValueError:
            print("Ops! Digite uma idade válida. Tente novamente...")
    
    maiorIdade(idade)

# Exercó

def sistemaAprovacao(nota):
    if nota >= 7:
        print('Eu sabia, parabéns, você está aprovado!')
    else:
        print('Uma pena, você está reprovado, mas não fique triste, tente novamente!')

def exercicio2():
    while True:
        try:
            nota = int(input('Olá, qual foi a sua nota? '))
            if nota >= 0:
                break
            else:
                print('Sua nota não foi menor que zero, me diga a verdade! :(')
        except ValueError:
            print("Ops! Digitou uma nota invalida. Tente novamente...")
    
    sistemaAprovacao(nota)

# Exercício 3 - Classificador de Temperatura
def temperaturaAmbiente(temperatura):
    if temperatura > 25:
        print(f'Nossa {temperatura}°C é quente!')
    elif temperatura < 15:
        print(f'Nossa {temperatura}°C é frio!')
    else:
        print(f'A temperatura de {temperatura}°C é agradável!')


def classificadorTemperatura():
    while True:
        try:
            temperatura = int(input('Qual a temperatura em °C do ambiente?'))
            break
        except ValueError:
            print("Ops! Digitou uma temperatura invalida. Tente novamente...")
    
    temperaturaAmbiente(temperatura)

# Desafio da Aula
# Desenvolva uma função que receba o consumo de energia (em kWh) e retorne:
def consumoEnergia(consumo):
    if consumo > 200:
        print(f'Seu consumo é alto!')
    elif consumo < 100:
        print(f'Nossa seu consumo é baixo!')
    else:
        print(f'Seu consumo é moderado!')   

def desafio():
    while True:
        try:
            consumo = int(input('Qual o seu consumo de energia em kWh?'))
            if consumo >= 0:
                break
            else:
                print('Sua consumo não foi menor que zero, me diga a verdade! :(')
        except ValueError:
            print("Ops! Digitou uma nota invalida. Tente novamente...")
    
    consumoEnergia(consumo)



while True:
    try:
        print('Exercícios aula de python: \n 1 - verifique maior idade \n 2 - Sistema de Aprovação \n 3 - Classificador de Temperatura \n 4 - Desafio \n 0 - Cancelar \n \n')
        exercicio = int(input('Qual exercício deseja exercutar? '))
        if exercicio == 1:
            exercicio1()
        elif exercicio == 2:
            exercicio2()
        elif exercicio == 3:
            classificadorTemperatura()   
        elif exercicio == 4:
            desafio()         
        elif exercicio == 0:
            print('Obriagado por jogar, até em breve.')
            print('Criado por José Luís.')
            break
        else:
            print('Digite um valor de 1 a 4 para exercutar o exercício ou 0 para encerar.')
    except ValueError:
        print("Ops! Digite uma idade válida. Tente novamente...")




