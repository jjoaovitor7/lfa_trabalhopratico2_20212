#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from src.File import File
from src.Grammar import Grammar
from src.Expression import Expression
from src.Table import Table


def main():
    # LEITURA DO ARQUIVO
    path__current = os.getcwd()
    file = File(f"{path__current}{os.sep}files{os.sep}1.cyk")
    file.open()

    # REPRESENTAÇÃO DA GRAMÁTICA
    grammar = Grammar(file.getFile__text())
    grammar.load()
    grammar.print()

    # EXPRESSÃO
    expr = Expression()
    expr.load()

    # TABELA DE PARSING
    table = Table()
    table.generateTable(grammar.get(), expr.get())
    table.print()


if __name__ == "__main__":
    main()
