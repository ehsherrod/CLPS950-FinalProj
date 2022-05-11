from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import random

def movePicked(picked, mouse, grabbed):
    # Move piece if we already moving that piece

    if grabbed is not None and mouse.isPressedIn(grabbed): # if the shape has been clicked AND the mouse clicked happened within the shape
        grabbed.pos = mouse.getPos() #position of the mouse is the position of the shape
        return grabbed # keep this
    else:
        # Move newly clicked piece
        for piece in picked: # for each shape that is clicked...
            if mouse.isPressedIn(piece) and grabbed is None: #if the mouse is in the piece that is clicked
                return piece

win = visual.Window([1400,900], color='white', units='pix',fullscr=0)
mouse = event.Mouse(visible=True, win=win)

Introtxt = visual.TextStim(win, text='CLPS950 Final Project', font='Times', units='pix', pos=(0,100), height=65, color="#000000")
subIntrotxt = visual.TextStim(win, text='by Shay, Monica, and Eden', font='Times', units='pix', pos=(0,-100), height=45, color="#000000")
subsubIntrotxt = visual.TextStim(win, text='press space bar to continue', font='Times', units='pix', pos=(0,-165), height=30, color="#000000")
Introtxt.draw()
subIntrotxt.draw()
subsubIntrotxt.draw()

win.flip()
event.waitKeys(maxWait=10, keyList=['space'], clearEvents=True,)
win.flip()

correct_color_order = ["#FBD83C","#F7B63A","#F5A73D","#F1843E","#EA643E"]
#correct_color_order_2 = ["#93DF8A","#6DC47B","#54A979","#3E8D76","#2B7271"]
#correct_color_order_3 = ["#71AFE5","#2B88D8","#0078D4","#106EBE","#005A9E"]
#correct_color_order_4 = ["#E2619F","#E44B8D","#D24787","#BB437E","#A53E76"]

shuffled_colors = correct_color_order.copy()
random.shuffle(shuffled_colors)

tiles = []
for i in range(len(correct_color_order)):
    newtile = visual.Rect(win,units='pix',pos=((-280+(i*140)),150),fillColor=shuffled_colors[i],width=140,height=90,fillColorSpace='hex')
    print(newtile.fillColor)
    tiles.append(newtile)
for t in tiles:
    t.draw()

puzzlekey = []
for i in range(5):
    newkey = visual.Rect(win,units='pix',pos=((-280+(i*140)),0),lineWidth=1, lineColor="#000000", width=140,height=90,fillColorSpace='hex')
    puzzlekey.append(newkey)
for pk in puzzlekey:
    pk.draw()

referent1 = visual.Rect(win, units='pix', pos=(-420, 0),lineWidth=1, lineColor="#000000",fillColor="#EED938", width=140,height=90,fillColorSpace='hex')
referent2 = visual.Rect(win, units='pix', pos=(420, 0),lineWidth=1, lineColor="#000000",fillColor="#E85440", width=140,height=90,fillColorSpace='hex')
referent1.draw()
referent2.draw()

check_button = visual.Rect(win,units='pix',pos=(0,-150),fillColor='black',width=140,height=90)
check_buttontext = visual.TextStim(win, units='pix', text='Check', font='Times',pos=(0,-150), height=40, color='white')
check_button.draw()
check_buttontext.draw()

pieces = tiles #define the draggable pieces
picked = [] # initially, no shape has been clicked. This defines the draggable piece
movingPiece = None # there is no piece being dragged

clicked_check = False
while not clicked_check:
    win.flip()# Window will keep flipping for the duration of the timer. Because evertime something moves on the window, the window must be flipped.
    if mouse.isPressedIn(check_button):
        clicked_check = True
    for piece in pieces: #for each shape
        if mouse.isPressedIn(piece) and movingPiece is None: # If the shape is clicked AND it's not moving
            picked.append(piece) # define it as a picked. So now piece is picked
    movingPiece = movePicked(picked, mouse, movingPiece) # move the picked piece
    for pk in puzzlekey:# want to keep drawing the puzzel keys so that it displays up until the check button is clicked
        pk.draw()
    for p in pieces:
        p.draw() #keep drawing the shape in their new position shape.
    referent1.draw()
    referent2.draw()
    check_button.draw()
    check_buttontext.draw()

win.flip()

total_correct = 0
for i in range(len(puzzlekey)):
    puzzletile = puzzlekey[i]
    correct_color = correct_color_order[i]
    is_correct = puzzletile.fillColor == correct_color
    if is_correct:
        total_correct += 1

result = visual.TextStim(win,text='you got '+str(total_correct)+' correct!')
result.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True,)

core.quit()
