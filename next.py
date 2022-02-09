import tkinter as tk
import random
# Variables
Range = 0
Prices = ["Monica's Grapple", "Mr K's Mask", "ClutterBot's Hand Cannon", "Willow's Spider Arms", "Mimi's BOW-II", "Dumb little Monica Plushie", "Artemis' Bandana", "VB Longneck", "Dollar Store Parc Blade", "50 Millionth K-tana"]
# Window
root = tk.Tk()
root.title("WoV Item Selector")
root.configure(bg="white")
root.geometry('600x200')
# Functions
def counter():
    global Range
    Range = len(Prices)
    select = random.randint(0,Range)
    result.configure(text=Prices[select])
    Prices.pop(select)
# Button
button = tk.Button(root)
button.configure(font=(20), text="WoV Item Selector", bg="red", command=counter)
button.pack(pady=10, anchor='center')
# Result
result = tk.Label(root, text="???", font=('consolas', 20), bg="gray")
result.pack(pady=40, anchor='center')

root.mainloop()
