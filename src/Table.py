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

            # MONTANDO "LINHA BASE"
            index = 0
            for symbol in expr:
                for i in grammar:
                    for j in grammar[i]:
                        for k in list(j):
                            if (k.islower() and k == symbol):
                                try:
                                    self.m[len(self.m)-1][index].append(i)
                                except:
                                    self.m[len(self.m)-1][index] = [i]
                index += 1

            for i in reversed(range(0, len(self.m))):
                for j in range(0, len(self.m[i])):
                    self.m[i][j] = ",".join(self.m[i][j])

            # MONTANDO SEGUNDA LINHA
            for i in reversed(range(len(self.m))):

                # "POUPAR PROCESSAMENTO"
                if (i > (len(self.m) - 1)):
                    break

                for j in range(0, len(self.m[i])-1):
                    _aux1 = self.m[i][j].split(",")
                    _aux2 = self.m[i][j+1].split(",")

                    for _i in range(0, len(_aux1)):
                        for _j in range(0, len(_aux2)):
                            for l in grammar:
                                for n in grammar[l]:
                                    if(f"{_aux1[_i]}{_aux2[_j]}".replace("*", "") == "".join(n)):
                                        self.m[i-1][j] = l
            
            # TODO: MONTANDO AS OUTRAS LINHAS
        fillTable(self, grammar, expr)

    def print(self):
        """Printar tabela."""

        for i in self.m:
            print(i)
