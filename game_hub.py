
import sys
import os

def import_game_module(file_name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(file_name.replace('.py', ''), file_name)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    print("=" * 40)
    print("      🎮 Python 游戏集合 🎮")
    print("=" * 40)
    
    games = {
        "1": ("猜数字游戏", "猜数字.py"),
        "2": ("石头剪刀布", "石头剪刀布.py"),
        "3": ("跳7游戏", "jump7.py"),
        "4": ("两数之和算法", "两数之和.py"),
    }
    
    while True:
        print("\n--- 游戏菜单 ---")
        for key, (name, _) in games.items():
            print(f"{key}. {name}")
        print("0. 退出")
        
        choice = input("\n请选择: ")
        
        if choice == "0":
            print("👋 再见！")
            break
        elif choice in games:
            game_name, game_file = games[choice]
            print(f"\n正在启动: {game_name}")
            print("-" * 30)
            
            try:
                if choice in ["1", "2"]:
                    module = import_game_module(game_file)
                    if choice == "1":
                        module.guess_number()
                    else:
                        module.rock_paper_scissors()
                else:
                    with open(game_file, 'r', encoding='utf-8') as f:
                        code = f.read()
                    exec(code)
            except Exception as e:
                print(f"运行出错: {e}")
        else:
            print("无效选择！")

if __name__ == "__main__":
    main()

