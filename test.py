"""实现一个建议GUI登录系统"""
import tkinter as tk
from tkinter import messagebox
import hashlib
# 模拟用户数据库
user_db = {
    "user1": hashlib.sha256("password1".encode()).hexdigest(),
    "user2": hashlib.sha256("password2".encode()).hexdigest(),
}
def register():
    """处理注册逻辑"""
    username = entry_username.get()
    password = entry_password.get()
    if not username or not password:
        messagebox.showerror("注册失败", "用户名和密码不能为空")
        return
    if username in user_db:
        messagebox.showerror("注册失败", "用户名已存在")
        return
    user_db[username] = hash_password(password)
    messagebox.showinfo("注册成功", f"用户 {username} 注册成功！")
def hash_password(password):
    """对密码进行哈希处理"""
    return hashlib.sha256(password.encode()).hexdigest()
def login():
    """处理登录逻辑"""
    username = entry_username.get()
    password = entry_password.get()
    hashed_password = hash_password(password)
    if username in user_db and user_db[username] == hashed_password:
        messagebox.showinfo("登录成功", f"欢迎, {username}!")
    else:
        messagebox.showerror("登录失败", "用户名或密码错误")
# 创建主窗口
root = tk.Tk()
root.title("登录系统")
# 创建并放置标签和输入框
tk.Label(root, text="用户名:").grid(row=0, column=0)
entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1)
tk.Label(root, text="密码:").grid(row=1, column=0)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1)
# 创建并放置登录按钮
# 创建并放置登录和注册按钮
btn_login = tk.Button(root, text="登录", command=login)
btn_login.grid(row=2, column=0)
btn_register = tk.Button(root, text="注册", command=register)
btn_register.grid(row=2, column=1)
# 运行主循环
root.mainloop()



