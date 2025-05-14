from Class_Veiculo import Veiculo

def preco_tanque_cheio(precos: list[float], list_vei: list[Veiculo]):
    """Calcula o preço do tanque cheio com base nos valores de combustivel"""
    precos.sort()
    maior_valor = precos[1]
    menor_valor = precos[0]
    list_result = []

    for veiculo in list_vei:
        preco_maior_valor = round(maior_valor * veiculo.capa_tanque, 2)
        preco_menor_valor = round(menor_valor * veiculo.capa_tanque, 2)
        list_result.append([veiculo.id, preco_maior_valor, preco_menor_valor])
    return list_result


def percentual_diferencial(precos: list[float]):
    """Calcula a diferença(%,R$) entre os preços de combustivel"""
    precos.sort()
    maior_valor = precos[1]
    menor_valor = precos[0]

    percentual_geral = round((menor_valor * 100) / maior_valor)
    percentual_final = round(percentual_geral - 100) * -1
    diferenca_reais =  round(maior_valor - menor_valor, 2)
    return [maior_valor, menor_valor, diferenca_reais, percentual_final, percentual_geral]


def cal_custo_viagem(dist: float, preco_combustivel: float, list_vei: list[Veiculo]):
    """Beseado na distancia a função calcula custo de combustivel em reais, quantidade de litros gasto e percentual
    do tanque(cheio) consumido no trajeto"""
    list_result = []
    for veiculo in list_vei:
        custo_reais_cidade = round((dist / veiculo.auto_cidade) * preco_combustivel, 2)
        custo_reais_estrada = round((dist / veiculo.auto_estrada) * preco_combustivel, 2)
        custo_litros_cidade = round(dist / veiculo.auto_cidade)
        custo_litros_estrada = round(dist / veiculo.auto_estrada)
        percentual_tanque_cidade = round((dist / (veiculo.auto_cidade * veiculo.capa_tanque)) * 100)
        percentual_tanque_estrada = round((dist / (veiculo.auto_estrada * veiculo.capa_tanque)) * 100)
        list_result.append([veiculo.id, dist, [custo_reais_cidade, custo_litros_cidade, percentual_tanque_cidade], [custo_reais_estrada, custo_litros_estrada, percentual_tanque_estrada]])
    return list_result
