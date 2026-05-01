
def calculator():
    print("=== 简易计算器 ===")
    print("支持: + - * /, 输入 q 退出")
    
    while True:
        try:
            expr = input("\n请输入表达式: ").strip()
            
            if expr.lower() == 'q':
                print("再见！")
                break
            
            if not expr:
                continue
            
            result = eval(expr)
            print(f"= {result}")
            
        except ZeroDivisionError:
            print("错误: 除数不能为0！")
        except SyntaxError:
            print("错误: 请输入正确的表达式！")
        except Exception as e:
            print(f"错误: {e}")

if __name__ == "__main__":
    calculator()

