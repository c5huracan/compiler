from ast_nodes import Number, BinOp, Variable, Assignment

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self):
        if self.pos >= len(self.tokens):
            return None
        return self.tokens[self.pos]
    
    def advance(self):
        self.pos += 1

    def expect(self, token_type):
        token = self.current_token()
        if token.type == token_type:
            self.advance()
            return
        raise Exception(f"Expected {token_type}, got {token.type}")
    
    def statement(self):
        token = self.current_token()
        if token and token.type == 'IDENTIFIER':
            if self.pos + 1 < len(self.tokens) and self.tokens[self.pos + 1].type == 'ASSIGN':
                return self.assignment()
            return self.expression()
        return self.expression()

    def assignment(self):
        name_token = self.current_token()
        self.advance()
        self.expect('ASSIGN')
        value = self.expression()
        return Assignment(name_token.value, value)

    def expression(self):
        result = self.term()
        while self.current_token() and self.current_token().value in ['+', '-']:
            op = self.current_token()
            self.advance()
            right = self.term()
            result = BinOp(op.value, result, right)
        return result

    def term(self):
        result = self.factor()
        while self.current_token() and self.current_token().value in ['*', '/']:
            op = self.current_token()
            self.advance()
            right = self.factor()
            result = BinOp(op.value, result, right)
        return result

    def factor(self):
        token = self.current_token()
        if token.type == 'NUMBER':
            self.advance()
            return Number(token.value)
        elif token.type == 'LPAREN':
            self.advance()
            res = self.expression()
            self.expect('RPAREN')
            return res
        elif token.type == 'IDENTIFIER':
            self.advance()
            return Variable(token.value)
        return None