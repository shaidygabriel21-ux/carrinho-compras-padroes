from item import Item
from carrinho_de_compras import CarrinhoDeCompras
from frete_factory import FreteFactory

carrinho = CarrinhoDeCompras()
carrinho.adicionar_item(Item("Teclado", 250.00, 0.85))
carrinho.adicionar_item(Item("Mouse", 180.00, 0.25))

print(f"Subtotal: R$ {carrinho.subtotal():.2f} | Peso: {carrinho.peso_total():.2f} kg")
for tipo in ("SEDEX", "PAC", "RETIRADA"):
    carrinho.definir_estrategia_frete(FreteFactory.criar(tipo))
    total, frete = carrinho.total()
    print(f"{tipo:<9} -> Frete: R$ {frete:.2f} | Total: R$ {total:.2f}")
