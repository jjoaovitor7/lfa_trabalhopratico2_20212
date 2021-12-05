class CYK (object):
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

        # FAZENDO A TABELA VAZIA
        n = len(expr)
        for i in range(n):
            for j in range(1, i+2):
                try:
                    self.m[i].append("")
                except IndexError:
                    self.m.append([""])

        # COLOCANDO A PALAVRA NA TABELA
        exprArr = []
        for i in expr:
            exprArr.append(i)
        self.m.append(exprArr)

        def fillTable(self, grammar, expr):
            """
            Preenchendo tabela.

            Parâmetros
            ----------
            grammar : dict
            expr    : str
            """

            self.m.reverse()
            for j in range(0, n):
                for key in grammar:
                    for values in grammar[key]:
                        if values == expr[j]:
                            self.m[1][j] = key

            iArr = [1, n]
            jArr = [1, 0]
            kArr = [1, 0]

            for i in range(1, n+1):
                jArr[1] = n-iArr[0]+1
                for j in range(0, jArr[1]):
                    kArr[1] = iArr[0]-1
                    for k in range(0, kArr[1]):
                        kArr[0] += 1
                        for key in grammar:
                            for values in grammar[key]:
                                valuesArr = list(values)
                                if len(valuesArr) == 2:
                                    # print(iArr, jArr, kArr)
                                    # print(key)
                                    # print("1:", valuesArr[0], self.m[kArr[0]][jArr[0]])
                                    # print("2:", valuesArr[1], self.m[iArr[0]-kArr[0]][jArr[0]+kArr[0]])
                                    if (valuesArr[0] == self.m[kArr[0]][jArr[0]] and valuesArr[1] == self.m[iArr[0]-kArr[0]][jArr[0]+kArr[0]]):
                                        self.m[iArr[0]][jArr[0]] = key
                    jArr[0] += 1
                    kArr[0] = 0

                jArr[0] = 0

                if (jArr[1] > 1):
                    jArr[1] -= 1

                iArr[0] += 1
                kArr[1] += 1

        fillTable(self, grammar, expr)

    def print(self):
        """Printar tabela."""
        for i in self.m:
            print(i)

    def get(self):
        """Retornar a tabela."""
        return self.m

    def verify(self):
        """Verificar se a palavra é aceita."""
        if (self.m[len(self.m)-1][0] == "S"):
            return "Palavra aceita."
        else:
            return "Palavra recusada."