class Grammar (object):
    grammar = dict()

    def __init__(self, file):
        """
        A instanciação cria um objeto vazio, aqui dá para criar com algum valor predeterminado.
        
        Parâmetros
        ----------
        file : File Object.
        """

        self._file = file

    def load(self):
        """Carregar a gramática."""

        for line in self._file:
            # PEGANDO A CHAVE
            key = line.split("=>")
            key__format = key[0].replace(" ", "")

            keys__value = []
            for symbol in key[1]:
                if (symbol != " " and symbol != "\n"):
                    keys__value.append(symbol)

            arr_to_string__aux = ""
            for symbol in keys__value:
                arr_to_string__aux += symbol

            # PEGANDO OS VALORES DA CHAVE
            values = arr_to_string__aux.split("|")

            for i in range(0, len(values)):
                _aux = []
                for j in list(values[i]):
                    _aux.append(j)
                values[i] = _aux
            try:
                self.grammar[key__format] = self.grammar[key__format] + values
            except:
                self.grammar[key__format] = values

    def get(self):
        """Retornar a gramática."""

        return self.grammar

    def print(self):
        """Visualizar a gramática."""

        print(self.grammar)
