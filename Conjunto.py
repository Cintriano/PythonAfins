class Conjunto:
    def __init__(self):
        self.conjunto = []

    def inserir(self, elemento):
        self.conjunto.append(elemento)

    def contem(self, elemento):
        if elemento in self.conjunto:
            return True
        return False

    def __str__(self):
        conjunto_formatado = "{" + ",".join(map(str,self.conjunto)) + "}"
        return f" = {conjunto_formatado}"
