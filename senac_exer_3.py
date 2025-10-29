"""

'''
Exercício 01
Transformação de strings
Dada uma lista de nomes, crie outra lista com os nomes em maiúsculas usando list comprehension



'''
nomes = ['Ana','carlos','MARIA','Raisa','Vitor']
nomesMaisculo = [n.upper() for n in nomes]

print(nomesMaisculo)



'''
02
Conversão e ordenação
Transforme uma tupla de números em lista e ordene os valores

'''
numerosTupla = (5,2,4,6,9,8,1,7,3)

numeroLista = sorted(numerosTupla)

print(numeroLista)


'''

03
Iteração em dicionário
Imprima chave e valor de um dicionário representando um aluno

'''
cadastro = {'Aluno':'Luis','Ano':25}


print(f'Itens: {cadastro.items()}')


"""




'''
04
Manipulação de strings
Faça um programa que receba uma frase e retorne uma lista de palavras usando split()
'''
paragrafo = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
c=0
i=0
print(len(paragrafo))
print(paragrafo[::-1])
print(paragrafo[::-1].find(' '))
print(len(paragrafo) - paragrafo[::-1].find(' '))
while c <= (len(paragrafo) - paragrafo[::-1].find(' ')):
    n = paragrafo[i:].find(' ')
    i = n
    c = c+1
print(n)
print(paragrafo[::])




'''
05
List comprehension avançado
Use list comprehension para criar uma lista com os comprimentos de cada palavra de uma frase
'''

