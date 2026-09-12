# Define a idade mínima exigida para entrar no evento.
idade_minima = 17
# Converte a idade digitada pelo usuário para um número inteiro.
idade_usuario = int(input("Digite a sua idade: "))
# Guarda a resposta sobre o ingresso, removendo espaços e convertendo para minúsculas.
resposta_ingresso = input("Você possui ingresso? (sim/não): ").strip().lower()
# Recebe True quando a resposta for "sim" e False em qualquer outro caso.
tem_ingresso = resposta_ingresso == "sim"

# O acesso depende dos dois requisitos: idade mínima e ingresso.
if idade_usuario >= idade_minima and tem_ingresso:
    print("Acesso liberado! Divirta-se no evento.")
elif idade_usuario < idade_minima:
    print(f"Acesso negado. É necessário ter pelo menos {idade_minima} anos.")
else:
    print("Acesso negado. Apresente um ingresso válido para entrar.")

