from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import random

win = visual.Window([1400,900], color='black', fullscr=0)
mymouse = event.Mouse(visible=True, win=win)

# basic text
ready_text = visual.TextStim(win, text='hello world!')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True,)
win.flip()


# correct_color_order = ['red','orange','yellow','green']
correct_color_order = [(238,217,56),(250,212,64),(244,182,61)]
shuffled_colors = correct_color_order.copy()
random.shuffle(shuffled_colors)

tiles = []
for i in range(len(correct_color_order)):
    newtile = visual.Rect(win,pos=((-.5+(i*.2)),.5),fillColor=shuffled_colors[i],width=.2,height=.2,fillColorSpace='rgb255')
    print(newtile.fillColor)
    tiles.append(newtile)
for t in tiles:
    t.draw()



init_colors = [(0,0,0),(0,0,0),(0,0,0)]

puzzlekey = []
for i in range(len(init_colors)):
    newkey = visual.Rect(win,pos=((-.5+(i*.2)),0),fillColor=init_colors[i],width=.2,height=.2,fillColorSpace='rgb255')
    puzzlekey.append(newkey)
for pk in puzzlekey:
    pk.draw()

done_button = visual.Rect(win,pos=(0,-.5),fillColor='white',width=.2,height=.2)
done_button.draw()


win.flip()

clicked_done = False
while not clicked_done:
    if mymouse.isPressedIn(done_button):
        clicked_done = True
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
