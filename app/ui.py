import tkinter as tk  # 导入 Tkinter 库，创建图形用户界面
from tkinter import ttk, messagebox  # 从 Tkinter 库中导入 ttk 和 messagebox 模块

class App(tk.Tk):  # 创建一个继承自 tk.Tk 的 App 类
    def __init__(self):
        super().__init__()  # 调用父类的构造方法

        self.title("任务管理器")  # 设置窗口标题
        self.geometry("600x400")  # 设置窗口大小

        self.create_widgets()  # 调用创建控件的方法

    def create_widgets(self):
        # 创建顶部的模块选择按钮框架
        self.module_frame = ttk.Frame(self)  # 创建一个 ttk.Frame 并添加到主窗口
        self.module_frame.pack(pady=10)  # 设置框架的布局和间距

        # 创建红果按钮并设置其命令
        self.btn_hongguo = ttk.Button(self.module_frame, text="红果", command=self.show_hongguo_tasks)
        self.btn_hongguo.grid(row=0, column=0, padx=5)  # 将按钮放置在 grid 布局中的 (0, 0) 位置

        # 创建抖音按钮并设置其命令
        self.btn_douyin = ttk.Button(self.module_frame, text="抖音极速版", command=self.show_douyin_tasks)
        self.btn_douyin.grid(row=0, column=1, padx=5)  # 将按钮放置在 grid 布局中的 (0, 1) 位置

        # 创建快手按钮并设置其命令
        self.btn_kuaishou = ttk.Button(self.module_frame, text="快手极速版", command=self.show_kuaishou_tasks)
        self.btn_kuaishou.grid(row=0, column=2, padx=5)  # 将按钮放置在 grid 布局中的 (0, 2) 位置

        # 创建任务参数设置区框架
        self.task_frame = ttk.Frame(self)  # 创建一个 ttk.Frame 并添加到主窗口
        self.task_frame.pack(pady=20)  # 设置框架的布局和间距

        # 创建任务说明标签，改为使用 grid 布局
        self.task_label = ttk.Label(self.task_frame, text="选择一个模块来设置任务")
        self.task_label.grid(row=0, column=0, columnspan=3, pady=10)  # 将标签放置在框架中

    def show_hongguo_tasks(self):
        self.clear_task_frame()  # 清除任务框架中的所有控件，但保留任务标签
        self.task_label.config(text="红果任务设置")  # 更新任务标签的文本

        # 添加具体任务的参数设置
        self.create_task_input_with_button("开每日宝箱", row=1, command=self.execute_hongguo_task)
        self.create_task_input_with_button("看短剧", row=2, command=self.execute_hongguo_task)
        self.create_task_input_with_button("开每日宝箱+看短剧", row=3, command=self.execute_hongguo_task)

    def show_douyin_tasks(self):
        self.clear_task_frame()  # 清除任务框架中的所有控件，但保留任务标签
        self.task_label.config(text="抖音极速版任务设置")  # 更新任务标签的文本

        # 添加具体任务的参数设置
        self.create_task_input_with_button("任务1", row=1, command=self.execute_douyin_task)
        self.create_task_input_with_button("任务2", row=2, command=self.execute_douyin_task)

    def show_kuaishou_tasks(self):
        self.clear_task_frame()  # 清除任务框架中的所有控件，但保留任务标签
        self.task_label.config(text="快手极速版任务设置")  # 更新任务标签的文本

        # 添加具体任务的参数设置
        self.create_task_input_with_button("任务1", row=1, command=self.execute_kuaishou_task)
        self.create_task_input_with_button("任务2", row=2, command=self.execute_kuaishou_task)

    def create_task_input_with_button(self, task_name, row, command):
        label = ttk.Label(self.task_frame, text=task_name)  # 创建任务名称标签
        label.grid(row=row, column=0, padx=5, pady=5)  # 将标签放置在 grid 布局中的指定位置

        entry = ttk.Entry(self.task_frame)  # 创建任务参数输入框
        entry.grid(row=row, column=1, padx=5, pady=5)  # 将输入框放置在 grid 布局中的指定位置

        btn_execute = ttk.Button(self.task_frame, text="执行任务", command=lambda: command(task_name, entry.get()))
        btn_execute.grid(row=row, column=2, padx=5, pady=5)  # 将按钮放置在 grid 布局中的指定位置

    def clear_task_frame(self):
        # 仅清除任务框架中不包括任务标签的控件
        for widget in self.task_frame.winfo_children():
            if widget != self.task_label:
                widget.destroy()

    def execute_hongguo_task(self, task_name, param):
        self.execute_task("红果", task_name, param)

    def execute_douyin_task(self, task_name, param):
        self.execute_task("抖音极速版", task_name, param)

    def execute_kuaishou_task(self, task_name, param):
        self.execute_task("快手极速版", task_name, param)

    def execute_task(self, module_name, task_name, param):
        # 在这里实现具体的任务执行逻辑
        messagebox.showinfo("执行任务", f"正在执行{module_name}的任务：{task_name}\n参数: {param}")  # 显示任务执行信息

if __name__ == "__main__":
    app = App()  # 创建 App 实例
    app.mainloop()  # 运行主循环
