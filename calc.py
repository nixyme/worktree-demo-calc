"""
极简计算器 - feat/help: 新增帮助命令
"""

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0: raise ValueError("除数不能为零")
    return a / b

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
    print("=== 极简计算器 v1.1 (新增帮助) ===")
    print("输入 help 查看帮助")
    while True:
        expr = input("> ").strip()
        if expr.lower() == 'q': break
        if expr.lower() == 'help': print(HELP_TEXT); continue
        try:
            a, op, b = expr.split()
            a, b = float(a), float(b)
            ops = {'+': add, '-': subtract, '*': multiply, '/': divide}
            if op in ops: print(f"= {ops[op](a, b)}")
            else: print("不支持的运算符，输入 help 查看帮助")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    main()
