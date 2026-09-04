usuarios = ( 'Daniela', 'Roberta', 'Joana') # valores correspondentes aos usuários cadastrados
termos = ('python', 'java', 'c++') # valores correspondentes aos termos de pesquisa
sessoes = ('sair', 'continuar') # valor correspondente à opção de sair

usuario = input("Digite o nome do usuário: ")
if usuario in usuarios:
    print("Usuário autenticado com sucesso!")
else:
    print("Usuário não encontrado. Acesso negado.")
    exit()

termo = input("Digite o termo de pesquisa: ")
if termo in termos:
    print("Termo encontrado!")
else:
    print("Termo não encontrado.")  
    exit()

sessoes = input("Digite 'sair' ou 'continuar' caso deseje encerrar a sua sessão: ")
if sessoes == 'sair':
    print("Sessão encerrada. Até logo!")
else:
    print("A sessão continuará.")

