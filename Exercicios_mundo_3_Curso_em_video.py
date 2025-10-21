from numpy.ma.core import not_equal

Inout = "\n######################################################################################################\n"

Resp = "RESPOSTA:\n"

#--------------------------------------------------------------------------------------------------------------------------------------
# EXERCISES ONE WORLD
#---------------------------------------------------------------------------------------------------------------------------------------#
Fim = 1
while Fim != 0:
    n = int(input('\nDigite de 36 a 71 para ver os exercícios ou 0 para encerrar\nQual Exercício executar? '))
    if n == 0:
        print("Volte Sempre!")
        Fim = 0
    elif 72<= n <= 117:
        match n:
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




            case 73:
                print(Inout,Inout,Inout,Inout,Resp)
                x = "Python"
                y = "is"
                z = "awesome"
                print(x, y, z)

            case 74:
                print(Inout,Inout,Inout,Inout,Resp)
            case 75:
                print(Inout,Inout,Inout,Inout,Resp)
""""
            case 76:
                print(Inout,Inout,Ex076,Inout,Inout,Resp)
            case 77:
                print(Inout,Inout,Ex077,Inout,Inout,Resp)
            case 78:
                print(Inout,Inout,Ex078,Inout,Inout,Resp)
            case 79:
                print(Inout,Inout,Ex079,Inout,Inout,Resp)
            case 80:
                print(Inout,Inout,Ex080,Inout,Inout,Resp)
            case 81:
                print(Inout,Inout,Ex081,Inout,Inout,Resp)
            case 82:
                print(Inout,Inout,Ex082,Inout,Inout,Resp)
            case 83:
                print(Inout,Inout,Ex083,Inout,Inout,Resp)
            case 84:
                print(Inout,Inout,Ex084,Inout,Inout,Resp)
            case 85:
                print(Inout,Inout,Ex085,Inout,Inout,Resp)
            case 86:
                print(Inout,Inout,Ex086,Inout,Inout,Resp)
            case 87:
                print(Inout,Inout,Ex087,Inout,Inout,Resp)
            case 88:
                print(Inout,Inout,Ex088,Inout,Inout,Resp)
            case 89:
                print(Inout,Inout,Ex089,Inout,Inout,Resp)
            case 90:
                print(Inout,Inout,Ex090,Inout,Inout,Resp)
            case 91:
                print(Inout,Inout,Ex091,Inout,Inout,Resp)
            case 92:
                print(Inout,Inout,Ex092,Inout,Inout,Resp)
            case 93:
                print(Inout,Inout,Ex093,Inout,Inout,Resp)
            case 94:
                print(Inout,Inout,Ex094,Inout,Inout,Resp)
            case 95:
                print(Inout,Inout,Ex095,Inout,Inout,Resp)
            case 96:
                print(Inout,Inout,Ex096,Inout,Inout,Resp)
            case 97:
                print(Inout,Inout,Ex097,Inout,Inout,Resp)
            case 98:
                print(Inout,Inout,Ex098,Inout,Inout,Resp)
            case 99:
                print(Inout,Inout,Ex099,Inout,Inout,Resp)
            case 100:
                print(Inout,Inout,Ex100,Inout,Inout,Resp)
            case 101:
                print(Inout,Inout,Ex101,Inout,Inout,Resp)
            case 102:
                print(Inout,Inout,Ex102,Inout,Inout,Resp)
            case 103:
                print(Inout,Inout,Ex103,Inout,Inout,Resp)
            case 104:
                print(Inout,Inout,Ex104,Inout,Inout,Resp)
            case 105:
                print(Inout,Inout,Ex105,Inout,Inout,Resp)
            case 106:
                print(Inout,Inout,Ex106,Inout,Inout,Resp)
            case 107:
                print(Inout,Inout,Ex107,Inout,Inout,Resp)
            case 108:
                print(Inout,Inout,Ex108,Inout,Inout,Resp)
            case 109:
                print(Inout,Inout,Ex109,Inout,Inout,Resp)
            case 110:
                print(Inout,Inout,Ex110,Inout,Inout,Resp)
            case 111:
                print(Inout,Inout,Ex111,Inout,Inout,Resp)
            case 112:
                print(Inout,Inout,Ex112,Inout,Inout,Resp)
            case 113:
                print(Inout,Inout,Ex113,Inout,Inout,Resp)
            case 114:
                print(Inout,Inout,Ex114,Inout,Inout,Resp)
            case 115:
                print(Inout,Inout,Ex115,Inout,Inout,Resp)"""

