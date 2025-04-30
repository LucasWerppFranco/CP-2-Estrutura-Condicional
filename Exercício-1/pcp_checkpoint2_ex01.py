
nC = input("Digite o número da carga: ")
oC = input("Digite o estado de origem da carga (ex: Estado 1, Estado 2, etc.): ")
pC = float(input("Digite o peso da carga em toneladas: "))


peso_em_quilos = pC * 1000


taxas_imposto = {
    "1": 0.35,
    "2": 0.25,
    "3": 0.15,
    "4": 0.05,
    "5": 1.00,
}

valores_por_quilo = {
    (10000, 20000): 100,
    (21000, 30000): 250,
    (31000, 40000): 340,
}

if peso_em_quilos <= 0:
    print("Peso da carga deve ser positivo.")
else:
    taxa_estado = taxas_imposto.get(oC)
    valor_carga = next((valor for (min_peso, max_peso), valor in valores_por_quilo.items() if min_peso <= peso_em_quilos <= max_peso), None)

    if taxa_estado is None:
        print("Estado inválido.")
    elif valor_carga is None:
        print("Faixa de carga inválida.")
    else:
        imposto = peso_em_quilos * taxa_estado * valor_carga
        print(f"Imposto a ser pago para a carga {nC}: R$ {imposto:.2f}")
