import os, sys
import pygame
from Tkinter import *


cFile = 0

dirListing = os.listdir('/home/pi/Songs/')
files = []
for item in dirListing:
    if ".mp3" in item:
        files.append(item)
files.sort()

print ("-----------------------------------------------------")
for item in files [:4]:
    print (files.index(item) +1, item)

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(files[cFile])


def play():
    pygame.mixer.music.play()
    
def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def prev():
    global cFile
    cFile = cFile - 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(files[cFile])
    pygame.mixer.music.play()

    textBox.insert(END, "\n")
    textBox.insert(END, str(cFile) + ") ")
    textBox.insert(END, "<---" + files[cFile])

def next():
    global cFile
    cFile = cFile + 1
    pygame.mixer.music.stop()
    pygame.mixer.music.load(files[cFile])
    pygame.mixer.music.play()

    textBox.insert(END, "\n")
    textBox.insert(END, str(cFile) + ") ")
    textBox.insert(END, files[cFile])

def printPlaylist():
    print ("-------------")
    for item in files [:1000]:
        print (files.index(item) +1, item)

def test():
    pygame.mixer.music.load('/home/pi/Songs/ATC - Around The World(La La La La La).mp3')
    pygame.mixer.music.play()
    
    

main = Tk()
main.resizable(width=True, height=True)

yscrollbar = Scrollbar(main)
yscrollbar.pack(side=RIGHT, fill=Y)

textBox = Text(main, background = "black", foreground = "white", yscrollcommand=yscrollbar.set)
textBox.pack()

yscrollbar.config(command=textBox.yview)



bplay = Button(main, text="Play", command = play)
bplay.pack(side = LEFT)

bpause = Button(main, text="Pause", command = pause)
bpause.pack(side = LEFT)

bunpause = Button(main, text="Unpause", command = unpause)
bunpause.pack(side = LEFT)

bprev = Button(main, text="Previous", command = prev)
bprev.pack(side = LEFT)

bnext = Button(main, text="Next", command = next)
bnext.pack(side = LEFT)

bprint = Button(main, text="Print playlist to console", command = printPlaylist)
bprint.pack(side = RIGHT)

btest = Button(main, text="Test 1 song", command = test)
btest.pack(side = RIGHT)

main.maxsize(1000,1000);
main.minsize(800,500);
main.mainloop()
