"""
极简计算器 - feat/sqrt: 新增平方根
"""
import math

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("除数不能为零")
    return a / b
def sqrt(a):
    """平方根"""
    if a < 0: raise ValueError("不能对负数开平方根")
    return math.sqrt(a)

def main():
    print("=== 极简计算器 v1.1 (新增平方根) ===")
    print("支持: + - * /  |  输入 'sqrt 16' 计算平方根")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        try:
            parts = expr.split()
            if len(parts) == 2 and parts[0].lower() == 'sqrt':
                print(f"= {sqrt(float(parts[1]))}")
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
