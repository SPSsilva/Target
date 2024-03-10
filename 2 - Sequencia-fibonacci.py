S = int(input('Digite um número entre 0 a 1000: '))
F = 0
K = 1
L = 3
lista = []
for c in range(0, 20):
    G = F + K
    lista.append(G)
    F = K
    K = G
    L += 1
print(lista)
if S in lista:
    print('O número digitado pertence a sequência de fibonacci.')
else:
    print('Infelismente o número digitado não está na sequência de Fibonacci.')
