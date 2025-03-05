''' 
Escreva uma expressão que será utilizada para decidir se um aluno foi ou não aprovado.
Para ser aprovado, todas as médias devem ser maiores ou iguais a 7.
Considere que o aluno cursa apenas três disciplinas, e que a nota de cada uma está armazenada nas variáveis "materia1, materia2, materia3"
''' 

materia1 = 4
materia2 = 7
materia3 = 10

media = (materia1 + materia2 + materia3) / 3
aprovado = media >= 7
if aprovado == True:
    print("=== Aprovado, não fez mais que a obrigação")
else:
    print("=== Reprovado, burrão!")