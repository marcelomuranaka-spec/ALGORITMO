print("=" * 50)
print("         SISTEMA DE COMPRAS")
print("=" * 50)

# Guarda o nome do cliente informado, sem espaços extras nas extremidades.
nome_cliente = input("Nome do cliente: ").strip()
# Guarda o nome do produto que será comprado.
nome_produto = input("Nome do produto: ").strip()
# Converte a quantidade informada para um número inteiro.
quantidade_produto = int(input("Quantidade: "))
# Converte o preço unitário informado para um número decimal.
preco_unitario = float(input("Preço unitário do produto: R$ "))
# Guarda o percentual de desconto como número decimal.
percentual_desconto = float(input("Percentual de desconto (%): "))

# Calcula o preço dos produtos antes da aplicação do desconto.
subtotal = preco_unitario * quantidade_produto
# Calcula quanto será descontado do subtotal.
valor_desconto = subtotal * (percentual_desconto / 100)
# Subtrai o desconto e calcula o valor final da compra.
valor_total = subtotal - valor_desconto

print(f"Nome do cliente: {nome_cliente}")
print(f"Produto: {nome_produto}")
print(f"Quantidade: {quantidade_produto}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Total da compra: R$ {valor_total:.2f}")

print("=" * 50)
print("         OBRIGADO PELA COMPRA!")
print("=" * 50)
