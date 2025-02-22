# Extraindo a extensão de um arquivo
# 📌 Português:
# Peça ao usuário para digitar um nome de arquivo com sua extensão (exemplo: "documento.pdf").
# Exiba apenas a extensão do arquivo.

arquivo = input("Magnata, qual é o arquivo que você tem aí? Quero o nome e a extensão, por favor: ")
extensao = arquivo[arquivo.index("."):]
print(f"A extensão do arquivo é {extensao}")