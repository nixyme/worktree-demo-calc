"""
极简计算器 - 合并版: 幂运算 + 取模运算
"""

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("除数不能为零")
    return a / b
def power(a, b):
    """幂运算: a 的 b 次方"""
    return a ** b
def modulo(a, b):
    """取模: a % b"""
    if b == 0: raise ValueError("除数不能为零")
    return a % b

def main():
    print("=== 极简计算器 v1.2 (幂运算 + 取模) ===")
    print("支持: + - * / ^ %")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide, '^': power, '%': modulo}
            if op in ops: print(f"= {ops[op](a, b)}")
            else: print("不支持的运算符")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
