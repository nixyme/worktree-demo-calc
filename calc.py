"""
极简计算器 - feat/modulo: 新增取模运算
"""

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("除数不能为零")
    return a / b
def modulo(a, b):
    """取模: a % b"""
    if b == 0: raise ValueError("除数不能为零")
    return a % b

def main():
    print("=== 极简计算器 v1.1 (新增取模运算) ===")
    print("支持: + - * / %")
    while True:
        expr = input("输入表达式 (如 10 % 3) 或 q 退出: ").strip()
        if expr.lower() == 'q': break
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide, '%': modulo}
            if op in ops: print(f"= {ops[op](a, b)}")
            else: print("不支持的运算符")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
