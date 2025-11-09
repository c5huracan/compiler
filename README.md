# Simple Compiler

A educational compiler built from scratch that supports arithmetic expressions, variables, and code generation.

## Features

- **Lexical Analysis**: Tokenizes expressions and statements
- **Parsing**: Recursive descent parser with proper operator precedence
- **AST**: Clean abstract syntax tree representation
- **Evaluation**: Execute expressions with variable support
- **Code Generation**: Generate Python code from AST

## Architecture

**Evaluation Pipeline:**
Text → Lexer → Tokens → Parser → AST → Evaluator → Result

**Code Generation Pipeline:**
Text → Lexer → Tokens → Parser → AST → Code Generator → Python Code

Both pipelines share the same front-end (Lexer and Parser) that produces an AST but have different back-ends.

The AST can then be:
- Evaluated to produce a result
- Transformed into Python code

This separation allows the same parsed structure to be used for multiple purposes.

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

```bash
python main.py
```

```
>>> 3 + 5 * 2
Result: 13
Code: (3 + (5 * 2))

>>> x = 10
Result: 10
Code: x = 10
Env: {'x': 10}

>>> x + 5
Result: 15
Code: (x + 5)
Env: {'x': 10}
```

### Run Tests

```bash
python test_compiler.py
```

## Supported Syntax

- **Arithmetic**: `+`, `-`, `*`, `/`
- **Parentheses**: `(`, `)`
- **Variables**: `x`, `foo`, `my_var`
- **Assignment**: `x = 5`
- **Expressions**: `x + 3 * (y - 2)`

```python
from lexer import lexer
from parser import Parser
from evaluator import evaluate

# Parse and evaluate
tokens = lexer("x = 3 + 5")
parser = Parser(tokens)
ast = parser.statement()
env = {}
result = evaluate(ast, env)
print(result)  # 8
print(env)     # {'x': 8}
```

## Learning Journey

This compiler was built as a learning project to understand:
- How compilers transform source code
- Recursive descent parsing
- AST-based architecture
- Separation of concerns in compiler design

Each component was built deliberately, one piece at a time, to understand how the pipeline fits together.