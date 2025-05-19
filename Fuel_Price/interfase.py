from Main import *
from tabulate import tabulate

mobi = Veiculo("001", "Mobi", "Fiat", 2020, 47, 10.75, 12.1)
hilux = Veiculo("002", "Hilux", "Toyota", 2015, 80, 9, 11)
biz = Veiculo("003", "Biz", "Honda", 2010, 5.1, 45, 50)

list_veiculos = [mobi]

def interfase():
    print("========== Calculadora de Custo de Combustível ==========")

    print("""
    0 - Custo por distancia
    1 - Comparação de Preços
    """)

    while True:
        op1 = input("Qual o serviço desejado: ")
        status = input(f"Confirme a opção: ({op1}) s/n: ")
        if status == "s":
            break

    if op1 == "0":
        while True:
            distancia = float(input("\nInforme a distância percorrida (em km): "))
            status = input(f"Confirme a distancia: ({distancia}Km) s/n: ")
            if status == "s":
                break

        print("""
        0 - Preço do combustivel 6,59
        1 - Personalizado
        """)

        while True:
            op2 = input("Informe a custo do Combustivel: ")
            status = input(f"Confirme a opção: ({op2}) s/n: ")
            if status == "s":
                break

        if op2 == "0":
                preco_combustivel = 6.59
        elif op2 == "1":
            preco_combustivel = float(input("\nInforme o valor do combustível (R$/litro): "))
        else:
            return "Por favor, insira apenas números válidos."
        result_cal_custo_viagem = cal_custo_viagem(distancia, preco_combustivel, list_veiculos)

        print("\n========== RESULTADO ==========")
        for veiculo in result_cal_custo_viagem:
            for obj_veiculo in list_veiculos:
                if veiculo[0] == obj_veiculo.id:
                    headers = ["Modelo", "Marca", "Ano", "Cap.Tanque", "Auto.Cidade", "Auto.Estrada", "Auto.Total"]
                    table = [
                    [f"{obj_veiculo.modelo}", f"{obj_veiculo.marca}", f"{obj_veiculo.ano}",
                    f"{obj_veiculo.capa_tanque:.2f}L", f"{obj_veiculo.auto_cidade:.2f}Km | max: {obj_veiculo.auto_total()[0]}",
                    f"{obj_veiculo.auto_estrada:.2f}Km | max: {obj_veiculo.auto_total()[1]}"]]
                    print(tabulate(table, headers=headers, tablefmt="grid"))

            print(f"\nDistancia: {distancia}Km")

            headers = ["", "Custo na Cidade", "Custo na Estrada"]
            table = [
                ["Custo (R$)", f"{veiculo[2][0]:.2f}", f"{veiculo[3][0]:.2f}"],
                ["Litros (L)", f"{veiculo[2][1]:.2f}", f"{veiculo[3][1]:.2f}"],
                ["Consumo (%)", f"{veiculo[2][2]:.2f}%", f"{veiculo[3][2]:.2f}%"],
            ]
            print(tabulate(table, headers=headers, tablefmt="grid"),"\n\n===================================\n")

    elif op1 == "1":
        while True:
            valor1 = float(input("Primeiro Valor: "))
            valor2 = float(input("Segundo Valor: "))
            status = input(f"Confirme os Dados: valor1({valor1}) Valor2({valor2}) s/n: ")
            if status == "s":
                break
        p_tanque_cheio = preco_tanque_cheio([valor1, valor2], list_veiculos)
        perce_diferencial = percentual_diferencial([valor1, valor2])

        print("\n========== RESULTADO ==========")
        for veiculo in p_tanque_cheio:
            for obj_veiculo in list_veiculos:
                if veiculo[0] == obj_veiculo.id:
                    headers = ["Modelo", "Marca", "Ano", "Cap.Tanque", "Auto.Cidade", "Auto.Estrada", "Auto.Total"]
                    table = [
                        [f"{obj_veiculo.modelo}", f"{obj_veiculo.marca}", f"{obj_veiculo.ano}",
                         f"{obj_veiculo.capa_tanque:.2f}L",
                         f"{obj_veiculo.auto_cidade:.2f}Km | max: {obj_veiculo.auto_total()[0]}",
                         f"{obj_veiculo.auto_estrada:.2f}Km | max: {obj_veiculo.auto_total()[1]}"]]
                    print(tabulate(table, headers=headers, tablefmt="grid"))


            headers = ["", "Maior Valor", "Menor Valor"]
            table = [
                ["Custo tan_cheio", f"{veiculo[1]:.2f} R$", f"{veiculo[2]:.2f} R$"]
            ]
            print(tabulate(table, headers=headers, tablefmt="grid"), "\n\n===================================\n")

        headers = ["Maior Valor", "Menor Valor", "Variação", "Variação", "Porcentagem(menor->maior)"]
        table = [
            [f"{perce_diferencial[0]:.2f} R$", f"{perce_diferencial[1]:.2f} R$",
             f"{perce_diferencial[2]:.2f} R$", f"{perce_diferencial[3]:.2f} %", f"{perce_diferencial[4]:.2f} %"]
        ]
        print(tabulate(table, headers=headers, tablefmt="grid"), "\n\n===================================\n")


    return "Sucesso"

if __name__ == "__main__":
    interfase()