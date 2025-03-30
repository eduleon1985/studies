### PT-BR (🇧🇷): 
'''
Crie uma lista com sublistas contendo o nome de um aluno (string) e 
uma string com três letras representando suas notas (ex: "ABC"). 
Em seguida, percorra a lista e imprima o nome do aluno junto com cada uma
 das notas separadamente, acessando letra por letra usando índices duplos.
'''
### EN (🇺🇸):
'''
Create a list of sublists, where each sublist contains a student's name (string) and 
a string with three characters representing their grades (e.g., "ABC"). '
'Then, loop through the list and print the student's name along with each grade 
separately by accessing characters using double indexing.
'''

alunos = [
    ["Eduardo", [8.5, 9, 10]],
    ["Carol", [10, 9.5, 10]],
    ["Rafa", [10, 10, 10]]
]

for i in alunos:
    nome = i[0]
    notas = i[1]
    print("=" * 50)
    print(f"{nome}, Nota 1: {notas[0]}, Nota 2: {notas[1]}, Nota 3: {notas[2]}")