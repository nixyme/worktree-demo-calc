"""
极简计算器 - feat/batch: 新增批量计算（从文件读取）
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

def calc_line(line):
    a, op, b = line.strip().split()
    a, b = float(a), float(b)
    ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
    return ops[op](a, b)

def main():
    print("=== 极简计算器 v1.1 (新增批量计算) ===")
    print("支持: + - * /  |  输入 'batch 文件名' 批量计算")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        if expr.lower().startswith('batch '):
            fname = expr[6:].strip()
            try:
                with open(fname) as f:
                    for line in f:
                        if line.strip():
                            print(f"{line.strip()} = {calc_line(line)}")
            except FileNotFoundError:
                print(f"文件不存在: {fname}")
            continue
        try:
            print(f"= {calc_line(expr)}")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
