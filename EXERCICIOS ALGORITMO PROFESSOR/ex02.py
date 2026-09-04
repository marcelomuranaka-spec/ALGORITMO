titulo = "Calculo do carrinho"
descricao = "João comprou dois livros na Livraria, cada um por"
cont = "O desconto aplicado foi de:"
pergunta = "Quanto ele gastou no total?"
resposta = "O valor final da compra foi de: "
preco = 35.00
quantidade = 2
desconto = 10.00

valor_total = preco * quantidade
valor_desconto = valor_total - desconto
valor_final = valor_desconto

print(f"""
{titulo}
{descricao}R$ {preco:.2f}.{cont}R$ {desconto:.2f}
{pergunta}
{resposta}R$ {valor_final:.2f}
""")