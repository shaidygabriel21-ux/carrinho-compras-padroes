# Carrinho de Compras com cálculo de frete

Trabalho de Análise e Projeto de Sistemas I (Sistemas de Informação).

Padrões de projeto usados:
- **Strategy**: cada forma de frete (Sedex, PAC, Retirada) é uma classe.
- **Simple Factory**: `FreteFactory` cria o frete certo a partir de um texto.

## Como rodar

```
python main.py
```

## Arquivos

| Arquivo | Conteúdo |
| --- | --- |
| `item.py` | Classe Item (nome, preço, peso) |
| `estrategia_frete.py` | Interface EstrategiaFrete e as 3 estratégias |
| `frete_factory.py` | FreteFactory |
| `carrinho_de_compras.py` | CarrinhoDeCompras (contexto) |
| `main.py` | Exemplo de execução |
