# 3 - Invertendo uma palavra | Reversing a word
# 📌 Português:
# Peça ao usuário para digitar uma palavra e exiba essa palavra ao contrário.

# 📌 English:
# Ask the user to enter a word and display that word in reverse order.

palavra = input("Digite uma palavra qualquer: ")
palavra_invertida = palavra[::-1]
print(f"A palavra {palavra} invertida é {palavra_invertida}")
