# Programa que exibe a tabuada de um número fornecido pelo usuário.
print("=== TABUADA ===")

numero = int(input("Digite o número que deseja ver a tbuada: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

