from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import random

win = visual.Window([1400,900], color='white', fullscr=0)
mymouse = event.Mouse(visible=True, win=win)

Introtxt = visual.TextStim(win, text='CLPS950 Final Project', font='Times', units='pix', pos=(0,100), height=65, color="#000000")
subIntrotxt = visual.TextStim(win, text='by Shay, Monica, and Eden', font='Times', units='pix', pos=(0,-100), height=45, color="#000000")
subsubIntrotxt = visual.TextStim(win, text='press space bar to continue', font='Times', units='pix', pos=(0,-165), height=30, color="#000000")
Introtxt.draw()
subIntrotxt.draw()
subsubIntrotxt.draw()

win.flip()
event.waitKeys(maxWait=10, keyList=['space'], clearEvents=True,)
win.flip()


correct_color_order = ["#EED938","#FAD440", "#F4B63D", "#F3953F", "#EC743C", "#E85440"]
shuffled_colors = correct_color_order.copy()
random.shuffle(shuffled_colors)

tiles = []
for i in range(len(correct_color_order)):
    newtile = visual.Rect(win,pos=((-.5+(i*.2)),.5),fillColor=shuffled_colors[i],width=.2,height=.2,fillColorSpace='hex')
    print(newtile.fillColor)
    tiles.append(newtile)
for t in tiles:
    t.draw()



init_colors = ["#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF","#FFFFFF"]

puzzlekey = []
for i in range(len(init_colors)):
    newkey = visual.Rect(win,pos=((-.5+(i*.2)),0),lineWidth=1, lineColor='black',fillColor=init_colors[i], width=.2,height=.2,fillColorSpace='hex')
    puzzlekey.append(newkey)
for pk in puzzlekey:
    pk.draw()

check_button = visual.Rect(win,pos=(0,-.5),fillColor='black',width=.2,height=.2)
check_buttontext = visual.TextStim(win, text='Check', font='Times',pos=(0,-.5), height=.08, color='white')
check_button.draw()
check_buttontext.draw()


win.flip()

clicked_check = False
while not clicked_check:
    if mymouse.isPressedIn(check_button):
        clicked_check = True
    # update , drag, colors, etc


win.flip()

total_correct = 0
for i in range(len(puzzlekey)):
    puzzletile = puzzlekey[i]
    correct_color = correct_color_order[i]
    is_correct = puzzletile.fillColor == correct_color
    is_correct = sum(is_correct)
    if is_correct==3:
        total_correct += 1





result = visual.TextStim(win,text='you got '+str(total_correct)+' correct!')
result.draw()
win.flip()
event.waitKeys(maxWait=3, keyList=['space'], clearEvents=True,)







core.quit()
