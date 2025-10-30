
'''
    Exercício 01
    Transformação de strings
    Dada uma lista de nomes, crie outra lista com os nomes em maiúsculas usando list comprehension

'''
def exercicio1():
    nomes = ['Ana','carlos','MARIA','Raisa','Vitor']
    nomesMaisculo = [n.upper() for n in nomes]

    print(nomesMaisculo)



'''
    02
    Conversão e ordenação
    Transforme uma tupla de números em lista e ordene os valores
'''
# ========================================
def exercicio2():
    numerosTupla = (5,2,4,6,9,8,1,7,3)

    numeroLista = sorted(numerosTupla)

    print(numeroLista)
# ========================================

'''

    03
    Iteração em dicionário
    Imprima chave e valor de um dicionário representando um aluno

'''
# ========================================
def exercicio3():
    cadastro = {'Aluno':'Luis','Ano':25}


    print(f'Itens: {cadastro.items()}')
# ========================================

'''
    04
    Manipulação de strings
    Faça um programa que receba uma frase e retorne uma lista de palavras usando split()

'''

# ========================================
def palavrasDoTexto(paragrafo):
    i = n = 0
    listaPalavras = []
    while True:
        n = paragrafo[i:].find(' ')
        if n >=0:
            listaPalavras.append(paragrafo[i:(n+i)])
            i += n + 1
        elif n == -1:
            listaPalavras.append(paragrafo[i:])    
            break
        else:
            print('Entrada inválida')
    return listaPalavras

def exercicio4():

    paragrafo = input('Digite o texto: \n   ')
    print(palavrasDoTexto(paragrafo))


    listaPalavraSplit = paragrafo.split(' ')    
    print(f'splite: {listaPalavraSplit} ')

# ========================================

'''
05
List comprehension avançado
Use list comprehension para criar uma lista com os comprimentos de cada palavra de uma frase
'''
def exercicio5():
    texto = input('Digite o texto: \n   ')
    lista = []
    listapalavra = []
    c = 0
    for n in texto:
        if n == ' ':
            print (n)
            lista.append(c)
            c = 0
        else:
            c += 1



    print(lista)



"""
receber o texto
reconhecer o espaço que tem no texto

"""
# ========================================
#                                        #
#      GERENCIADOR DE EXERCÍCIOS         #
#                                        #
# ========================================
while True:
    try:
        print('\nExercícios 3° aula de python: \n 01 - Transformação de strings\n 02 - Conversão e ordenação \n 03 - Iteração em dicionário \n 04 - Manipulação de strings \n 05 - List comprehension avançado \n 0 - Cancelar \n \n')
        exercicio = int(input('Qual exercício deseja exercutar? '))
        if exercicio == 1:
            exercicio1()
        elif exercicio == 2:
            exercicio2()
        elif exercicio == 3:
            exercicio3()
        elif exercicio == 4:
            exercicio4()         
        elif exercicio == 5:
            exercicio5()  
        elif exercicio == 0:
            print('Obriagado por jogar, até em breve.')
            print('Criado por José Luís.')
            break
        else:
            print('Digite um valor de 1 a 5 para exercutar o exercício ou 0 para encerar.')
    except ValueError:
        print("Ops! Digite uma idade válida. Tente novamente...")