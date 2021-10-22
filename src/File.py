class File (object):
    """
    Classe que representa um arquivo.

    Atributos
    ---------
    _file : File object

    Métodos
    -------

    """

    def __init__(self, file):
        """
        A instanciação cria um objeto vazio, aqui dá para criar com algum valor predeterminado.

        Parâmetros
        ----------
        file : File Object.

        """

        self._file = file
        self._file__open = None

    def open(self):
        """Abertura do arquivo."""

        self._file__open = open(self._file, mode="r",
                                encoding="utf8", newline=None)

    def getFile(self):
        """Retornar o arquivo."""

        return self._file

    def getFile__text(self):
        """Retornar o arquivo aberto."""

        return self._file__open

    def print(self):
        """Visualizar o arquivo."""

        for line in self._file__open:
            if (line != None):
                print(line, end='')
