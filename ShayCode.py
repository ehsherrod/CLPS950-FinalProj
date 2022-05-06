# importing necessary packages
from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd
import random

# creating window
win = visual.Window([1400,900], color='black', fullscr=0)
mymouse = event.Mouse(visible=True, win=win)

# instructions page
ready_text = visual.TextStim(win, text='Color Sorting Game')
# drawing draws "behind the screen"
ready_text.draw()
# flipping the window is how to show things - you can get whatever ready you want in the background in the mean time
win.flip()
event.waitKeys(maxWait=3, keyList=['1', '2'], clearEvents=True,)
win.flip()

# creating color order for boxes
correct_color_order = ['#E85440', '#EC743C', '#F3953F', '#F4B63D', '#FAD440']
shuffled_colors = correct_color_order.copy()
random.shuffle(shuffled_colors)

tiles = []
for i in range(len(correct_color_order)):
    newtile = visual.Rect(win,pos=((-.5+(i*.2)),.5),fillColor=shuffled_colors[i],width=.2,height=.2,fillColorSpace='hex')
    print(newtile.fillColor)
    tiles.append(newtile)
for t in tiles:
    t.draw()

init_colors = ['#000000', '#000000', '#000000', '#000000', '#000000']

puzzlekey = []
for i in range(len(init_colors)):
    newkey = visual.Rect(win,pos=((-.5+(i*.2)),0),fillColor=init_colors[i],width=.2,height=.2,fillColorSpace='hex')
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
