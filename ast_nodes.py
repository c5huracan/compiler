from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Number:
    value: int | float

@dataclass
class BinOp:
    operator: str
    left: Number | BinOp | Variable
    right: Number | BinOp | Variable

@dataclass
class Variable:
    name: str

@dataclass
class Assignment:
    name: str
    value: Number | BinOp | Variable