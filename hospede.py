from pessoa import Pessoa

class Hospede(Pessoa):
    def __init__(self, nome, idade, dias_estadia, quarto=None):
        super().__init__(nome, idade)
        self._nome = nome
        self._idade = idade
        self.dias_estadia = dias_estadia
        self._quarto = quarto
    
        @property
        def quarto(self):
            return self._quarto
        
        @quarto.setter
        def quarto(self, novo_quarto):
            if self.quarto is None:
                self.quarto = novo_quarto
            else:
                print("O Hospede ja tem um Quarto")

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválida, ajustada para 0.")
            self._idade = 0
        else:
            self._idade = nova_idade 


    def mostrar_informacoes(self):
        print("--- Informações do Hóspede ---")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Dias de estadia: {self.dias_estadia}")
        if self.quarto:
            print(f"Quarto: {self.quarto.numero} ({self.quarto.tipo})")
        else:
            print("Quarto: Ainda não atribuído")

    def atribuir_quarto(self, quarto):
        if quarto and not quarto.ocupado:
            self.quarto = quarto
            quarto.ocupar()
            print(f"Quarto {quarto.numero} atribuído a {self.nome}.")
        else:
            print(f"ERRO: Quarto {quarto.numero} ocupado ou inválido para {self.nome}!")

    def calcular_conta(self):
        if self.quarto:
            valor_total = self.dias_estadia * self.quarto.preco_diaria
            return valor_total
        return 0

    def checkout(self):
        if self.quarto:
            print(f"CHECKOUT: O hóspede {self.nome} do quarto {self.quarto.numero} está a sair.")
            self.quarto.desocupar()
            self.quarto = None
        else:
            print(f"AVISO: O hóspede {self.nome} não tem quarto atribuído.")