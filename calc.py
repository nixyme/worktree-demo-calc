"""
极简计算器 - feat/memory: 新增内存存储 (MS/MR/MC)
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
    print("=== 极简计算器 v1.1 (新增内存存储) ===")
    print("支持: + - * /  |  ms=存储 mr=读取 mc=清除")
    memory = 0
    while True:
        expr = input("> ").strip().lower()
        if expr == 'q': break
        if expr == 'mr': print(f"内存: {memory}"); continue
        if expr == 'mc': memory = 0; print("内存已清除"); continue
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
            if op in ops:
                result = ops[op](a, b)
                print(f"= {result}")
                if expr.startswith('ms'): memory = result; print(f"已存入内存: {memory}")
            else: print("不支持的运算符")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
