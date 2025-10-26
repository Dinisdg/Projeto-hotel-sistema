from funcionario import Funcionario

class Recepcionista(Funcionario):
    def __init__(self, nome, id_func, idade, salario, turno):
        Funcionario.__init__(self, nome, id_func, idade, salario)
        self.turno = turno

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, novo_turno):
        if novo_turno.lower() in ["manhã", "tarde", "noite"]:
            self._turno = novo_turno.capitalize()
        else:
            print("Turno inválido. Definido como 'Manhã'.")
            self._turno = "Manhã"

    def mostrar_informacoes(self):
        print(f"Recepcionista: {self._nome} | ID: {self.id_func} | Turno: {self._turno} | Salário: {self.salario:.2f}€")

    def registrar_hospede(self, hospede, lista_hospedes):
        lista_hospedes.append(hospede)
        print(f"Hóspede {hospede.nome} registado por {self._nome}.")

    def listar_hospedes(self, lista_hospedes):
        print("\n--- Lista de Hóspedes ---")
        if not lista_hospedes:
            print("Nenhum hóspede registado.")
        else:
            for h in lista_hospedes:
                h.mostrar_informacoes()
