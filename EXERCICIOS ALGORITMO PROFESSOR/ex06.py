soma = 1
quantidade = 1

# ---------- CONDIÇÃO (loop principal) ----------
while True:
    print("\n===== MENU DO LOOP =====")
    print("1 - Informar um número")
    print("======================")
    print("2 - Ver soma e média")
    print("======================")
    print("3 - Sair")
    print("======================")

    
    opcao = input("Escolha uma opção: ").strip()

    if opcao not in ("1", "2", "3"):
        print("⚠️  Opção inválida! Tente novamente.")
        continue  # volta para o início do loop, ignorando o resto

    if opcao == "1":
        entrada = input("Digite um número (ou 'sair' para voltar ao menu): ").strip()

        # Permite cancelar a entrada e voltar ao menu sem travar o programa
        if entrada.lower() == "sair":
            print("Entrada cancelada. Voltando ao menu...")
            continue

        
        numero = int(entrada)

        # Usa 'continue' para ignorar números negativos
        if numero < 0:
            print("Número negativo ignorado.")
            continue

        # ---------- ATUALIZAÇÃO ----------
        soma += numero
        quantidade += 1
        print(f"Número {numero} registrado com sucesso!")

    elif opcao == "2":
        if quantidade == 0:
            print("Nenhum número positivo informado ainda.")
        else:
            media = soma / quantidade
            print(f"Soma atual: {soma}")
            print(f"Média atual: {media:.2f}")

    elif opcao == "3":
        # ---------- INTERRUPÇÃO ----------
        print("Encerrando o programa...")
        break

print("Programa finalizado. Até logo!")