# Inteiros ('int')

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_1 = int(input('Digite um número inteiro a ser somado: '))
num_2 = int(input('Digite um segundo número inteiro a ser somado: '))
soma = num_1 +num_2
print(f'O resultado da soma é: {soma}')

print('\n' + '-'*30 + '\n')
# 2.  Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input('Digite um número: '))
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

print('\n' + '-'*30 + '\n')
# 3.  Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num_1 = float(input('Digite um número  a ser multiplicado: '))
num_2 = float(input('Digite um segundo número  a ser multiplicado: '))
multiplicacao = num_1 * num_2
print(f'O resultado da multiplicação é:, {multiplicacao}')

print('\n' + '-'*30 + '\n')
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_1 = (int(input('Digite um número inteiro a ser divido: ')))
num_2 = (int(input('Digite o segundo número a ser divido: ')))
divisao_inteira = num_1 // num_2
print(f'O resultado da divisão inteira é: {divisao_inteira}')

print('\n' + '-'*30 + '\n')
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = float(input('Digite um número: '))
num_ao_quadrado = num ** 2
print(f'O número ao quadrado é : {num_ao_quadrado}')