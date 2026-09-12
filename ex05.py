usuarios_cadastrados = ("Daniela", "Roberta", "Joana")
termos_disponiveis = ("python", "java", "c++")

nome_usuario = input("Digite o nome do usuário: ").strip()
if nome_usuario in usuarios_cadastrados:
    print("Usuário autenticado com sucesso!")
else:
    print("Usuário não encontrado. Acesso negado.")
    raise SystemExit

termo_pesquisa = input("Digite o termo de pesquisa: ").strip().lower()
if termo_pesquisa in termos_disponiveis:
    print("Termo encontrado!")
else:
    print("Termo não encontrado.")
    raise SystemExit

opcao_sessao = input("Digite 'sair' ou 'continuar' para encerrar a sessão: ").strip().lower()
if opcao_sessao == "sair":
    print("Sessão encerrada. Até logo!")
elif opcao_sessao == "continuar":
    print("A sessão continuará.")
else:
    print("Opção inválida. A sessão continuará.")

