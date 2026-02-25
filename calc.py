"""
极简计算器 - feat/history: 新增历史记录
"""

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("除数不能为零")
    return a / b

def main():
    print("=== 极简计算器 v1.1 (新增历史记录) ===")
    print("支持: + - * /  |  输入 history 查看历史")
    history = []
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        if expr.lower() == 'history':
            print("--- 历史记录 ---")
            for i, h in enumerate(history, 1): print(f"  {i}. {h}")
            continue
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
            if op in ops:
                result = ops[op](a, b)
                print(f"= {result}")
                history.append(f"{expr} = {result}")
            else: print("不支持的运算符")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
