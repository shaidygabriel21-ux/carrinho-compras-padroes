class CarrinhoDeCompras:
    """Contexto do Strategy: delega o cálculo do frete à estratégia atual."""

    def __init__(self):
        self._itens = []
        self._estrategia = None

    def adicionar_item(self, item):
        self._itens.append(item)

    def definir_estrategia_frete(self, estrategia):
        self._estrategia = estrategia

    def subtotal(self):
        return sum(i.preco for i in self._itens)

    def peso_total(self):
        return sum(i.peso for i in self._itens)

    def total(self):
        frete = self._estrategia.calcular(self.peso_total(), self.subtotal())
        return self.subtotal() + frete, frete
