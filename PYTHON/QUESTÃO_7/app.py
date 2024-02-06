from abc import ABC, abstractmethod

class CalculadoraSalario(ABC):
    def __init__(self, horas_trabalhadas):
        self.horas_trabalhadas = horas_trabalhadas

    @abstractmethod
    def calcular_salario(self):
        pass

class GrupoComBonus(CalculadoraSalario):
    def calcular_salario(self):
        valor_hora = 200.00
        salario = self.horas_trabalhadas * valor_hora
        bonus = salario * 0.30
        salario_total = salario + bonus
        return salario_total

class GrupoSemBonus(CalculadoraSalario):
    def calcular_salario(self):
        valor_hora = 250.00
        salario = self.horas_trabalhadas * valor_hora
        return salario

horas_trabalhadas_grupo1 = 20
horas_trabalhadas_grupo2 = 30

calculadora_grupo1 = GrupoComBonus(horas_trabalhadas_grupo1)
calculadora_grupo2 = GrupoSemBonus(horas_trabalhadas_grupo2)

salario_grupo1 = calculadora_grupo1.calcular_salario()
salario_grupo2 = calculadora_grupo2.calcular_salario()

print("Salário do Grupo 1:", salario_grupo1)
print("Salário do Grupo 2:", salario_grupo2)
