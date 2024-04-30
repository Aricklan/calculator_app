import tkinter as tk

class Calculator: 
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculator")

        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.configure(bg="black")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    
    ###111