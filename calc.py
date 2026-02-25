"""
极简计算器 - feat/color: 新增彩色终端输出
"""
import math

GREEN  = "\033[92m"
RED    = "\033[91m"
YELLOW = "\033[93m"
RESET  = "\033[0m"

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

def calc_line(line):
    a, op, b = line.strip().split()
    a, b = float(a), float(b)
    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    return ops[op](a, b)

def main():
    print(f"{YELLOW}=== 极简计算器 v1.1 (彩色输出) ==={RESET}")
    print("支持: + - * /")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
            if op in ops:
                result = ops[op](a, b)
                print(f"{GREEN}= {result}{RESET}")
            else:
                print(f"{RED}不支持的运算符{RESET}")
        except Exception as e:
            print(f"{RED}错误: {e}{RESET}")

if __name__ == "__main__":
    main()
