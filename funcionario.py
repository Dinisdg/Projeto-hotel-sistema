from pessoa import Pessoa
from abc import ABC

class Funcionario(Pessoa):
    def __init__(self, nome, id_func, idade, salario):
        super().__init__(nome, idade)
        self.id_func = id_func
        self.salario = salario

        if self.salario < 0:
            print("ERRO: Salário não pode ser negativo. A ajustar para 0.")
            self.salario = 0

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
        print(f"Funcionário: {self.nome}") 
        print(f"ID: {self.id_func}") 
        print(f"Idade: {self.idade}")
        print(f"Salário: {self.salario:.2f}€")
