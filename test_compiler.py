from lexer import lexer
from parser import Parser
from evaluator import evaluate
from codegen import codegen

def test_arithmetic():
    """Test basic arithmetic expressions"""
    tests = [
        ("3 + 5 * 2", 13),
        ("10 - 2 * 3", 4),
        ("(10 - 2) * 3", 24),
        ("100 / 5 / 4", 5.0),
        ("2 + 3 * 4 - 5", 9)
    ]
    
    for expression, expected in tests:
        tokens = lexer(expression)
        parser = Parser(tokens)
        ast = parser.expression()
        result = evaluate(ast)
        assert result == expected, f"{expression} failed: got {result}, expected {expected}"
        print(f"✓ {expression} = {result}")

def test_variables():
    """Test variable assignment and usage"""
    env = {}
    
    # Test assignment
    tokens = lexer('x = 5')
    parser = Parser(tokens)
    ast = parser.statement()
    result = evaluate(ast, env)
    assert result == 5
    assert env['x'] == 5
    print("✓ x = 5")
    
    # Test variable usage
    tokens = lexer('x + 3')
    parser = Parser(tokens)
    ast = parser.statement()
    result = evaluate(ast, env)
    assert result == 8
    print("✓ x + 3 = 8")

def test_codegen():
    """Test code generation"""
    tests = [
        ("3 + 5 * 2", "(3 + (5 * 2))"),
        ("x = 5", "x = 5"),
        ("y = x + 2", "y = (x + 2)")
    ]
    
    for expression, expected in tests:
        tokens = lexer(expression)
        parser = Parser(tokens)
        ast = parser.statement()
        code = codegen(ast)
        assert code == expected, f"{expression} failed: got {code}, expected {expected}"
        print(f"✓ {expression} → {code}")

if __name__ == "__main__":
    print("Testing arithmetic...")
    test_arithmetic()
    print("\nTesting variables...")
    test_variables()
    print("\nTesting code generation...")
    test_codegen()
    print("\n✅ All tests passed!")