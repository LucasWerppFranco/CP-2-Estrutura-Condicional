def calcular_horas_extras(salario_base, horas):
    return horas * (0.015 * salario_base)

def calcular_descontos_faltas(salario_base, faltas):
    return faltas * (0.02 * salario_base)

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() == 's':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0


nome = input("Nome do funcionario: ")
print("Cargos: 1-Gerente, 2-Analista, 3-Assistente, 4-Estagiario")
cargo = int(input("Digite o codigo do cargo (1-4): "))
salario_base = float(input("Salario base: R$ "))
horas_extras = int(input("Total de horas extras trabalhadas: "))
faltas = int(input("Total de faltas no mes: "))
recebeu_bonus = input("Recebeu bonus por desempenho? (s/n): ")

valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

acrescimos = valor_horas_extras + valor_bonus
descontos = valor_descontos
salario_final = salario_base + acrescimos - descontos

print(f"Funcionario: {nome}")
print(f"Salario Bruto: R$ {salario_base:.2f}")
print(f"Acrescimos (horas extras + bonus): R$ {acrescimos:.2f}")
print(f"Descontos (faltas): R$ {descontos:.2f}")
print(f"Salario Final: R$ {salario_final:.2f}")
