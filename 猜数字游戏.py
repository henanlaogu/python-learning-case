import random

# 生成一个1到100之间的随机数
number_to_guess = random.randint(1, 100)
guess_count = 0
while True:
    try:
        # 获取玩家的猜测
        user_guess = int(input("请猜一个1到100之间的数字: "))
        guess_count += 1
        if user_guess == number_to_guess:
            print(f"恭喜你，猜对了！你一共猜了{guess_count}次。")
            break
        elif user_guess < number_to_guess:
            print("猜的数字小了，再试试吧。")
        else:
            print("猜的数字大了，再试试吧。")
    except ValueError:
        print("请输入整数哦，重新猜一下吧。")