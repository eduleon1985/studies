### PT-BR (🇧🇷): 
# Corrija o programa a seguir.

### EN (🇺🇸):  
# Fix the following program.

'''
Me dei a liberdade de criar um enunciado para o programa, pois isso torna o entendimento mais fácil.
Crie um programa que lê a média.
< 4 = reprovado
< 7 = recuperação
> 7 = aprovado
'''

media = int(input("Qual foi sua média? "))

if media < 4:
    print("Reprovado")
elif (media >= 4) and (media < 7):
    print("Em recuperação")
else:
    print("Aprovado")