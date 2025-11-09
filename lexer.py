from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def lexer(text):
    tokens = []
    i = 0
    while i < len(text):
        char = text[i]
        if char == ' ':
            i += 1
            continue
        elif char == '+':
            tokens.append(Token('OPERATOR', '+'))
        elif char == '-':
            tokens.append(Token('OPERATOR', '-'))
        elif char == '*':
            tokens.append(Token('OPERATOR', '*'))
        elif char == '/':
            tokens.append(Token('OPERATOR', '/'))
        elif char.isdigit():
            num = ''
            while i < len(text) and text[i].isdigit():
                num += text[i]
                i += 1
            num = int(num)
            tokens.append(Token('NUMBER', num))
            i -= 1
        elif char.isalpha():
            var = ''
            while i < len(text) and text[i].isalpha():
                var += text[i]
                i += 1
            tokens.append(Token('IDENTIFIER', var))
            i -= 1
        elif char == '=':
            tokens.append(Token('ASSIGN', '='))
        elif char == '(':
            tokens.append(Token('LPAREN', '('))
        elif char == ')':
            tokens.append(Token('RPAREN', ')'))
        i += 1
    return tokens