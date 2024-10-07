class Endereco:
    def __init__(self, rua, numero, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado}"
