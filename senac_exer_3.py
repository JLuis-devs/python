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







'''
04
Manipulação de strings
Faça um programa que receba uma frase e retorne uma lista de palavras usando split()
'''
paragrafo = 'Python also includes a data type for sets. A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.'


n = paragrafo.find(' ')
print(n)
print(paragrafo[::2])


'''
05
List comprehension avançado
Use list comprehension para criar uma lista com os comprimentos de cada palavra de uma frase
'''

