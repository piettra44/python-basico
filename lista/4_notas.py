# Programa que armazena as notas de 5 aluos de uma turma
# Utilizando o for pra percorrer
# Tbm vai calcular a média da turma e exibir a maior nota e a menor nota

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)
    

media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

print(f"\nMédia da turma: {media}")
print(f"Maior nota: {maior_nota}")
print(f"Menor nota: {menor_nota}")