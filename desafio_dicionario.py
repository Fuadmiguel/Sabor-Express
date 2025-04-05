pessoa  = {
    'nome' : 'Felipe',
    'idade' : 22,
    'cidade' : 'Goiania'
}
digite = input('Digite o nome: ')
if pessoa['nome'] == digite:
    print("O nome está no dicionário")
else:
    print('Não existe no dicionário')

alterar_nome = input('Digite o novo nome: ')
pessoa['nome'] = alterar_nome
print(f'{pessoa}')

pessoa['profissao'] = 'programador'
del pessoa['cidade']

numeros_quadrados = {x: x**2 for x in range(1, 6)}
print(numeros_quadrados)

teste = {'tempo' : 'Dia'}
input_tempo = input(f'Como está o tempo? ')
if input_tempo == teste['tempo']:
    print('Existe!')
else:
    print('Não existe!')

frase = "Abedudada de lá"
contagem = {}
for letra in frase:
    if letra.isalpha():
        contagem[letra] = contagem.get(letra, 0) + 1
print(f'Contagem de letras: {contagem}')
