import ply.yacc as yacc
from Lexer import Lexer
import sys
from Command import Command

class Parser:
    tokens = Lexer.tokens  # Vai buscar os tokens ao lexer

    def __init__(self):
        self.parser= None
        self.lexer = None
        self.color = (0, 0, 0)
        self.vars = {}



    def Parser(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Starter(input, **kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        program = self.parser.parse(lexer=self.lexer.lexer)
        print(program)
        self.execute(program)


    def execute(self, program):
        for command in program:
            command.run(self)

    def p_error(self, t):
        print(t, file=sys.stderr)
        exit(1)


    def p_program0(self, t):
        """ program  : command """
        t[0] = [t[1]]

    def p_program1(self, t):
        """ program  : program command """  # uso de recursividade
        lst = t[1]
        lst.append(t[2])
        t[0] = lst
        #t[0] = t[1].appned(t[2])

    def p_command0(self, t):
        """ command : fd INT
                    | forward INT """
        args = {"forward":t[2]}
        t[0]= Command("forward", args)

    def p_command1(self, t):
        """ command : bk INT
                    | back INT """
        args = {"back": t[2]}
        t[0]= Command("back", args)

    def p_command2(self, t):
        """ command : lt INT
                    | left INT """
        args = {"left": t[2]}
        t[0] = Command("left", args)

    def p_command3(self, t):
        """ command : rt INT
                    | right INT """
        args = {"right": t[2]}
        t[0] = Command("right", args)
#exemplo!
    #def p_command4(self, t):
        #""" command : setpos '[' cordenadas ']' """
        #t[0] = Command("posicao", t[3])

    def p_command4(self, t):
        """ command : setpos '[' INT INT ']' """
        t[0] = Command("pos", {
            "x": t[3],
            "y": t[4]})

    def p_command5(self, t):
        """ command : setxy INT INT """
        t[0] = Command("posxy", {
            "x": t[2],
            "y": t[3]})

    def p_command6(self, t):
        """ command : setx INT """
        t[0] = Command("setx", {
            "x": t[2]})


    def p_command7(self, t):
        """ command : sety INT """
        t[0] = Command("sety", {
            "y": t[2]})

    def p_command8(self, t):
        """ command : penup
                    | pu  """
        t[0] = Command("canetaup", t[1])

    def p_command9(self, t):
        """ command : pendown
                    | pd  """
        t[0] = Command("canetadown", {"x:": t[1]})

    def p_command10(self, t):
        """ command : home  """
        t[0] = Command("inicio", {"casa:": t[1]})

    def p_command11(self, t):
        """ command : setpencolor '[' INT INT INT ']' """
        t[0] = Command("corcaneta", {
            "a": t[3],
            "b": t[4],
            "c": t[5]})


    def p_command12(self, t):
        """ command : make VARNOME INT """
        t[0]= Command("make", {
            "var": t[2],
            "inteiro": t[3]})

    def p_command13(self, t):
        """ command : if ':' VARNOME SINAIS INT '[' program ']'
                    | ifelse ':' VARNOME SINAIS INT '[' program ']'"""

        t[0]= Command("if", {
            "var": t[3],
            "sinais": t[4],
            "inteiro": t[5],
            "program": t[7]})

    def p_command14(self, t):
        """ command : while '[' ':' VARNOME SINAIS INT ']' '[' program ']' """
        t[0] = Command("while", {
        "var": t[4],
        "sinais": t[5],
        "inteiro": t[6],
        "program": t[9]})

    def p_command15(self, t):
        """ command : repeat command """
        t[0] = Command("repetir", t[2])


    #def p_cordenadas(self, t):
        #""" cordenadas : INT INT"""
        #t[0] = (t[1], t[2])

    #def p_color(self, t):
        #""" color : INT INT INT """
        #t[0] = (t[1], t[2], t[3])
