from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer
import sys
import os
from mutagen.mp3 import MP3

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

rew = resource_path('rewind.png')

mute = resource_path('mute.png')

unmute = resource_path('unmute.png')


root = Tk()

mixer.init()  # Initializing the Mixer

mus_play = 0  # Initializing the play music functions

muted = False  # Initializing the Mute functions

root.title('Melody')

root.iconbitmap(micon)  # Changing the Icon of the Window


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
                        'Stop Button: Stops and Resets Music.\n'
                        'Pause Button: Pauses Currently Playing Music.\n'
                        'Rewind Button: Rewinds Music back to the Beginning.\n')

lab1.pack(pady=10)


# Creating a function to show the details and duration of the currently playing song in a text label
def show_details():
    """For .wav and .mp3 files. This function gets the total duration of
     the chosen song, formats it, and then displays it.
     """

    file_data = os.path.splitext(filename)

    if file_data[1] == '.mp3':
        filelab['text'] = f'Playing - {base_name}'
        audio = MP3(filename)
        total_length = audio.info.length

    else:
        filelab['text'] = f'Playing - {base_name}'
        a = mixer.Sound(filename)
        total_length = a.get_length()

    mins, secs, = divmod(total_length, 60)  # div: mins == total_length/60, mod: secs == total_length % 60
    mins = round(mins)
    secs = round(secs)

    time_format = '{:02d}:{:02d}'.format(mins, secs)
    lenlab['text'] = f'Total Duration : {time_format}'


filelab = Label(root, text='Select a song and press play.')
filelab.pack()

lenlab = Label(root, text='Total Duration : --:--')
lenlab.pack()


# Creating a Frame for the three media control buttons: play, stop, and pause
midbtn_frame = Frame(root)
midbtn_frame.pack(padx=30, pady=30)


# Creating the bottom frame which currently houses the rewindbtn and volumesld
bottom_frame = Frame(root)
bottom_frame.pack(pady=10)


# Adding a Play Button and assigning a Play command to it
def play_music():
    """Loading the chosen music and playing/resuming it, but throwing an error if no music has been chosen."""

    try:
        if mus_play == 1:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text'] = f'Playing song: {base_name}'
            show_details()

        elif mus_play == 2:
            mixer.music.unpause()
            statusbar['text'] = f'Playing song: {base_name}'

        elif mus_play == 0:
            raise Exception
    except Exception:
        tkinter.messagebox.showerror('Play Error', 'Please choose a song first by clicking on '
                                                   'sub menu "file" < "open".')


playimg = PhotoImage(file=ply)
playbtn = Button(midbtn_frame, image=playimg, command=play_music)
playbtn.grid(row=0, column=0, padx=10)


# Adding a Stop Button and assigning a Stop command to it
def stop_music():
    """Stops the currently playing music and restarts it from the beginning."""
    global mus_play
    mus_play = 1
    mixer.music.stop()
    statusbar['text'] = 'Music stopped'


stopimg = PhotoImage(file=stp)
stopbtn = Button(midbtn_frame, image=stopimg, command=stop_music)
stopbtn.grid(row=0, column=1, padx=10)


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
pausebtn = Button(midbtn_frame, image=pauseimg, command=pause_music)
pausebtn.grid(row=0, column=2, padx=10)


# Adding a Volume control slider
def set_vol(val):
    """Enabling the volume slider by taking input
        from the slider, storing it into parameter 'val'
        and converting it into type integer, then
        dividing that input by 100.
        """


    volume = int(val) / 100  # Input must be divided by 100 since set_volume func only takes args ranging from 0 to 1
    mixer.music.set_volume(volume)


volumesld = Scale(bottom_frame, from_=0, to=100, orient='horizontal', command=set_vol)
volumesld.set(50)
mixer.music.set_volume(0.5)
volumesld.grid(row=0, column=2, padx=30)


# Creating a Rewind button and assigning its respective function
def rewind():
    mixer.music.play()


rewindpho = PhotoImage(file=rew)
rewindbtn = Button(bottom_frame, image=rewindpho, command=rewind)
rewindbtn.grid(row=0, column=0, pady=5)


# Creating a Mute button and assigning its respective function
def mute_music():
    """Using the global var 'muted', this function will mute the music if 'muted' == False, and vice-versa."""

    global muted

    if muted:  # Unmute the music
        mixer.music.set_volume(.5)
        unmutebtn.configure(image=unmutepho)
        volumesld.set(50)
        muted = False

    else:  # Mute the music
        mixer.music.set_volume(0)
        unmutebtn.configure(image=mutepho)
        volumesld.set(0)
        muted = True

mutepho = PhotoImage(file=mute)
unmutepho = PhotoImage(file=unmute)
unmutebtn = Button(bottom_frame, image=unmutepho, command=mute_music)
unmutebtn.grid(row=0, column=1)


# Creating a Status Bar
statusbar = Label(root, text='Welcome to Melody', relief='sunken', anchor='w')
statusbar.pack(side='bottom', fill='x')


root.mainloop()  # Start the mainloop process
