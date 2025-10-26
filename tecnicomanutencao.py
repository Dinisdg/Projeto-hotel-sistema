from funcionario import Funcionario

class TecnicoManutencao(Funcionario):
    def __init__(self, nome, id_func, idade, salario, especialidade):
        super().__init__(nome, id_func, idade, salario)
        self._especialidade = especialidade

    @property
    def especialidade(self):
        return self._especialidade

    @especialidade.setter
    def especialidade(self, nova_especialidade):
        self._especialidade = nova_especialidade
    
    def mostrar_informacoes(self):
        print(f"Técnico Manutenção: {self.nome}") 
        print(f"Especialidade: {self._especialidade}")
        print(f"ID: {self.id_func}")

    def registar_reparo(self, descricao):
        print(f"[REPARO] Técnico {self.nome}")
        print(f"{self.especialidade}") 
        print(f"registrou: {descricao}")