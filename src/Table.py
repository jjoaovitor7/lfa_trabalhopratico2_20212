class Table (object):
    def __init__(self):
        """A instanciação cria um objeto vazio, aqui dá para criar com algum valor predeterminado."""

        self.m = []

    def generateTable(self, grammar, expr):
        """
        Gerar tabela.

        Parâmetros
        ----------
        grammar : dict
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
            grammar : dict
            expr    : str
            """

            # MONTANDO LINHA BASE
            for i in range(0, len(expr)):
                for key in grammar:
                    for values in grammar[key]:
                        for value in list(values):
                            # RETIRANDO *
                            self.m[len(self.m)-1][i] = self.m[len(self.m)-1][i].replace("*", "")

                            if (value.islower() and expr[i] == value):
                                self.m[len(self.m)-1][i] += key
                # QUANDO TIVER MAIS DE UM NÃO-TERMINAL
                self.m[len(self.m)-1][i] = ",".join(self.m[len(self.m)-1][i])            

            self.m.reverse()
            # MONTANDO AS OUTRAS LINHAS
            # n = len(expr)
            # for i in range(2, n):
            #     for j in range(1, n-i+1):
            #         for k in range(1, i-1):
            #             for key in grammar:
            #                 for values in grammar[key]:
            #                     if (len(values) == 2):
            #                         # print(f"{values[0]} {self.m[j][k]} | {values[1]} {self.m[j+k][i-k]}")
            #                         if (values[0] in self.m[j][k] and values[1] in self.m[j+k][i-k]):
            #                             self.m[j][i] = key





        fillTable(self, grammar, expr)  

    def print(self):
        """Printar tabela."""

        for i in self.m:
            print(i)
