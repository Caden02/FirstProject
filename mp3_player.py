from tkinter import *
from pygame import mixer

# Learning how to create an Mp3 player using tkinter and pygame


root = Tk()  # Creating a Window

mixer.init()  # Initializing the Mixer

root.title('Melody')  # Giving the Window a Title

root.iconbitmap(r'melody_icon.ico')  # Changing the Icon of the Window

root.geometry('300x300')  # Setting the size of the Window


# Adding a Text Label
lab1 = Label(root, text='Lets make some noise!')
lab1.pack()


# Adding a Play Button Button and assigning a command to it
def play_music():
    """Loading the chosen music and playing it."""

    mixer.music.load('shattered_time.mp3')
    mixer.music.play()


playimg = PhotoImage(file='play.png')
playlab = Button(root, image=playimg, command=play_music)
playlab.pack()





root.mainloop()  # Starting the mainloop process
