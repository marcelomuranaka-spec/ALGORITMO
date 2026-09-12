titulo = "Cálculo do carrinho"
nome_cliente = "João"
preco_unitario = 35.00
quantidade_livros = 2
valor_desconto = 10.00

valor_total_sem_desconto = preco_unitario * quantidade_livros
valor_total_com_desconto = valor_total_sem_desconto - valor_desconto

print(titulo)
print(f"{nome_cliente} comprou {quantidade_livros} livros por R$ {preco_unitario:.2f} cada.")
print(f"Total sem desconto: R$ {valor_total_sem_desconto:.2f}")
print(f"Desconto aplicado: R$ {valor_desconto:.2f}")
print(f"Valor final da compra: R$ {valor_total_com_desconto:.2f}")