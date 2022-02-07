import tkinter as tk
import time

clock = tk.Tk()
clock.title("The time is...")

def TheTime():
    TheClock = time.strftime('%H:%M:%S %p')
    timer.configure(text=TheClock)
    timer.after(1000, TheTime)

timer = tk.Label(clock, font=('consolas', 80), bg='black', fg='red')
timer.pack(anchor='center')
TheTime()

clock.mainloop()