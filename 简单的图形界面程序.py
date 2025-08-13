import tkinter as tk

# 创建主窗口
root = tk.Tk()
root.title("简单GUI示例")

# 创建一个文本框
text_box = tk.Text(root, height=50, width=100)
text_box.pack()

# 创建一个按钮
def show_message():
    text_box.insert(tk.END, "欢迎来到地球Online2.0版本实况游戏，请尽情体验人生吧！")

button = tk.Button(root,text="降生之初",command=show_message)
button.pack()

# 启动主窗口的事件循环
root.mainloop()
