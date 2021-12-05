#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from src.File import File
from src.Grammar import Grammar
from src.Expression import Expression
from src.CYK import CYK


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

    # CYK
    cyk = CYK()
    cyk.generateTable(grammar.get(), expr.get())
    cyk.print()
    print(cyk.verify())

if __name__ == "__main__":
    main()
