import os

restaurantes = [{'nome':'Penna', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Atira', 'categoria':'Italiana', 'ativo':True},
                {'nome':'Shabbaj', 'categoria':'Árabe', 'ativo':False}]

def exibir_nome_do_programa():
    """Exibe o nome do programa com arte Fstring"""

    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
    
def exibir_menu():
    """Exibe o menu de opções do programa"""

    print('1: Cadastrar restaurante')
    print('2: Listar restaurante')
    print('3: Selecionar Status')
    print('4: Finalizar programação')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def finalizar_programa():
    """Finaliza o programa com mensagem de encerramento"""
    exibir_subtitulo('Programa finalizado!')

def opcao_invalida():
    """Exibe mensagem de opção inválida"""
    
    print('Opção inválida!\n')
    input('Pressione qualquer tecla para voltar ao menu principal.')
    main()

def exibir_subtitulo(texto):
    """Exibe um subtítulo formatado com asteriscos e limpa a tela"""
    os.system('clear')
    linha = '*' * len(texto)
    print(linha)
    print('\n' + texto)
    print(linha)
    print()

def cadastrar_restaurante():
    """Cadastra um novo restaurante  e adiciona à lista de restaurantes
       input: nome e categoria do restaurante """
    
    exibir_subtitulo('Cadastro de restaurante')
    nome_restaurante = input('\nDigite o nome do restaurante: ')
    categoria = input('Digite a categoria do restaurante: ')
    if not nome_restaurante or not categoria:
        print('Nome e categoria são obrigatórios!')
        voltar_ao_menu_principal()
        return
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado com sucesso!')

    voltar_ao_menu_principal()

def listar_restaurantes():
    """Lista todos os restaurantes cadastrados com seus detalhes"""

    exibir_subtitulo('Lista de restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")

    for restaurante in (restaurantes):
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = "ativado" if restaurante['ativo'] else "desativado"
        print(f'- {nome_restaurante.ljust(22)} | {categoria.ljust(20)} | {ativo}')

    voltar_ao_menu_principal()

def alternar_status():
    """Altera o status de ativação/desativação de um restaurante
    imput: nome do restaurante 
    output: ativa ou desativa o restaurante"""

    exibir_subtitulo('Alterar status do restaurante')
    restaurante_encontrado = False
    nome_restaurante = input('Digite o nome do restaurante que deseja ativar/desativar: ')
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] # Se torna True
            mensagem = f"O restautarante {nome_restaurante} foi ativado com sucesso!" if restaurante['ativo'] else f"O restaurante {nome_restaurante} foi desativado com sucesso!"
            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')

    voltar_ao_menu_principal()

def escolher_opcao():
    """Escolhe a opção do menu e executa a função correspondente"""

    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        opcoes = {
            1: cadastrar_restaurante,
            2: listar_restaurantes,
            3: alternar_status,
            4: finalizar_programa
        }

        descricao_opcao = opcoes.get(opcao_escolhida, opcao_invalida)

        if callable(descricao_opcao):
            descricao_opcao()
        else:
            print(f'{descricao_opcao}')
    except:
        opcao_invalida()
    print(f'{descricao_opcao}')

def main():
    """Função principal que inicia o programa e exibe o menu"""

    os.system('clear')
    exibir_nome_do_programa()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()