from time import sleep
from sly import Lexer, Parser
import motor

class Lexer(Lexer):
    tokens = { FORWARD, BACKWARD, LEFT, RIGHT, STOP , ARG, DURING,}
    ignore = ' \t'

    # Tokens
    FORWARD = r'FORWARD'
    BACKWARD = r'BACKWARD'
    LEFT = r'LEFT'
    RIGHT = r'RIGHT'
    DURING = r'DURING'
    STOP = r'STOP'
    # real number in regex
    ARG = r'\d+\.\d+|\d+'  

    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1

class Parser(Parser):
    tokens = Lexer.tokens
    
    # Grammar rules 
    '''
    program := instruction program
    program := epsilon
    instruction := FORWARD ARG during
    instruction := BACKWARD ARG during
    instruction := LEFT ARG during
    instruction := RIGHT ARG during
    instruction := STOP
    during := epsilon
    during := DURING ARG
    '''

    # Grammar actions

    # program := instruction program
    @_('instruction program')
    def program(self, p):
        motor.stop()
        sleep(1)
        pass

    # program := empty
    @_('')
    def program(self, p):
        pass
        
    # instruction := FORWARD ARG during
    @_('FORWARD ARG during')
    def instruction(self, p):
        if float(p[1])>100: 
            print("Speed too high")
            return
        delay = p[2] if p[2] else 3
        print("Moving Forward {}km/h During {} sec".format(p[1],delay))
        motor.forward(delay, 0 if float(p[1]) == 0 else float(p[1])/2+50)

    # instruction := BACKWARD ARG during
    @_('BACKWARD ARG during')
    def instruction(self, p):
        if float(p[1])>100: 
            print("Speed too high")
            return
        delay = p[2] if p[2] else 3
        print("Moving Backward {}km/h During {} sec".format(p[1],delay))
        motor.backward(delay, float(p[1]))

    # instruction := LEFT ARG during
    @_('RIGHT ARG during')
    def instruction(self, p):
        delay = p[2] if p[2] else 3
        print("Turning Right During {} sec".format(delay))
        motor.right(delay)

    # instruction := RIGHT ARG during
    @_('LEFT ARG during')
    def instruction(self, p):
        delay = p[2] if p[2] else 3
        print("Turning Left During {} sec".format(delay))
        motor.left(delay)

    # during := empty
    @_('')
    def during(self, p):
        pass

    # during := DURING ARG
    @_('DURING ARG')
    def during(self, p):
       return float(p[1])
    
    # instruction := STOP
    @_('STOP')
    def instruction(self, p):
        print("Stopping!")
        motor.stop() 

if __name__ == '__main__':
    import sys
    #try to open the file
    try:
        f = open(sys.argv[1])
    except:
        print("File not found")
        exit()

    if f.read() == "":
        print("File is empty")
        exit()

    if not sys.argv[1].endswith(".d"):
        print("File extension must be .d")
        exit()

    data = ''.join(open(sys.argv[1]).readlines())
    lexer = Lexer()
    parser = Parser()

    try:
        parser.parse(lexer.tokenize(data))
    except KeyboardInterrupt:
        print("Canceling...")

    motor.cleanup()
    exit()

