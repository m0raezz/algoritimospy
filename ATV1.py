

#DEFINIÇÃO DA FUNÇÃO
def soma(L):
    L=sum(L)
    print(f'A soma é {L}')

#DEFINIÇÃO DA FUNÇÃO MED
def med(A):
    A = sum(A) / len(A)
    print('A média é',A)







#Criação da lista
lista = []

for a in range(5):
    lista.append(int(input('Selecione um número: ')))

soma(lista)
med(lista)
