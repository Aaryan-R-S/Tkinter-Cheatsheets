import tkinter

window = tkinter.Tk()
window.title("Form")

tkinter.Label(window, text="Username").grid(row=0)
tkinter.Entry(window).grid(row=0, column=1)

tkinter.Label(window, text="Password").grid(row=1)
tkinter.Entry(window).grid(row=1, column=1)

tkinter.Checkbutton(window, text="Keep me loggeg In").grid(columnspan=2)


def say_hi():
    tkinter.Label(window, text="Done").grid(row=3, column=0, columnspan=2)

tkinter.Button(window, text="Do?", command=say_hi).grid(row=3, column=0, columnspan=2)


window.mainloop()