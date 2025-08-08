#  Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
valor1 = input("Digite o primeiro valor booleano (True/False): ").lower() == 'true'
valor2 = input("Digite o segundo valor booleano (True/False): ").lower() == 'true'
resultado_and = valor1 and valor2
print(f"O resultado da operação AND é: {resultado_and}")
print('\n' + '-'*30 + '\n')
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = input("Digite o primeiro valor booleano (True/False): ").lower() == 'true'
valor2 = input("Digite o segundo valor booleano (True/False): ").lower() == 'true'
resultado_or = valor1 or valor2
print(f"O resultado da operação OR é: {resultado_or}")
print('\n' + '-'*30 + '\n')
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor = input("Digite um valor booleano para inverter (True/False): ").lower() == 'true'
valor_invertido = not valor
print(f"O valor invertido é: {valor_invertido}")
print('\n' + '-'*30 + '\n')
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
sao_iguais = num1 == num2
print(f"Os números são iguais? {sao_iguais}")
print('\n' + '-'*30 + '\n')
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
sao_diferentes = num1 != num2
print(f"Os números são diferentes? {sao_diferentes}")