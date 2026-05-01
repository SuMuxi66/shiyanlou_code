
import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def snake_game():
    width, height = 20, 10
    snake = [(width//2, height//2)]
    food = (random.randint(0, width-1), random.randint(0, height-1))
    direction = (1, 0)
    score = 0
    
    print("=== 贪吃蛇游戏 ===")
    print("控制: W(上), S(下), A(左), D(右), Q(退出)")
    print("每3秒自动移动，或按回车键立即移动")
    time.sleep(2)
    
    while True:
        clear_screen()
        
        for y in range(height):
            for x in range(width):
                if (x, y) == food:
                    print('🍎', end='')
                elif (x, y) in snake:
                    print('🐍', end='')
                else:
                    print('⬜', end='')
            print()
        
        print(f"\n得分: {score}")
        
        try:
            import select
            import sys
            rlist, _, _ = select.select([sys.stdin], [], [], 0.5)
            if rlist:
                key = sys.stdin.readline().strip().lower()
                if key == 'w' and direction != (0, 1):
                    direction = (0, -1)
                elif key == 's' and direction != (0, -1):
                    direction = (0, 1)
                elif key == 'a' and direction != (1, 0):
                    direction = (-1, 0)
                elif key == 'd' and direction != (-1, 0):
                    direction = (1, 0)
                elif key == 'q':
                    print("游戏结束！")
                    return
        except:
            pass
        
        head_x, head_y = snake[0]
        new_head = (head_x + direction[0], head_y + direction[1])
        
        if new_head[0] &lt; 0 or new_head[0] &gt;= width or \
           new_head[1] &lt; 0 or new_head[1] &gt;= height or \
           new_head in snake:
            print(f"游戏结束！最终得分: {score}")
            break
        
        snake.insert(0, new_head)
        
        if new_head == food:
            score += 10
            while food in snake:
                food = (random.randint(0, width-1), random.randint(0, height-1))
        else:
            snake.pop()
        
        time.sleep(0.5)

if __name__ == "__main__":
    snake_game()

