student_scores = {}

while True:
    print("1.添加学生成绩")
    print("2.查询学生成绩")
    print("3.计算班级平均成绩")
    print("4.退出")
    choice = input("请输入你的选择（1-4）：")

    if choice == "1":
        name = input("请输入学生姓名")
        score = float(input("请输入学生的成绩："))
        student_scores[name] = score
        print("学生成绩添加成功")
    elif choice == "2":
        name = input("请输入要查询成绩的学生姓名：")
        if name in student_scores:
            print(f"{name}的成绩是：{student_scores[name]}")
        else:
            print(f"不存在名为{name}的学生成绩记录。")
    elif choice == "3":
        if len(student_scores) == 0:
            print("还没有添加学生成绩，请先添加")
        else:
            total_score = sum(student_scores.values())
            average_score = total_score / len(student_scores)
            print(f"班级平均成绩是：{average_score}")
    elif choice == "4":
        print("感谢使用，程序已退出")
        break
    else:
        print("输入错误，请重新输入")
