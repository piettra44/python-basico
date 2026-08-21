# Programa de calcular imc
peso = float(input("Digite o peso (kg): ").replace(",", "."))
altura = float(input("Digite a altura (m): ").replace(",", "."))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"\nIMC: {imc:.2f} - Abaixo do peso")

elif 18.5 <= imc < 24.9:
    print(f"\nIMC: {imc:.2f} - Peso normal")

elif 25 <= imc < 29.9:
    print(f"\nIMC: {imc:.2f} - Sobrepeso")

elif 30 <= imc < 39.9:
    print(f"\nIMC: {imc:.2f} - Obesidade")

else: 
    print(f"\nIMC: {imc:.2f} - Obesidade grave")