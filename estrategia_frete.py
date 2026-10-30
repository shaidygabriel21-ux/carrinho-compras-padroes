from abc import ABC, abstractmethod


class EstrategiaFrete(ABC):
    """Interface do padrão Strategy: todo frete precisa ter 'calcular'."""

    @abstractmethod
    def calcular(self, peso_total, subtotal):
        pass


class FreteSedex(EstrategiaFrete):
    def calcular(self, peso_total, subtotal):
        return 15.00 + 2.50 * peso_total


class FretePAC(EstrategiaFrete):
    def calcular(self, peso_total, subtotal):
        return 8.00 + 1.20 * peso_total


class FreteRetiradaLoja(EstrategiaFrete):
    def calcular(self, peso_total, subtotal):
        return 0.0
