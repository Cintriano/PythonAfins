def calcular_custo_viagem():
    print("========== Calculadora de Custo de Combustível ==========")

#47L
    try:
        distancia = float(input("Informe a distância percorrida (em km): "))

        print("""
        0 - Preço do combustivel 6,59
        1 - Personalizado
        """)

        op1 = input("Informe a custo do Combustivel: ")

        if op1 == "0":
            preco_combustivel = 6.59
        elif op1 == "1":
            preco_combustivel = float(input("Informe o valor do combustível (R$/litro): "))
        else:
            return "Por favor, insira apenas números válidos."


        print("""
        0 - Autonomia na Cidade (Fiat Mobi)
        1 - Autonomia na Estrada (Fiat Mobi)
        2 - Personalizado
        """)

        op2 = input("Informe a autonomia: ")

        if op2 == "0":
            autonomia = 13.7
        elif op2 == "1":
            autonomia = 15
        elif op2 == "2":
            autonomia = float(input("Informe a autonomia do veículo (km/litro): "))
        else:
            return "Por favor, insira apenas números válidos."

        if autonomia <= 0:
            print("A autonomia precisa ser maior que zero.")
            return

        custo = (distancia / autonomia) * preco_combustivel

        capacidade_combustivel = 47

        litros = round(distancia / autonomia)

        porcentagem = round((distancia / (autonomia * capacidade_combustivel)) * 100)

        print(f"\n========== Resultado ==========\n"
              f"Distancia: {distancia}Km\n"
              f"Custo: R$ {custo:.2f}\n"
              f"Litros gastos: {litros}L\n"
              f"Porcentagem de gasto do tanque: {porcentagem}%")

    except ValueError:
        print("Por favor, insira apenas números válidos.")

if __name__ == "__main__":
    calcular_custo_viagem()
