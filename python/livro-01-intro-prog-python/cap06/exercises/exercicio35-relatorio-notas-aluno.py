# PT-BR:
# Crie uma lista com sublistas, onde cada sublista contém:
# - o nome de um aluno (string)
# - uma lista com 3 notas (floats)
# Percorra essa estrutura usando for e mostre:
# - o nome do aluno
# - cada uma das 3 notas
# a média final

alunos = [
    ["Huguinho", [7, 8.5, 9.8]],
    ["Zezinho", [6.3, 10, 8]],
    ["Luizinho", [7, 7.1, 3]],
    ["Juquinha", [4, 1, 10]],
    ["Bola de Sebo", [3, 0, 7]]
]

for i in alunos:
    nome = i[0]
    notas = i[1]
    media = sum(notas) / len(notas)
    print(f"Aluno: {nome} - Notas: N1 = {notas[0]}, N2 = {notas[1]}, N3 = {notas[2]} - Média: {media:.2f}")