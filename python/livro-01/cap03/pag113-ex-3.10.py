# PT-BR (🇧🇷): Faça um programa que calcule o aumento de um salário. 
# Ele deve solicitar o valor do salário e a porcentagem do aumento.
# Exiba o valor do aumento e do novo salário.

# EN (🇺🇸): Write a program that calculates a salary increase.
# It should ask for the salary amount and the percentage of the increase.
# Display the increase amount and the new salary.

salary = float(input("Enter your salary amount: "))
increase = float(input("Enter the percentage of the increase: "))
increase_amount = (salary * increase) / 100
new_salary = salary + ((salary * increase) / 100)
print(f"Salary amount: {salary}")
print(f"Percentage of increase: {increase}%")
print(f"Increase amount: {increase_amount}")
print(f"New salary: {new_salary}")