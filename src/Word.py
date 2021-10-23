class Word:
    """Classe que representa uma palavra."""

    def __init__(self):
        """A instanciação cria um objeto vazio, aqui dá para criar com algum valor predeterminado."""

        self._word = None

    def load(self):
        """Carregar a palavra."""

        self._word = input("Palavra\n:")

    def get(self):
        """Retornar a palavra."""

        return self._word
