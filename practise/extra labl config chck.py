import tkinter as tk


class Frontend:
    def __init__(self, master):
        self.master = master
        self.label_text = tk.StringVar()
        self.label = tk.Label(self.master, textvariable=self.label_text)
        self.label.pack()

    def set_label_text(self, text):
        self.label_text.set(text)


if __name__ == '__main__':
    root = tk.Tk()
    frontend = Frontend(root)
    frontend.set_label_text("Initial label text")
    root.mainloop()
