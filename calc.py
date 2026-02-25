"""
极简计算器 - feat/power: 新增幂运算
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def power(a, b):
    """幂运算: a 的 b 次方"""
    return a ** b

def main():
    print("=== 极简计算器 v1.1 (新增幂运算) ===")
    print("支持: + - * / ^")
    while True:
        expr = input("输入表达式 (如 2 ^ 8) 或 q 退出: ").strip()
        if expr.lower() == 'q':
            break
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            if op == '+':   print(f"= {add(a, b)}")
            elif op == '-': print(f"= {subtract(a, b)}")
            elif op == '*': print(f"= {multiply(a, b)}")
            elif op == '/': print(f"= {divide(a, b)}")
            elif op == '^': print(f"= {power(a, b)}")
            else:           print("不支持的运算符")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
