idade_minima = 17
idade_usuario = int(input("Digite a sua idade: "))
resposta_ingresso = input("Você possui ingresso? (sim/não): ").strip().lower()
tem_ingresso = resposta_ingresso == "sim"

# O acesso depende dos dois requisitos: idade mínima e ingresso.
if idade_usuario >= idade_minima and tem_ingresso:
    print("Acesso liberado! Divirta-se no evento.")
elif idade_usuario < idade_minima:
    print(f"Acesso negado. É necessário ter pelo menos {idade_minima} anos.")
else:
    print("Acesso negado. Apresente um ingresso válido para entrar.")

