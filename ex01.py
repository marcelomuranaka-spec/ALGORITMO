# Guarda o nome informado pelo usuário como texto.
nome_usuario = input("Qual é o seu nome? ").strip()
print(f"Olá, {nome_usuario}!")

# A multiplicação é realizada antes da adição quando não há parênteses.
# Guarda o resultado de 5 + 7 * 2, respeitando a prioridade matemática.
resultado_sem_parenteses = 5 + 7 * 2
# Guarda o resultado de (5 + 7) * 2, em que os parênteses alteram a ordem.
resultado_com_parenteses = (5 + 7) * 2

print(f"Resultado sem parênteses: {resultado_sem_parenteses}")
print(f"Resultado com parênteses: {resultado_com_parenteses}")

