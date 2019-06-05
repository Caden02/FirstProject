import tkinter as tk

win = tk.Tk()

win.geometry('220x350')

win.resizable(False, False)

win.title('First GUI')

lab1 = tk.Label(win, text='First Label')
lab1.pack()

lab2 = tk.Label(win, text='Second Label')
lab2.pack()


# Create the Number Buttons
numFrame1 = tk.Frame(win)
numFrame1.pack(side='left')

numFrame2 = tk.Frame(win)
numFrame2.pack(side='left')

numFrame3 = tk.Frame(win)
numFrame3.pack(side='left')

num7 = tk.Button(numFrame1, text='7')
num5 = tk.Button(numFrame1, text='5')
num1 = tk.Button(numFrame1, text='1')

num7.config(height = 5, width = 6)
num5.config(height = 5, width = 6)
num1.config(height = 5, width = 6)

num7.grid()
num5.grid()
num1.grid()

num8 = tk.Button(numFrame2, text='8')
num5 = tk.Button(numFrame2, text='5')
num2 = tk.Button(numFrame2, text='2')

num8.config(height = 5, width = 6)
num5.config(height = 5, width = 6)
num2.config(height = 5, width = 6)

num8.grid(column=1)
num5.grid(column=1)
num2.grid(column=1)

num9 = tk.Button(numFrame3, text='9')
num6 = tk.Button(numFrame3, text='6')
num3 = tk.Button(numFrame3, text='3')

num9.config(height = 5, width = 6)
num6.config(height = 5, width = 6)
num3.config(height = 5, width = 6)

num9.grid(column=2)
num6.grid(column=2)
num3.grid(column=2)


# Create the Operator Buttons
operFrame = tk.Frame(win)
operFrame.pack(side='left')


but1 = tk.Button(operFrame, text='C')
but2 = tk.Button(operFrame, text='+')
but3 = tk.Button(operFrame, text='-')
but5 = tk.Button(operFrame, text='=')

but1.config(height=4, width=7)
but2.config(height=3, width=7)
but3.config(height=3, width=7)
but5.config(height=5, width=7)

but1.grid(column=3)
but2.grid(column=3)
but3.grid(column=3)
but5.grid(column=3)


win.mainloop()








