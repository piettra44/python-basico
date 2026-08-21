# Programa que calcula a aprovação de um aluno com base em suas notas e número de faltas.
print("=== CALCULADORA DE APROVAÇÃO ===")

nome = input("Digite seu nome: ")

faltas = int(input("Digite o número de faltas: "))

nota1 = float(input("Digite a primeira nota: ").replace(",", "."))
nota2 = float(input("Digite a segunda nota: ").replace(",", "."))
nota3 = float(input("Digite a terceira nota: ").replace(",", "."))

media = (nota1 + nota2 + nota3) / 3

print()

if media >= 6 and faltas <=15:
    print("Resultado aluno", nome, ": Aprovado!")
else:
    print("Resultado aluno", nome, ": Reprovado!")