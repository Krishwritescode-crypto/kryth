import sympy as sp

# Environment to store variables and functions
env = {}

def evaluate(expr: str):
    try:
        expr = expr.replace('^', '**')

        # Function definition: fn square(x) = x^2
        if expr.startswith("fn "):
            fn_def = expr[3:].split("=")
            header = fn_def[0].strip()
            body = fn_def[1].strip()
            name = header.split("(")[0].strip()
            args = header[header.find("(")+1:header.find(")")].split(",")
            args = [arg.strip() for arg in args]
            env[name] = ("function", args, body)
            return f"Function '{name}' defined."

        # Variable assignment: a = 10
        if "=" in expr and not expr.startswith("fn "):
            var, val = expr.split("=", 1)
            var = var.strip()
            val = val.strip()
            val_result = sp.sympify(val, locals=env).evalf()
            env[var] = val_result
            return f"{var} = {val_result}"

        # Function call: square(4)
        if "(" in expr and ")" in expr:
            name = expr.split("(")[0].strip()
            if name in env and env[name][0] == "function":
                args, body = env[name][1], env[name][2]
                vals = expr[expr.find("(")+1:expr.find(")")].split(",")
                local_env = dict(zip(args, vals))
                for k, v in local_env.items():
                    body = body.replace(k, v)
                return evaluate(body)

        # Solve expressions: solve(expr, x)
        if expr.startswith("solve("):
            inner = expr[6:-1]
            equation, symbol = inner.split(",")
            equation = sp.sympify(equation.strip())
            symbol = sp.Symbol(symbol.strip())
            result = sp.solve(equation, symbol)
            return result

        # Default expression evaluation
        result = sp.sympify(expr, locals=env)
        return result.evalf()

    except Exception as e:
        return f"Error: {str(e)}"


# Main program to run Kryth code from a file or REPL

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Kryth REPL v0.2. Type 'exit' to quit.")
        while True:
            line = input(">>> ")
            if line.lower() in ["exit", "quit"]:
                break
            print(evaluate(line))
    else:
        with open(sys.argv[1], 'r') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line:
                    print(">>", line)
                    print(evaluate(line))
