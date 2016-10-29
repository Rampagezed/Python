import os, sys
import pygame
from Tkinter import *


cFile = 0

dirListing = os.listdir('/home/pi/test/')
files = []
for item in dirListing:
    if ".mp3" in item:
        files.append(item)


pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(files[cFile])


print ("-------------")
for item in files [:4]:
   print (item)


def play():
    pygame.mixer.music.play()
    

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()


def next():
    global cFile
    cFile = cFile + 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(files[cFile])
    pygame.mixer.music.play()

    textBox.insert(END, "\n")
    textBox.insert(END, files[cFile])

main = Tk()
main.resizable(width=True, height=True)

textBox = Text(main, background = "black", foreground = "white")

textBox.pack()

bplay = Button(main, text="Play", command = play)
bplay.pack(side = LEFT)

bpause = Button(main, text="Pause", command = pause)
bpause.pack(side = LEFT)

bunpause = Button(main, text="Unpause", command = unpause)
bunpause.pack(side = LEFT)

bnext = Button(main, text="Next", command = next)
bnext.pack(side = LEFT)

main.maxsize(1000,1000);
main.minsize(800,500);
main.mainloop()





