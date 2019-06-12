from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
import sys
import os

# Learning how to create an Mp3 player using Tkinter and Pygame


# Retrieving and Assigning the absolute paths of files to their respective variables
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """

    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


micon = resource_path('melody_icon.ico')

ply = resource_path('play.png')

stp = resource_path('stop.png')

pas = resource_path('pause.png')


root = Tk()  # Creating a Window

mixer.init()  # Initializing the Mixer

mus_play = 0  # Initializing the play music functions

root.title('Melody')  # Giving the Window a Title

root.iconbitmap(micon)  # Changing the Icon of the Window

root.geometry('350x350')  # Setting the size of the Window


# Creating the MenuBar
menubar = Menu(root)
root.config(menu=menubar)


# Building the SubMenus
sub_file = Menu(menubar, tearoff=0)  # Creating the submenu 'file'

def browse_file():
    """A function to allow the cascade menu 'Open' to open and browse file explorer,
        while also retrieving the base name of the chosen song."""

    global filename
    global base_name
    global mus_play
    filename = filedialog.askopenfilename(title='Choose a song')
    base = os.path.basename(filename)
    base_name = os.path.splitext(base)[0]
    mus_play = 1
    mixer.music.pause()
    statusbar['text'] = f'Press Play to start {base_name}'

menubar.add_cascade(label='File', menu=sub_file)
sub_file.add_command(label='Open', command=browse_file)
sub_file.add_command(label='Exit', command=root.destroy)


sub_help = Menu(menubar, tearoff=0)  # Creating the submenu 'help'

def about():
    """Creating the pop-up information window for the cascade menu 'Help'."""

    tkinter.messagebox.showinfo('About this program', 'This Mp3 player was created to develop '
                                                      'a solid knowledge of GUI applications and programming.')


menubar.add_cascade(label='Help', menu=sub_help)
sub_help.add_command(label='About this program', command=about)


# Adding a Text Label
lab1 = Label(root, text='Play Button: Plays and Resumes Paused Music.\n'
                        'Stop Button: Stops and Restarts Music.\n'
                        'Pause Button: Pauses Currently Playing Music.')
lab1.pack()


# Adding a Play Button and assigning a Play command to it
def play_music():
    """Loading the chosen music and playing/resuming it, but throwing an error if no music has been chosen."""

    try:
        if mus_play == 1:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = f'Playing song: {base_name}'

        elif mus_play == 2:
            mixer.music.unpause()
            statusbar['text'] = f'Playing song: {base_name}'

        elif mus_play == 0:
            raise Exception
    except Exception:
        tkinter.messagebox.showerror('Play Error', 'Please choose a song first by clicking on '
                                                   'sub menu "file" < "open".')




playimg = PhotoImage(file=ply)
playbtn = Button(root, image=playimg, command=play_music)
playbtn.pack()


# Adding a Stop Button and assigning a Stop command to it
def stop_music():
    """Stops the currently playing music and restarts it from the beginning."""
    global mus_play
    mus_play = 1
    mixer.music.stop()
    statusbar['text'] = 'Music stopped'

stopimg = PhotoImage(file=stp)
stopbtn = Button(root, image=stopimg, command=stop_music)
stopbtn.pack()


# Adding a Pause button and assigning a Pause function to it
def pause_music():
    """Pause the currently playing music and create a global
        variable to be used by play func when music is paused.
        """
    global mus_play
    mus_play = 2
    mixer.music.pause()
    statusbar['text'] = 'Music paused'


pauseimg = PhotoImage(file=pas)
pausebtn = Button(root, image=pauseimg, command=pause_music)
pausebtn.pack()


# Adding a Volume control slider
def set_vol(val):
    """Enabling the volume slider by taking input
        from the slider, storing it into parameter 'val'
        and converting it into type integer, then
        dividing that input by 100.
        """

    volume = int(val) / 100  # Input must be divided by 100 since set_volume func only takes args ranging from 0 to 1
    mixer.music.set_volume(volume)


volumesld = Scale(root, from_=0, to=100, orient='horizontal', command=set_vol)
volumesld.set(50)
mixer.music.set_volume(0.5)
volumesld.pack()


# Creating a Status Bar
statusbar = Label(root, text='Welcome to Melody', relief='sunken', anchor='w')
statusbar.pack(side='bottom', fill='x')


root.mainloop()  # Start the mainloop process
