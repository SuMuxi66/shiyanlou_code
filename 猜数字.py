
import random

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("=== 猜数字游戏 ===")
    print("我想了一个1到100之间的数字，来猜猜看！")
    
    while True:
        try:
            guess = int(input("请输入你猜的数字: "))
            attempts += 1
            
            if guess &lt; 1 or guess &gt; 100:
                print("请输入1到100之间的数字！")
                continue
            
            if guess &lt; secret_number:
                print("太小了！再大一点~")
            elif guess &gt; secret_number:
                print("太大了！再小一点~")
            else:
                print(f"恭喜你！猜对了！答案就是{secret_number}")
                print(f"你一共猜了{attempts}次")
                break
                
        except ValueError:
            print("请输入有效的数字！")

if __name__ == "__main__":
    guess_number()

