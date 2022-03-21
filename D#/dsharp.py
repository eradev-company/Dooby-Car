from sly import Lexer, Parser

class Lexer(Lexer):
    tokens = { FORWARD, BACKWARD, LEFT, RIGHT, STOP , ARG, DURING, ENDLINE,}
    ignore = ' \t'

    # Tokens
    FORWARD = r'FORWARD'
    BACKWARD = r'BACKWARD'
    LEFT = r'LEFT'
    RIGHT = r'RIGHT'
    DURING = r'DURING'
    STOP = r'STOP'
    ARG = r'\d+'
    ENDLINE = r'\n+'

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
    

    @_('instruction program')
    def program(self, p):
        pass

    @_('')
    def program(self, p):
        pass
        
    @_('FORWARD ARG during ENDLINE')
    def instruction(self, p):
        print("Moving Forward")
        if p[2]:
          print("During {} sec".format(p[2]))
        #define actions here

    @_('BACKWARD ARG during ENDLINE')
    def instruction(self, p):
        print("Moving Backward")
        if p[2]:
          print("During {} sec".format(p[2]))
          #define actions here

    @_('RIGHT ARG during ENDLINE')
    def instruction(self, p):
        print("Turning Right")
        if p[2]:
          print("During {} sec".format(p[2]))
        #define actions here

    @_('LEFT ARG during ENDLINE')
    def instruction(self, p):
        print("Turning left")
        if p[2]:
          print("During {} sec".format(p[2]))
        #define actions here

    @_('')
    def during(self, p):
        pass

    @_('DURING ARG')
    def during(self, p):
        return p[1]
      
    @_('STOP')
    def instruction(self, p):
        print("Stopping!")
        #define actions here   

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
    parser.parse(lexer.tokenize(data))

