# kryth/cli.py

import sys
import sympy as sp
from sympy.parsing.sympy_parser import parse_expr

x = sp.Symbol('x')
y = sp.Symbol('y')

def parse_line(line):
    tokens = line.strip().split()
    if not tokens:
        return

    cmd = tokens[0]

    try:
        if cmd == "diff":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.diff(expr, x))
        elif cmd == "int":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.integrate(expr, x))
        elif cmd == "log":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.log(expr))
        elif cmd == "sin":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.sin(expr))
        elif cmd == "cos":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.cos(expr))
        elif cmd == "tan":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.tan(expr))
        elif cmd == "eval":
            expr = parse_expr(" ".join(tokens[1:-1]))
            val = float(tokens[-1])
            print("→", expr.evalf(subs={x: val}))
        elif cmd == "expand":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.expand(expr))
        elif cmd == "factor":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.factor(expr))
        elif cmd == "simplify":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.simplify(expr))
        elif cmd == "solve":
            expr = parse_expr(" ".join(tokens[1:]))
            print("→", sp.solve(expr, x))
        elif cmd == "#":
            pass  # comment
        else:
            print(f"❌ Unknown command: {cmd}")
    except Exception as e:
        print(f"⚠️ Error: {e}")

def run_kryth(file_path):
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parse_line(line)
    except FileNotFoundError:
        print(f"⚠️ File '{file_path}' not found.")
