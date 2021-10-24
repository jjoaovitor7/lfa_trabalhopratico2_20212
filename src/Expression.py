class Expression (object):
    """Classe que representa uma expressão (sentença fica estranho)."""

    def __init__(self):
        """A instanciação cria um objeto vazio, aqui dá para criar com algum valor predeterminado."""

        self.expr = None

    def load(self):
        """Carregar a expressão."""

        self.expr = input("Expressão\n:")

    def get(self):
        """Retornar a expressão."""

        return self.expr
