# Tupla com os nomes que podem acessar o sistema.
usuarios_cadastrados = ("Daniela", "Roberta", "Joana")
# Tupla com os termos de pesquisa aceitos pelo sistema.
termos_disponiveis = ("python", "java", "c++")

# Guarda o nome digitado para verificar se o usuário está cadastrado.
nome_usuario = input("Digite o nome do usuário: ").strip()
if nome_usuario in usuarios_cadastrados:
    print("Usuário autenticado com sucesso!")
else:
    print("Usuário não encontrado. Acesso negado.")
    raise SystemExit

# Guarda o termo informado, removendo espaços e padronizando letras minúsculas.
termo_pesquisa = input("Digite o termo de pesquisa: ").strip().lower()
if termo_pesquisa in termos_disponiveis:
    print("Termo encontrado!")
else:
    print("Termo não encontrado.")
    raise SystemExit

# Guarda a escolha do usuário para encerrar ou continuar a sessão.
opcao_sessao = input("Digite 'sair' ou 'continuar' para encerrar a sessão: ").strip().lower()
if opcao_sessao == "sair":
    print("Sessão encerrada. Até logo!")
elif opcao_sessao == "continuar":
    print("A sessão continuará.")
else:
    print("Opção inválida. A sessão continuará.")

