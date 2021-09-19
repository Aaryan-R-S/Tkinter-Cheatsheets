import tkinter

window = tkinter.Tk()
window.title("Test")

top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side="bottom")
# label = tkinter.Label(window, text="Hello, world!").pack()

btn1 = tkinter.Button(top_frame, text="B1", fg="red").pack()
btn2 = tkinter.Button(top_frame, text="B2", fg="green").pack()
btn3 = tkinter.Button(bottom_frame, text="B3", fg="purple").pack(side="left")
btn4 = tkinter.Button(bottom_frame, text="B4", fg="orange").pack(side="left")

window.mainloop()
