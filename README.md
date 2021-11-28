# lfa_trabalhopratico2_20212
Trabalho Prático 2 da disciplina de Linguagens Formais e Automâtos (LFA).

Integrantes:
* João Vítor Silva Ferreira

Algoritmo:
* CYK

Como baixar e executar?

Clonar o repositório.
```
git clone https://github.com/jjoaovitor7-unit/lfa_trabalhopratico2_20212.git
cd lfa_trabalhopratico2_20212/
```

<br />
(Terminal)

Criar um arquivo `.cyk` em `/files/` com a gramática na Forma Normal de Chomsky (FNC).

Modificar caminho do arquivo em `main.py`:

`file = File(f"{path__current}{os.sep}files{os.sep}<file>.cyk")`

`python3 main.py`

E digitar a palavra para ser verificada.

<br />
(Web)

Baixar a dependência *(flask)*.

`pip3 install flask`

Rodar o servidor.

`python3 server.py`

Enviar o arquivo e logo após digitar a palavra para ser verificada.