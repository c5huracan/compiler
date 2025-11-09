# Simple Compiler

A educational compiler built from scratch that supports arithmetic expressions, variables, and code generation.

## Features

- **Lexical Analysis**: Tokenizes expressions and statements
- **Parsing**: Recursive descent parser with proper operator precedence
- **AST**: Clean abstract syntax tree representation
- **Evaluation**: Execute expressions with variable support
- **Code Generation**: Generate Python code from AST

## Architecture
Text → Lexer → Tokens → Parser → AST → Evaluator → Result ↓ Code Generator → Python Code

Copied!
## Components

- `lexer.py` - Tokenization
- `ast_nodes.py` - AST node definitions
- `parser.py` - Recursive descent parser
- `evaluator.py` - AST evaluation with environment
- `codegen.py` - Python code generation
- `main.py` - Interactive CLI
- `test_compiler.py` - Test suite

## Usage

### Interactive Mode
python main.py

Copied!

3 + 5 * 2 Result: 13 Code: (3 + (5 * 2))

x = 10 Result: 10 Code: x = 10 Env: {'x': 10}

x + 5 Result: 15 Code: (x + 5) Env: {'x': 10}

Copied!
### Run Tests
python test_compiler.py

Copied!
## Supported Syntax

- **Arithmetic**: `+`, `-`, `*`, `/`
- **Parentheses**: `(`, `)`
- **Variables**: `x`, `foo`, `my_var`
- **Assignment**: `x = 5`
- **Expressions**: `x + 3 * (y - 2)`

## Example
from lexer import lexer from parser import Parser from evaluator import evaluate

Parse and evaluate
tokens = lexer("x = 3 + 5") parser = Parser(tokens) ast = parser.statement() env = {} result = evaluate(ast, env) print(result) # 8 print(env) # {'x': 8}

Copied!
## Learning Journey

This compiler was built as a learning project to understand:
- How compilers transform source code
- Recursive descent parsing
- AST-based architecture
- Separation of concerns in compiler design

Each component was built deliberately, one piece at a time, to understand how the pipeline fits together.