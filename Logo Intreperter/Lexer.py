# lexer.py
import sys

import ply.lex as lex


class Lexer:
    tokens = (
    "INT", "fd", "forward", "bk", "back", "lt", "left", "rt", "right", "setpos", "setxy", "setx", "sety", "home",
    "pendown", "penup", "setpencolor", "pu", "pd", "if", "ifelse", "repeat", "VARNOME", "make", "SINAIS", "while")
    literals = "[]:"
    t_ignore = " \n\t\""

    # setxy | setx | setysetpencolor
    def t_COMMAND(self, t):
        r"fd|forward|bk|back|lt|left|rt|right|set(pos)?(xy)?(x)?(y)?(pencolor)?|home|pen(down)?(up)?|pu|pd|if(else)?|repeat|make|while"
        t.type = t.value
        return t

    def t_SINAIS(self, t):
        r"\>|\<|=|<=|>=|==|!="
        return t

    def t_VARNOME(self, t):
        r"\"*[a-z][0-9a-z]*"
        return t

    def t_INT(self, t):
        r"[0-9]*\.*[0-9]+"
        t.value = float(t.value)
        return t

    def t_error(self, t):
        print(f"Erro no parse {t.value}", file=sys.stderr)
        exit(1)

    def __init__(self):
        self.lexer = None

    def Starter(self, input, **Kwargs):
        self.lexer = lex.lex(module=self, **Kwargs)
        self.lexer.input(input)
