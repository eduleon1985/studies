# 4 - Pegando apenas as letras em posições ímpares | Extracting only odd-positioned letters
# 📌 Português:
# Peça uma palavra ao usuário e exiba somente os caracteres que estão nas posições ímpares (começando do índice 0).

# 📌 English:
# Ask the user for a word and display only the characters in odd positions (starting from index 0).

palavra = input("Digite uma palavra qualquer: ")
letras_impares = palavra[1::2]
print(f"Letras em posições ímpares: {letras_impares}")