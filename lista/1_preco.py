# Atividade 1 - Preço
# Programa que lê o preço de um produto e a quantidade comprada
# e calcula o valor total da compra (preço * quantidade), aplicando um desconto de 10% se o valor for maior que R$ 200,00.

# Lê o preço do produto
preco = float(input("Digite o preço do produto: "))

# Lê a quantidade comprada
quantidade = int(input("Digite a quantidade comprada: "))

# Calcula o valor total da compra
valor_total = preco * quantidade

# Aplica desconto de 10% se o valor total for maior que R$ 200,00
if valor_total > 200:
    desconto = valor_total * 0.10
    valor_total -= desconto
    print(f"Desconto de 10% aplicado com sucesso! \nValor total com desconto: R$ {valor_total:.2f}")

else: 
    print(f"Valor total da compra: R$ {valor_total:.2f}")