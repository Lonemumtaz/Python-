import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.minsize(320, 440)
        self.configure(bg="#000000")  # Black background
        self.expression = ""
        self.create_widgets()
        self.bind('<Configure>', self.on_resize)

    def create_widgets(self):
        self.display = tk.Entry(self, font=("Segoe UI", 28), borderwidth=0, relief="flat", justify="right", bg="#222222", fg="#EEEEEE")
        self.display.grid(row=0, column=0, columnspan=4, padx=16, pady=18, sticky="nsew")
        buttons = [
            ('C', 1, 0), ('', 1, 1), ('', 1, 2), ('', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3)
        ]
        self.button_refs = []
        purple = "#800080"  # Purple color
        for (text, row, col) in buttons:
            if text == '':
                continue  # Skip empty placeholders
            # Set purple background for options, default for numbers and '.'
            if text in ['+', '-', '*', '/', 'C', '=']:
                bg_color = purple
                fg_color = "#EEEEEE" if text != 'C' else "#F96D00"
            else:
                bg_color = "#222222"
                fg_color = "#EEEEEE"
            btn = tk.Button(self, text=text, font=("Segoe UI", 20), command=(self.clear if text == 'C' else (self.calculate if text == '=' else lambda t=text: self.append(t))), bg=bg_color, fg=fg_color, borderwidth=0, activebackground="#9932CC" if text in ['+', '-', '*', '/', 'C', '='] else "#393E46")
            btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
            self.button_refs.append(btn)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def on_resize(self, event):
        # Dynamically adjust font size based on window size
        w = self.winfo_width()
        h = self.winfo_height()
        font_size = max(18, min(int(h/22), int(w/18)))
        self.display.config(font=("Segoe UI", font_size+8))
        for btn in self.button_refs:
            btn.config(font=("Segoe UI", font_size))

    def append(self, char):
        self.expression += str(char)
        self.display.delete(0, tk.END)
        self.display.insert(tk.END, self.expression)

    def clear(self):
        self.expression = ""
        self.display.delete(0, tk.END)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
            self.expression = result
        except Exception:
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, "Error")
            self.expression = ""

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()