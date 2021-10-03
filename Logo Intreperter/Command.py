
f=open("ex1.svg","w")
f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 500.00 500.00">""")



class Movimentos:
    rotacao = 90
    x = 100
    y = 100
    a=0
    b=0
    c=0
    xfinal = 100
    yfinal = 150
    canetaup = False



def do_forward(command, parser):
    p1 = float(command.args["forward"])
    print(Movimentos.rotacao)
    if Movimentos.rotacao == 90:
        Movimentos.xfinal = Movimentos.x
        Movimentos.yfinal = Movimentos.y - p1
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>"""%(Movimentos.x, Movimentos.y,Movimentos.xfinal,Movimentos.yfinal,Movimentos.a,Movimentos.b,Movimentos.c))
        Movimentos.x = Movimentos.xfinal
        Movimentos.y = Movimentos.yfinal
    if Movimentos.rotacao == 180:
        Movimentos.xfinal = Movimentos.x - p1
        Movimentos.yfinal = Movimentos.y
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>""" % (Movimentos.x, Movimentos.y, Movimentos.xfinal, Movimentos.yfinal, Movimentos.a, Movimentos.b, Movimentos.c))
        Movimentos.x = Movimentos.xfinal
        Movimentos.y = Movimentos.yfinal
    if Movimentos.rotacao == 270:
        Movimentos.xfinal = Movimentos.x
        Movimentos.yfinal = Movimentos.y + p1
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>""" % (Movimentos.x, Movimentos.y, Movimentos.xfinal, Movimentos.yfinal, Movimentos.a, Movimentos.b, Movimentos.c))
        Movimentos.x = Movimentos.xfinal
        Movimentos.y = Movimentos.yfinal
    if Movimentos.rotacao == 0:
        Movimentos.xfinal = Movimentos.x + p1
        Movimentos.yfinal = Movimentos.y
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>""" % (Movimentos.x, Movimentos.y, Movimentos.xfinal, Movimentos.yfinal, Movimentos.a, Movimentos.b, Movimentos.c))
        Movimentos.x = Movimentos.xfinal
        Movimentos.y = Movimentos.yfinal
def do_backwards(command, parser):
    p1 = command.args["back"]
    if Movimentos.rotacao == 90:
        Movimentos.xfinal = Movimentos.x
        Movimentos.yfinal = Movimentos.y + p1
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>"""%(Movimentos.x, Movimentos.y,Movimentos.xfinal,Movimentos.yfinal,Movimentos.a,Movimentos.b,Movimentos.c))
    if Movimentos.rotacao == 180:
        Movimentos.xfinal = Movimentos.x + p1
        Movimentos.yfinal = Movimentos.y
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>""" % (Movimentos.x, Movimentos.y, Movimentos.xfinal, Movimentos.yfinal, Movimentos.a, Movimentos.b, Movimentos.c))
    if Movimentos.rotacao == 270:
        Movimentos.xfinal = Movimentos.x
        Movimentos.yfinal = Movimentos.y - p1
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>""" % (Movimentos.x, Movimentos.y, Movimentos.xfinal, Movimentos.yfinal, Movimentos.a, Movimentos.b, Movimentos.c))
    if Movimentos.rotacao == 360:
        Movimentos.xfinal = Movimentos.x - p1
        Movimentos.yfinal = Movimentos.y
        f.write("""<line x1="%f" y1="%f" x2="%f" y2="%f" style="stroke: rgb(%d, %d, %d); stroke-width: 1px"/>""" % (Movimentos.x, Movimentos.y, Movimentos.xfinal, Movimentos.yfinal, Movimentos.a, Movimentos.b, Movimentos.c))


def do_left(command, parser):
    p1 = command.args['left']
    Movimentos.rotacao += p1
    if Movimentos.rotacao > 360:
        Movimentos.rotacao = p1-360;
    if Movimentos.rotacao <0:
        Movimentos.rotacao = p1+360;


def do_right(command, parser):
    p1 = float(command.args["right"])
    Movimentos.rotacao -= p1
    if Movimentos.rotacao > 360:
        Movimentos.rotacao = p1 - 360;
    elif Movimentos.rotacao < 0:
        Movimentos.rotacao = 360 - p1;


def do_position(command, parser):
    p1 = command.args['x']
    p2= command.args['y']
    Movimentos.x = p1
    Movimentos.y=p2


def do_setx(command, parser):
    x1 = command.args['x']
    Movimentos.x=x1
    Movimentos.y = Movimentos.yfinal


def do_setxy(command, parser):
    x1= command.args['x']
    y1 = command.args['y']
    Movimentos.x = x1
    Movimentos.y = y1


def do_sety(command, parser):
    p1 = command.args['y']
    Movimentos.x = Movimentos.xfinal
    Movimentos.y = Movimentos.y

def do_uppen(command, parser):
    Movimentos.canetaup = True



def do_downpen(command, parser):
    Movimentos.canetadown = False


def do_home(command, parser):
    Movimentos.rotacao == 90
    Movimentos.x= 0
    Movimentos.y= 0


def do_colorpen(command, parser):
    p1 = command.args['a']
    p2 = command.args['b']
    p3 = command.args['c']
    Movimentos.a = p1
    Movimentos.b = p2
    Movimentos.c = p3


def do_make(command, parser):
    p1 = command.args['var']
    p2 = command.args['inteiro']
    parser.vars[p1] = p2

#aula 4 minuto 10
def do_if(command, parser):
    p1 = command.args['var']
    p2 = command.args['sinais']
    p3 = command.args['inteiro']
    p4 = command.args['program']
    if p1>p3:
        parser.vars[p1] = p3
        Command.exec(p4,parser)
    elif p1 < p3:
        parser.vars[p1] = p3
        Command.exec(p4, parser)

    elif p1 == p3:
        parser.vars[p1] = p3
        Command.exec(p4, parser)


def do_while(command, parser):
    var = command.args['var']
    sinais = command.args['sinais']
    p3 = command.args['inteiro']
    p4 = command.args['program']



def do_repeat(command, parser):
    p1 = command.args['repetir']


class Command:
    dispatch_table = {
        "forward": do_forward,
        "back": do_backwards,
        "left": do_left,
        "right": do_right,
        "pos": do_position,
        "setx": do_setx,
        "posxy": do_setxy,
        "sety": do_sety,
        "inicio": do_home,
        "pendown": do_downpen,
        "canetaup": do_uppen,
        "corcaneta": do_colorpen,
        "if": do_if,
        "repeat": do_repeat,
        "make": do_make,
        "while": do_while,
    }

    def __init__(self, command, args):
        self.nome = command
        self.args = args

    def __repr__(self):
        return f"Command({self.nome}, {self.args})"

    def run(self, parser):
        self.dispatch_table[self.nome](self, parser)


    @classmethod
    def exec(self, program, parser):
        for command in program:
            print(Command)
            command.draw(parser)