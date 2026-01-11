import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("電卓")
        self.root.geometry("300x400")

        # 表示エリア
        self.display = tk.Entry(root, font=("Arial", 24), justify="right")
        self.display.pack(fill=tk.X, padx=10, pady=10)

        # ボタン配置
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", "C", "=", "+"]
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(fill=tk.X)

            for btn_text in row:
                btn = tk.Button(
                    frame,
                    text=btn_text,
                    font=("Arial", 18),
                    width=5,
                    height=2
                )
                btn.pack(side=tk.LEFT, padx=2, pady=2)
                btn.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        """ボタンクリック時の処理"""
        btn_text = event.widget["text"]

        if btn_text == "C":
            self.display.delete(0, tk.END)

        elif btn_text == "=":
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                messagebox.showerror("エラー", "無効な式です")

        else:
            self.display.insert(tk.END, btn_text)

# アプリ起動
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
