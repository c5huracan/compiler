from ast_nodes import Number, BinOp, Variable, Assignment

def codegen(node):
    if isinstance(node, Number):
        return str(node.value)
    elif isinstance(node, BinOp):
        l = codegen(node.left)
        r = codegen(node.right)
        return f"({l} {node.operator} {r})"
    elif isinstance(node, Variable):
        return node.name
    elif isinstance(node, Assignment):
        return f"{node.name} = {codegen(node.value)}"

def generate_python_program(ast):
    code = codegen(ast)
    return f"print({code})"

def generate_python_assignment(ast):
    code = codegen(ast)
    return f"res = {code}"