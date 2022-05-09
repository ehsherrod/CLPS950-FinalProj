from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import random

win = visual.Window([1400,900], color='white', fullscr=0)
mymouse = event.Mouse(visible=True, win=win)

# basic text
ready_text = visual.TextStim(win, text='hello world!', color='black')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True,)
win.flip()


correct_color_order = ["#EED938","#FAD440", "#F4B63D"]
shuffled_colors = correct_color_order.copy()
random.shuffle(shuffled_colors)

tiles = []
for i in range(len(correct_color_order)):
    newtile = visual.Rect(win,pos=((-.5+(i*.2)),.5),fillColor=shuffled_colors[i],width=.2,height=.2,fillColorSpace='hex')
    print(newtile.fillColor)
    tiles.append(newtile)
for t in tiles:
    t.draw()



init_colors = ["#FFFFFF","#FFFFFF","#FFFFFF"]

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
