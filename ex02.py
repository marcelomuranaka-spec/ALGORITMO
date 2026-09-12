# Texto usado como título da apresentação do resultado.
titulo = "Cálculo do carrinho"
# Nome do cliente da compra.
nome_cliente = "João"
# Preço de cada livro, armazenado como número decimal.
preco_unitario = 35.00
# Quantidade de livros comprados.
quantidade_livros = 2
# Valor fixo retirado da compra como desconto.
valor_desconto = 10.00

# Multiplica o preço de um livro pela quantidade comprada.
valor_total_sem_desconto = preco_unitario * quantidade_livros
# Subtrai o desconto do valor total para obter o preço final.
valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

print(titulo)
print(f"{nome_cliente} comprou {quantidade_livros} livros por R$ {preco_unitario:.2f} cada.")
print(f"Total sem desconto: R$ {valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_total_com_desconto:.2f}")