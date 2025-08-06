while 3<4:
    # 获取用户输入的两个数字
    num1 = float(input("请输入第一个数字"))
    num2 = float(input("请输入第二个数字"))

    # 获取用户选择的运算操作
    operation = input("请选择运算操作（+、-、*、）:")

    # 根据操作符进行相应计算并输出结果
    if operation == "+":
        result = num1 + num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == "-":
        result = num1 - num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == "*":
        result = num1 * num2
        print(f"{num1} {operation} {num2} = {result}")
    elif operation == "/":
        if num2 == 0:
            print("除数不能为0，请重新输入")
        else:
            result = num1 / num2
            print(f"{num1} {operation} {num2} = {result}")
    else:
        print("输入的运算符号不符合要求，请重新输入。")

