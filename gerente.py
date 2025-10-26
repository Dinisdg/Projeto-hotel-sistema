from funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, id_func, idade, salario, bonus=0.10):
        super().__init__(nome, id_func, idade, salario)
        self.bonus = bonus
    
    def mostrar_informacoes(self):
        total = self.salario * (1 + self.bonus)
        print(f"Gerente: {self._nome} | Idade: {self._idade} | Salário+Bónus: {total:.2f}€")

    def gerar_relatorio(self, funcionarios):
        print(" Relatório de Funcionários ")
        for f in funcionarios:          
            f.mostrar_informacoes()
        print("=============================")