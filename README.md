# Simple Compiler

Ever wondered how programming languages actually work? This is a compiler built from scratch to demystify the magic. It handles arithmetic, variables, and can both execute code *and* generate new Python code from the same parsed structure.

## What It Does

Turn this: `x = 3 + 5 * 2` 

Into this: An abstract syntax tree, a computed result (13), *and* generated Python code. All from one parsing pass.

**Key capabilities:**
- 🔍 **Lexical Analysis** - Breaks code into meaningful tokens
- 🌳 **Recursive Descent Parser** - Builds an AST with proper operator precedence  
- ⚡ **Evaluation Engine** - Executes expressions with variable environments
- 🔧 **Code Generator** - Transforms ASTs back into Python code

## Architecture

The compiler uses a dual-pipeline design that shares a common front-end:

**Evaluation Pipeline:**
```
Text → Lexer → Tokens → Parser → AST → Evaluator → Result
```

**Code Generation Pipeline:**
```
Text → Lexer → Tokens → Parser → AST → Code Generator → Python Code
```

Same parsing, multiple backends. Parse once, use everywhere.

## Quick Start

**Try it interactively:**

```bash
python3 main.py
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

**Run the test suite:**

```bash
python3 test_compiler.py
```

## What You Can Write

- **Math**: `3 + 5 * 2`, `(10 - 2) / 4`
- **Variables**: `x = 42`, `result = x + 10`  
- **Complex expressions**: `y = (a + b) * (c - d)`

Supports `+`, `-`, `*`, `/`, parentheses, variable assignment, and nested expressions.

## Code Example

```python
from lexer import lexer
from parser import Parser
from evaluator import evaluate

# Parse and evaluate an expression
tokens = lexer("x = 3 + 5")
parser = Parser(tokens)
ast = parser.statement()

env = {}
result = evaluate(ast, env)
print(result)  # 8
print(env)     # {'x': 8}
```

## Project Structure

```
├── lexer.py          # Tokenization
├── ast_nodes.py      # AST node definitions
├── parser.py         # Recursive descent parser
├── evaluator.py      # Execution engine with environments
├── codegen.py        # Python code generation
├── main.py           # Interactive REPL
└── test_compiler.py  # Test suite
```

## Why This Exists

This compiler was built as a deliberate learning exercise to understand:
- How source code transforms into executable instructions
- Recursive descent parsing and operator precedence
- AST-based compiler architecture
- Separation of parsing from execution/generation

Each component was built one piece at a time, focusing on understanding how the pipeline fits together rather than just getting it working.

## What's Next?

Potential extensions:
- Add comparison operators and boolean logic
- Implement control flow (if/else, loops)
- Support functions and function calls
- Generate code for other languages (C, LISP, JavaScript)
- Add optimization passes
