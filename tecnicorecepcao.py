from recepcionista import Recepcionista
from tecnicomanutencao import TecnicoManutencao

class TecnicoRecepcao(Recepcionista, TecnicoManutencao):
    def __init__(self, nome, id_func, idade, salario, turno, especialidade):
        Recepcionista.__init__(self, nome, id_func, idade, salario, turno)
        TecnicoManutencao.__init__(self, nome, id_func, idade, salario, especialidade)

    def mostrar_informacoes(self):
        print(f"Técnico-Recepção: {self._nome} | ID: {self.id_func} | Turno: {self._turno} | Especialidade: {self._especialidade} | Salário: {self.salario:.2f}€")

    def registrar_hospede(self, hospede, lista_hospedes):
        print(f"Técnico-Recepção {self._nome} registou o hóspede {hospede.nome}.")
        lista_hospedes.append(hospede)

    def registar_reparo(self, descricao):
        print(f"[Reparo] Técnico-Recepção {self._nome} ({self._especialidade}) registrou: {descricao}")

