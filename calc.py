"""
极简计算器 - feat/version: 新增版本信息
"""
import math

__version__ = "1.1.0"
__author__  = "Worktree Demo"
__date__    = "2026-02-25"

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

HELP_TEXT = """
命令列表:
  <数字> <运算符> <数字>  基本运算 (如: 3 + 4)
  help                   显示此帮助
  q                      退出

运算符:
  +  加法    -  减法
  *  乘法    /  除法
"""

def main():
    print(f"=== 极简计算器 v{__version__} ===")
    print(f"作者: {__author__}  日期: {__date__}")
    print("支持: + - * /  |  输入 version 查看版本")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        if expr.lower() == 'version':
            print(f"版本: {__version__}  作者: {__author__}  日期: {__date__}")
            continue
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
            if op in ops: print(f"= {ops[op](a, b)}")
            else: print("不支持的运算符")
        except Exception as e:
            print(f"{RED}错误: {e}{RESET}")

if __name__ == "__main__":
    main()
