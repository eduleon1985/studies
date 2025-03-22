### PT-BR (🇧🇷): 
# Crie uma lista com nomes de alunos e outra com suas respectivas notas.
# Use a função zip e um for para exibir a seguinte frase para cada par:
# "O aluno [nome] tirou nota [nota]."

### EN (🇺🇸):
# Create a list with student names and another with their respective grades.
# Use the zip function and a for loop to display the following message for each pair:
# "Student [name] scored [grade]."

alunos = ["Rafinha", "Mari", "Mariazinha", "Clarinha"]
notas = 10, 9, 8, 7

for i, j in zip(alunos, notas):
    print(f"Nome: {i} - Nota: {j}")