class Table (object):
    def __init__(self):
        """A instanciação cria um objeto vazio, aqui dá para criar com algum valor predeterminado."""

        self.m = []

    def generateTable(self, grammar, expr):
        """
        Gerar tabela.

        Parâmetros
        ----------
        grammar : Dict.
        expr    : str
        """

        for i in range(len(expr)):
            for j in range(i+1):
                try:
                    self.m[(i-j)+j].append("*")
                except IndexError:
                    self.m.append(["*"])

        def fillTable(self, grammar, expr):
            """
            Preenchendo tabela.

            Parâmetros
            ----------
            grammar : Dict.
            expr    : str
            """

            # MONTANDO "LINHA BASE"
            index = 0
            for symbol in expr:
                for i in grammar:
                    for j in grammar[i]:
                        for k in list(j):
                            if (k.islower() and k == symbol):
                                self.m[len(self.m)-1][index] = i
                index += 1

            # MONTANDO AS OUTRAS LINHAS A PARTIR DA "LINHA BASE"
            for i in reversed(range(0, len(self.m))):
                for j in range(0, len(self.m[i])):
                    for k in grammar:
                        for l in grammar[k]:
                            try:
                                if ("".join(l) == f"{self.m[i][j]}{self.m[i][j+1]}".replace("*", "")):
                                    self.m[i-1][j] = k
                            except IndexError as e:
                                # if ("".join(l) == f"{self.m[i][j-1]}{self.m[i][j]}".replace("*", "")):
                                #     self.m[i-1][j] = k
                                # print(e)
                                pass

        fillTable(self, grammar, expr)

    def print(self):
        """Printar tabela."""

        for i in self.m:
            print(i)
