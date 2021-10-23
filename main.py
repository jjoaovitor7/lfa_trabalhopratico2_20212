#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from src.File import File
from src.Grammar import Grammar


def main():
    # LEITURA DE ARQUIVO
    path__current = os.getcwd()
    file = File(f"{path__current}{os.sep}files{os.sep}2.cyk")
    file.open()

    # REPRESENTAÇÃO DA GRAMÁTICA
    grammar = Grammar(file.getFile__text())
    grammar.load()
    grammar.print()


if __name__ == "__main__":
    main()
