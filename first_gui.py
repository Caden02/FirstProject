import tkinter as tk

win = tk.Tk()

win.geometry('250x450')

win.title('First GUI')

lab1 = tk.Label(win, text='First Label')
lab1.pack()

lab2 = tk.Label(win, text='Second Label')
lab2.pack()

operFrame = tk.Frame(win)
operFrame.pack(side='right')

# Create the Operator Buttons
but1 = tk.Button(operFrame, text='C').pack()
but2 = tk.Button(operFrame, text='+').pack()
but3 = tk.Button(operFrame, text='-').pack()
but4 = tk.Button(operFrame, text='=').pack()

# Create the Number Buttons
numFrame1 = tk.Frame(win)
numFrame1.pack(side='left')

numFrame2 = tk.Frame(win)
numFrame2.pack(side='bottom')

numFrame3 = tk.Frame(win)
numFrame3.pack(side='right')

num7 = tk.Button(numFrame1, text='7')
num4 = tk.Button(numFrame1, text='4')
num1 = tk.Button(numFrame1, text='1')

num7.config(height = 4, width = 4)
num4.config(height = 4, width = 4)
num1.config(height = 4, width = 4)

num7.pack()
num4.pack()
num1.pack()

num8 = tk.Button(numFrame2, text='8')
num5 = tk.Button(numFrame2, text='5')
num2 = tk.Button(numFrame2, text='2')

num8.config(height = 4, width = 4)
num5.config(height = 4, width = 4)
num2.config(height = 4, width = 4)

num8.pack()
num5.pack()
num2.pack()

num9 = tk.Button(numFrame3, text='9')
num6 = tk.Button(numFrame3, text='6')
num3 = tk.Button(numFrame3, text='3')

num9.config(height = 4, width = 4)
num6.config(height = 4, width = 4)
num3.config(height = 4, width = 4)

num9.pack()
num6.pack()
num3.pack()


win.mainloop()








