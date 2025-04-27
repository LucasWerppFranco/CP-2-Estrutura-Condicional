'''
    Sistema de Banco para Análise de Clientes
'''
def aprovacao(idade, renda, valor_emprestimo, n_parcelas):
    if idade <= 18:
        return False
    if valor_emprestimo > 15 * renda:
        return False
    valor_parcelas = valor_emprestimo / n_parcelas
    if valor_parcelas < 100 or valor_parcelas > 2000:
        return False
    return True


def calc_juros(valor_emprestimo, n_parcelas):
    valor_emprestimo_original = valor_emprestimo
    if n_parcelas <= 6:
        valor_emprestimo += valor_emprestimo * 0.05
    elif 7 <= n_parcelas <= 12:
        valor_emprestimo += valor_emprestimo * 0.08
    elif 13 <= n_parcelas <= 24:
        valor_emprestimo += valor_emprestimo * 0.1
    juros_totais = valor_emprestimo - valor_emprestimo_original
    return valor_emprestimo, juros_totais


def calc_parcela(valor_emprestimo, n_parcelas):
    valor_parcelas = valor_emprestimo / n_parcelas
    return valor_parcelas

def validar_parcelas():
    while True:
        n_parcelas = int(input("Insira o número de parcelas desejadas (3 à 24): "))
        if 3 <= n_parcelas <= 24:
            return n_parcelas
        else:
            print("Número de parcelas inválido. Deve ser entre 3 e 24.")

def main():
    # Requisito 1
    nome = input("Insira seu nome: ").capitalize()
    idade = int(input("Insira sua idade: "))
    renda = float(input("Insira sua renda mensal: "))
    valor_emprestimo = float(input("Insira o valor de empréstimo desejado: "))
    n_parcelas = validar_parcelas()

    # Requisito 2
    # Verifica se o empréstimo pode ser aprovado
    if aprovacao(idade, renda, valor_emprestimo, n_parcelas):
        # Calculando juros e valor das parcelas:
        valor_emprestimo, juros_totais = calc_juros(valor_emprestimo, n_parcelas)
        valor_parcelas = calc_parcela(valor_emprestimo, n_parcelas)
        valor_total_cjuros = valor_parcelas * n_parcelas

    # Requisito 3
        # Exibindo as informações para o cliente
        print(f"\nEmpréstimo Aprovado!\n"
              f"O valor de suas parcelas mensais será de R${valor_parcelas:.2f}.\n"
              f"O valor total será de R${valor_total_cjuros:.2f}.\n"
              f"Os juros totais pagos serão de R${juros_totais:.2f}.")
    else:
        print("\nEmpréstimo Negado: o cliente não atende algum dos requisitos.")


# Chama a função principal
if __name__ == "__main__":
    main()
