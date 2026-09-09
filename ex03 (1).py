print("=" * 50)
print("         SISTEMA DE COMPRAS")
print("=" * 50)

nome_cliente = input('Nome do cliente: ')
produto = input('Nome do produto: ')
quantidade = int(input('Quantidade:'))
preco = float(input('Preço do produto: '))
percentual_desconto = float(input('Percentual de desconto (em%): '))

subtotal = preco * quantidade
desconto = subtotal * (percentual_desconto / 100)
total = subtotal - desconto 

print(f"Nome do cliente: {nome_cliente}")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade}")
print(f'Preço unitário: R${preco:.2f}')
print(f"Subtotal: R${subtotal:.2f}")
print(f"Desconto: R${desconto:.2f}")
print(f"Total: R${total:.2f}")

print("=" * 50)
print("         OBRIADO PELA COMPRA!")
print("=" * 50)