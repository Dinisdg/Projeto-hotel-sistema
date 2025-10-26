
class Quarto:
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria 
        self.ocupado = False 

    def ocupar(self):
        self.ocupado = True
        print(f"Quarto {self.numero} agora ocupado.")

    def desocupar(self):
        self.ocupado = False
        print(f"Quarto {self.numero} agora livre.")

    def mostrar_informacoes(self):
        status = "OCUPADO" if self.ocupado else "LIVRE"
        print(f"Quarto {self.numero} | Tipo: {self.tipo} | Diária: {self.preco_diaria:.2f}€ | Status: {status}")

class QuartoSimples(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Simples", 50.0)

class QuartoLuxo(Quarto):
    def __init__(self, numero):
        super().__init__(numero, "Luxo", 120.0)

    def mostrar_informacoes(self):
        print(f"--- QUARTO DE LUXO {self.numero} ---")
        super().mostrar_informacoes()
        print("Equipado com jacuzi e vista para o mar!")

