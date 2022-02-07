import tkinter

Hello = tkinter.Tk()
# > Start Code
Hello.title("The Message.")
Hello.geometry('200x200')
Hello.configure(bg='black')
# > Box

box1 = tkinter.Label(
    Hello,
    text="Hello World!",
    bg="maroon",
    fg="black"
)

box1.pack(
    ipadx=50,
    ipady=70,
    expand=True
)
Hello.mainloop()