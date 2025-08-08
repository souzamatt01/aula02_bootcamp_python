# Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
texto = str(input("Digite um texto: "))
texto_upper = texto.upper()
print(f"Texto em caixa alta: {texto_upper}")
print('\n' + '-'*30 + '\n')
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
user_name = str(input("Digite o seu nome: "))
user_name_upper = user_name.upper()
print(f"Seu nome em caixa alta: {user_name_upper}")
print('\n' + '-'*30 + '\n')
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços no início e no final:, {frase_sem_espacos}")
print('\n' + '-'*30 + '\n')
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
print('\n' + '-'*30 + '\n')
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
texto1 = input("Digite a primeira parte do texto: ")
texto2 = input("Digite a segunda parte do texto: ")
texto_concatenado = texto1 + texto2
print("Texto concatenado:", texto_concatenado)