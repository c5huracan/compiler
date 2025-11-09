from lexer import lexer
from parser import Parser
from evaluator import evaluate
from codegen import codegen

def main():
    print("Simple Compiler - Enter expressions or assignments (or 'quit' to exit)")
    env = {}
    
    while True:
        try:
            text = input(">>> ")
            if text.strip().lower() == 'quit':
                break
            
            # Lex and parse
            tokens = lexer(text)
            parser = Parser(tokens)
            ast = parser.statement()
            
            # Evaluate
            result = evaluate(ast, env)
            print(f"Result: {result}")
            
            # Show generated code
            code = codegen(ast)
            print(f"Code: {code}")
            
            # Show environment if variables exist
            if env:
                print(f"Env: {env}")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()