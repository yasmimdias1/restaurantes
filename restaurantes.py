import os
while True:
    restaurantes=[{'nome': 'aaa','categoria': 'lanche', 'ativo': False},
                {'nome': 'bbb','categoria': 'lanche', 'ativo': False},
                {'nome': 'ccc','categoria': 'lanche', 'ativo': False}]

    def exibir_opcoes():
        print('1. Cadastrar restaurante')
        print('2. Listar restaurante')
        print('3. Ativar restaurante')
        print('4. Sair')

    def cadastrar_restaurante():
        nome_restaurante=input('insira o nome do restaurante: ')
        categoria_restaurante=input('insira a categoria do restaurante: ')
        dados_restaurante=[{'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo': False}]
        restaurantes.append(dados_restaurante)
        print('restaurante adicionado com sucesso\n')

    def listar_restaurantes():
        for restaurante in restaurantes:
            nome_restaurante = restaurante['nome']  
            categoria_restaurante = restaurante['categoria'] 
            situacao_restaurante = restaurante['ativo'] 
            print(f'- {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {situacao_restaurante}')

    def ativar_restaurante():
        nome_restaurante=input('insira o nome do restaurante: ')
        restaurante_encontrado=False  
        for restaurante in restaurantes:
            if nome_restaurante==restaurante['nome']:
                restaurante_encontrado=True  
                restaurante['ativo']= not restaurante['ativo']
                print('seu restaurante foi ativado/desativado')
        if not restaurante_encontrado:
            print('O restaurante não foi encontrado')
    
    def sair():
        os.system('cls')
        main()

    def main():
        exibir_opcoes()   
        opcao=int(input('escolha a opcao do q deseja fazer\n'))
        if opcao==1:
            print('opcao 1 selecionada -> Cadastrar restaurante\n')
            cadastrar_restaurante()
        
        elif opcao==2:
            print('opcao 2 selecionada -> Listar restaurante\n')
            listar_restaurantes()

        elif opcao==3:
            print('opcao 3 selecionada -> Ativar restaurante\n')
            ativar_restaurante()

        elif opcao==4: 
            sair()

    main()