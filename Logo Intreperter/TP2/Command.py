
f=open("ex1.svg","w")
f.write("""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 102.00 102.00">""")

def do_forward(command, parser):
    p1 = float (command.args["forward"])
    print(p1)
    f.write("%d" % p1)

def do_backwards(command, parser):
    p1 = command.args['back']


def do_left(command, parser):
    p1 = command.args['left']


def do_right(command, parser):
    p1 = float(command.args["right"])
    print(p1)
    f.write("%d" % p1)


def do_position(command, parser):
    p1 = command.args['posicao']


def do_setx(command, parser):
    x1 = command.args['posicaox']


def do_sety(command, parser):
    p1 = command.args['posicaoy']


def do_uppen(command, parser):
    p1 = command.args['canetaup']


def do_downpen(command, parser):
    p1 = command.args['canetadown']


def do_home(command, parser):
    p1 = command.args['home']


def do_colorpen(command, parser):
    r = command.args['corcaneta']



def do_make(command, parser):
    p1 = command.args['make']


def do_if(command, parser):
    p1 = command.args['if']


def do_while(command, parser):
    var = command.args['var']
    sinais = command.args['sinais']



def do_repeat(command, parser):
    p1 = command.args['repetir']


class Command:
    dispatch_table = {
        "forward": do_forward,
        "backwards": do_backwards,
        "left": do_left,
        "right": do_right,
        "setpos": do_position,
        "setx": do_setx,
        "sety": do_sety,
        "home": do_home,
        "pendown": do_uppen,
        "penup": do_downpen,
        "setpencolor": do_colorpen,
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
