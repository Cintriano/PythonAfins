class Conjunto:
    def __init__(self):
        self.conjunto = []

    def inserir(self, elemento):
        self.conjunto.append(elemento)

    def comtem(self, elemento):
        if elemento in self.conjunto:
            return True
        return False

    def __str__(self):
        return f"A = {{self.conjunto}}"
