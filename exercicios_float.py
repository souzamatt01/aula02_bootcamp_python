# Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_1 = float(input('Digite um número decimal: '))
num_2 = float(input('Digite um segundo número decimal: '))
soma_float = num_1 + num_2
print(f"A soma dos números decimais é: {soma_float}")
print('\n' + '-'*30 + '\n')
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_1 = float(input('Digite um número decimal: '))
num_2 = float(input('Digite um segundo número decimal: '))
media_float = (num_1 + num_2) / 2 
print(f"A média dos números decimais é: {media_float}")
print('\n' + '-'*30 + '\n')
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
num_base = float(input("Digite o valor da base: "))
num_expoente = float(input("Digite o valor do expoente: "))
potencia = num_base ** num_expoente
print("O resultado da potência é:", potencia)
print('\n' + '-'*30 + '\n')
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
conversao_fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a: {conversao_fahrenheit}°F")
print('\n' + '-'*30 + '\n')
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o valor do raio: "))
area = 3.14159 * raio ** 2
print(f"A área do círculo é:", {area})