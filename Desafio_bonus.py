# Solicitando o nome ao usuário:
try:
    nome = input("Digite seu nome: ")

    # Verificando se a entrada foi feita de fomra correta:
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    # Verificando se há algum número no nome:
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        print("Nome válido:", nome)
except ValueError as e:
    print(e)

# Solicitando o valor do salário e convertendo para float:

try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

# Solicitando o valor do bônus e convertendo para float:
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

# Assumindo uma lógica de cálculo para o bônus final e KPI
bonus_final = bonus_recebido * 1.2  # Exemplo
kpi = (salario + bonus_final) / 1000  # Exemplo

# Imprimindo as informações para o usuário:
print(f"Seu KPI é: {kpi:.2f}")
print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_final:.2f}.")
print('\n' + '-'*30 + '\n')
