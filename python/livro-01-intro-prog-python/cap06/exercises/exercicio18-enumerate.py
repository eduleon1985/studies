# PT-BR (🇧🇷):
# Crie uma lista com 5 tarefas.
# Use a função enumerate e um for para exibir as tarefas com sua numeração, assim:
# "1 - Comprar pão"
# "2 - Estudar Python"
# ...

# EN (🇺🇸):
# Create a list with 5 tasks.
# Use the enumerate function and a for loop to display the tasks with their numbering, like:
# "1 - Buy bread"
# "2 - Study Python"
# ...

Tasks = ["Oração matinal", "Higiene pessoal", "Leitura espiritual", "Exercício físico", "Café da manhã em família"]

for i, tarefas in enumerate(Tasks):
    print(f"{i} - {tarefas}")