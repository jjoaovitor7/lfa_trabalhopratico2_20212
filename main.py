#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from src.File import File


def main():
    # LEITURA DE ARQUIVO
    path__current = os.getcwd()
    file = File(f"{path__current}{os.sep}files{os.sep}1.cyk")
    file.open()
    file.print()


if __name__ == "__main__":
    main()
