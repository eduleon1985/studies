### PT-BR (🇧🇷): 
# Reescreva o programa a seguir com if-elif-else

### EN (🇺🇸):  
# Rewrite the following program using if-elif-else.  

''''
hora = int(input("Informe a hora: "))
if hora < 12:
    print("Bom dia")
if hora >= 12 and hora <= 18:
    print("Boa tarde")
if hora >= 18:
    print("Boa noite")
'''

hora = int(input("Informe a hora: "))

if hora < 12:
    print("Bom dia")
elif hora >= 12 and hora < 18:
    print("Boa tarde")
else:
    print("Boa noite")