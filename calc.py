"""
极简计算器 - feat/percent: 新增百分比运算
"""

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("除数不能为零")
    return a / b
def percent(a):
    """百分比: a / 100"""
    return a / 100

def main():
    print("=== 极简计算器 v1.1 (新增百分比) ===")
    print("支持: + - * /  |  输入 '50 %' 转换百分比")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        try:
            parts = expr.split()
            if len(parts) == 2 and parts[1] == '%':
                print(f"= {percent(float(parts[0]))}")
            elif len(parts) == 3:
                a, op, b = parts
                a, b = float(a), float(b)
                ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
                if op in ops: print(f"= {ops[op](a, b)}")
                else: print("不支持的运算符")
            else: print("格式错误")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
