import tkinter

bomb = tkinter.Tk()
selection = ["white", "Maroon", "Red", "Orange", "Yellow"]
select = 0
sizeX = 50
sizeY = 50
count = 5

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
print('5')
bomb.after(2000, updateWindow)
bomb.after(4000, updateWindow)
bomb.after(6000, updateWindow)
bomb.after(8000, updateWindow)
bomb.after(10000, end)

# End
bomb.mainloop()