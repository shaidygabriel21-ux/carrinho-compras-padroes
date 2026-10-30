from estrategia_frete import FreteSedex, FretePAC, FreteRetiradaLoja


class FreteFactory:
    """Simple Factory: transforma um texto no objeto de frete certo."""

    @staticmethod
    def criar(tipo):
        tipo = tipo.upper()
        if tipo == "SEDEX":
            return FreteSedex()
        if tipo == "PAC":
            return FretePAC()
        if tipo == "RETIRADA":
            return FreteRetiradaLoja()
        raise ValueError(f"Tipo de frete inválido: {tipo}")
