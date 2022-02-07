import tkinter

bomb = tkinter.Tk()
selection = ["White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow", "White", "Maroon", "Red", "Orange", "Yellow"]
select = 0
sizeX = 50
sizeY = 50
count = 20
Time = 0

# Code
def updateWindow():
    global sizeX
    global sizeY
    global select
    global count

    sizeX = sizeX + 50
    sizeY = sizeY + 50
    select = select + 1
    bomb.geometry(str(sizeX)+'x'+str(sizeY))
    bomb.configure(bg=selection[select])
    count = count - 1
    print(count)

def end():
    bomb.destroy()
    print("Kaboom!!")

bomb.title("Bomb Threat!")
bomb.geometry('50x50')
bomb.configure(bg='white')
print(count)
for lole in range(0, count):
    Time = Time + 2000
    bomb.after(Time, updateWindow)
bomb.after(Time, end)


# End
bomb.mainloop()

print("lole")