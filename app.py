import os

restaurantes = [{'nome':'Sabor','tipo':'Variados','status':True},
                {'nome':'Pastel','tipo':'Pastelaria','status':True},
                {'nome':'Sushi','tipo':'Japones','status':False}
                ]

def exibir_titulo():
    print('Sabor Express\n')

def finalizar_app():
    print('Finalizando o app')

def opcao_invalida():
    print('Opcão Invalida!')
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def voltar_menu():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def listar_restaurante():
    for rest in restaurantes:
        nome_rest = rest['nome']
        status = 'ativado' if rest['status'] else 'desativado'
        tipo = rest['tipo']
        print(f'{nome_rest.ljust(20)} | {status.ljust(20)} | {tipo}')
    voltar_menu()

def alternar_status_restaurante():
    print('Alterando o status do Restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['status'] = not restaurante['status']
            mensagem = f'O restaurente {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('Restaurante não encontrado')
    
    voltar_menu()

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair')

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_restaurante = {'nome': nome_do_restaurante, 'tipo':categoria,'status': False}
    restaurantes.append(dados_restaurante)
    voltar_menu()
    

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        print("Você escolheu a opção" ,opcao_escolhida)



        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida ==2:
            listar_restaurante()
        elif opcao_escolhida ==3:
            alternar_status_restaurante()
        elif opcao_escolhida ==4:
            finalizar_app()
        else:
                opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_titulo()
    exibir_opcoes()
    escolher_opcao()


if __name__ == '__main__':
    main()