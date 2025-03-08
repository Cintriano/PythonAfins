def calcular_custo_viagem():
    print("========== Calculadora de Custo de Combustível ==========")

    try:
        distancia = float(input("Informe a distância percorrida (em km): "))

        print("""
        0 - Preço do combustivel 6,63
        1 - Personalizado
        """)

        op1 = input("Informe a custo do Combustivel: ")

        if op1 == "0":
            preco_combustivel = 6.63
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
            autonomia = 13.7
        elif op2 == "2":
            autonomia = float(input("Informe a autonomia do veículo (km/litro): "))
        else:
            return "Por favor, insira apenas números válidos."

        if autonomia <= 0:
            print("A autonomia precisa ser maior que zero.")
            return

        custo = (distancia / autonomia) * preco_combustivel

        print(f"\n========== Resultado ==========\nDistancia: {distancia}Km\nCusto: R$ {custo:.2f}")

    except ValueError:
        print("Por favor, insira apenas números válidos.")

if __name__ == "__main__":
    calcular_custo_viagem()
