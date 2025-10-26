# main.py

from hospede import Hospede
from gerente import Gerente
from recepcionista import Recepcionista
from tecnicomanutencao import TecnicoManutencao
from tecnicorecepcao import TecnicoRecepcao
from quarto import QuartoSimples, QuartoLuxo

lista_hospedes = []
lista_quartos = []
lista_funcionarios = []

print("=== Quartos Disponíveis ===")
q1 = QuartoSimples(101)
q2 = QuartoLuxo(102)
q3 = QuartoSimples(103)
lista_quartos.extend([q1, q2, q3])

for q in lista_quartos:
    q.mostrar_informacoes()

print("\n=== Funcionários ===")
g1 = Gerente("Gloria", 1, 40, 2000.0)
r1 = Recepcionista("Paula", 2, 28, 1000.0, "Noite")
t1 = TecnicoManutencao("Lucas", 3, 35, 1200.0, "Elétrica")
tr1 = TecnicoRecepcao("Ismael", 3, 32, 1400.0, "Tarde", "Hidráulica")

lista_funcionarios.extend([g1, r1, t1, tr1])

for f in lista_funcionarios:
    f.mostrar_informacoes()

print("\n=== Registo de Hóspedes ===")
h1 = Hospede("Joshua", 25, 3)
h2 = Hospede("Laercio", 40, 2)
h3 = Hospede("Taynara", 22, 1)

r1.registrar_hospede(h1, lista_hospedes)
r1.registrar_hospede(h2, lista_hospedes)
tr1.registrar_hospede(h3, lista_hospedes)

print("\n=== Atribuir Quartos ===")
h1.atribuir_quarto(q1)
h2.atribuir_quarto(q2)
h3.atribuir_quarto(q3)

print("\n=== Lista de Hóspedes ===")
r1.listar_hospedes(lista_hospedes)

print("\n=== Registo de Reparos ===")
t1.registar_reparo("Troca de lâmpada no quarto 102")
tr1.registar_reparo("Porta quebrada no corredor principal")

print("\n=== Checkout e Contas ===")
for h in lista_hospedes[:]:
    total = h.calcular_conta()
    print(f"Conta total de {h.nome}: {total:.2f}€")
    h.checkout()
    lista_hospedes.remove(h)

print("\n=== Relatório do Gerente ===")
g1.gerar_relatorio(lista_funcionarios)

print("\n=== Fim ===")
