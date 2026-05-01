
import os

def notepad():
    print("=== 简易记事本 ===")
    
    while True:
        print("\n--- 菜单 ---")
        print("1. 创建新笔记")
        print("2. 查看笔记")
        print("3. 列出所有笔记")
        print("0. 退出")
        
        choice = input("\n请选择: ")
        
        if choice == "0":
            print("再见！")
            break
        elif choice == "1":
            filename = input("请输入笔记文件名: ").strip()
            if not filename:
                print("文件名不能为空！")
                continue
            
            print("请输入笔记内容（输入 END 结束）:")
            lines = []
            while True:
                line = input()
                if line == "END":
                    break
                lines.append(line)
            
            content = "\n".join(lines)
            try:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"笔记已保存到 {filename}")
            except Exception as e:
                print(f"保存失败: {e}")
                
        elif choice == "2":
            filename = input("请输入要查看的笔记文件名: ").strip()
            if os.path.exists(filename):
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        content = f.read()
                    print(f"\n--- {filename} ---")
                    print(content)
                except Exception as e:
                    print(f"读取失败: {e}")
            else:
                print("文件不存在！")
                
        elif choice == "3":
            print("\n--- 当前目录笔记 ---")
            for file in os.listdir('.'):
                if file.endswith('.txt') or file.endswith('.md'):
                    print(f"- {file}")
                    
        else:
            print("无效选择！")

if __name__ == "__main__":
    notepad()

