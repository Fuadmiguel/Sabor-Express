números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Lucas', 'Ana', 'João', 'Maria', 'Pedro']
Nascimento = [2003, 2025]

for numero in números:
    print(int(numero))
else :
    print('Número inválido')

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

for i in range(10, 0, -1):
    print(i)

numero = input(int('Digite um número: '))
for i in range(1, 11):
    resultado = (numero) * i
    print(f'{numero} x {i} = {resultado}')

lista = [1, 2, 3, 4, 5]
soma = 0

try:
    for numero in range(lista):
        soma += numero
    print(f'A soma dos números é: {soma}')
except Exception as e:
        print(f'Ocorreu um erro: {e}')

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
     for valor in lista_valores:
        soma_valores += valor
        media = soma_valores / len(lista_valores)
        print(f'A média dos valores é: {media}')
except ZeroDivisionError:
    print('Não é possível dividir por zero.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')