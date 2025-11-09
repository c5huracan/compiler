from ast_nodes import Number, BinOp, Variable, Assignment

def evaluate(node, env=None):
    if env is None:
        env = {}
    
    if isinstance(node, Number):
        return node.value
    elif isinstance(node, BinOp):
        l = evaluate(node.left, env)
        r = evaluate(node.right, env)
        if node.operator == '+':
            return l + r
        elif node.operator == '-':
            return l - r
        elif node.operator == '*':
            return l * r
        elif node.operator == '/':
            return l / r
    elif isinstance(node, Variable):
        return env[node.name]
    elif isinstance(node, Assignment):
        value = evaluate(node.value, env)
        env[node.name] = value
        return value
