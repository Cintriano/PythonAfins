class Veiculo:
    def __init__(self, id: str, modelo: str, marca: str, ano: float, capa_tanque: int, auto_cidade: float, auto_estrada: float):
        self.id = id
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.capa_tanque = capa_tanque
        self.auto_cidade = auto_cidade
        self.auto_estrada = auto_estrada

    def auto_total(self):
        auto_total_cidade =round(self.auto_cidade * self.capa_tanque, 2)
        auto_total_estrada = round(self.auto_estrada * self.capa_tanque, 2)
        return [auto_total_cidade, auto_total_estrada]

    def exibir(self):
        print(f"ID: {self.id}\n"
              f"Modelo: {self.modelo}\n"
              f"Marca: {self.marca}\n"
              f"Ano: {self.ano}\n"
              f"Capcidade do Tanque: {self.capa_tanque}\n"
              f"Autonomia da Cidade: {self.auto_cidade}\n"
              f"Autonomia de Estrada: {self.auto_estrada}")