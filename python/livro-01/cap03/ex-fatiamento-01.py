# 1 - Pegando a primeira metade de uma palavra | Getting the first half of a word
# 📌 Português:
# Peça ao usuário para digitar uma palavra e exiba apenas a primeira metade dos caracteres.
# Se o número de caracteres for ímpar, arredonde para baixo.
# 📌 English:
# Ask the user to enter a word and display only the first half of the characters.
# If the number of characters is odd, round down.

palavra = input("Digite uma palavra qualquer: ")
metade = len(palavra) // 2
primeira_metade = palavra[:metade]
print(f"Primeira metade da palavra {palavra} é {primeira_metade}")