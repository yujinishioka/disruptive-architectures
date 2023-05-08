# Exercicio 04

i = 0
total = 0
qtd = 5
dados = []

while (i < (qtd - 1)):
    aux = int(input('Digite um valor: '))
    dados.append(aux)
    i = i + 1

print('------------------')

for dado in dados:
    total = total + dado
    dado_txt = str(dado)
    print('Valor digitado: ' + dado_txt)

print('Total: ', total)