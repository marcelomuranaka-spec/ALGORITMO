print("=" * 50)
print("         SISTEMA DE COMPRAS")
print("=" * 50)

nome_cliente = input("Nome do cliente: ").strip()
nome_produto = input("Nome do produto: ").strip()
quantidade_produto = int(input("Quantidade: "))
preco_unitario = float(input("Preço unitário do produto: R$ "))
percentual_desconto = float(input("Percentual de desconto (%): "))

subtotal = preco_unitario * quantidade_produto
valor_desconto = subtotal * (percentual_desconto / 100)
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
