
import random

def rock_paper_scissors():
    choices = ["石头", "剪刀", "布"]
    win_count = 0
    lose_count = 0
    draw_count = 0
    
    print("=== 石头剪刀布游戏 ===")
    print("输入: 1-石头, 2-剪刀, 3-布, 0-退出")
    
    while True:
        try:
            user_choice = input("\n请选择: ")
            
            if user_choice == "0":
                print("\n=== 游戏结束 ===")
                print(f"胜: {win_count}, 负: {lose_count}, 平: {draw_count}")
                break
            
            if user_choice not in ["1", "2", "3"]:
                print("请输入有效的选择！")
                continue
            
            user_idx = int(user_choice) - 1
            computer_idx = random.randint(0, 2)
            
            user = choices[user_idx]
            computer = choices[computer_idx]
            
            print(f"你出了: {user}")
            print(f"电脑出了: {computer}")
            
            if user_idx == computer_idx:
                print("平局！")
                draw_count += 1
            elif (user_idx == 0 and computer_idx == 1) or \
                 (user_idx == 1 and computer_idx == 2) or \
                 (user_idx == 2 and computer_idx == 0):
                print("你赢了！🎉")
                win_count += 1
            else:
                print("你输了！😢")
                lose_count += 1
                
        except KeyboardInterrupt:
            print("\n\n游戏被中断")
            break

if __name__ == "__main__":
    rock_paper_scissors()

