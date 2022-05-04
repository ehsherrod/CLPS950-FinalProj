from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd

# window and pixels. if you make one that isn't the right size, it will tell you in warnings in the terminal
full_scr = input('full screen? 1 (yes) or 0 (no)')
if full_scr:
	# 1440 x 900 is size of my mac
	win = win = visual.Window([1440,900], color='black', fullscr=0)
else:
	win = visual.Window([600,400], color='black', fullscr=0)

square1 = visual.Rect(win, units='pix', lineWidth=None, pos=(200,200), fillColor=(238,217,56), width=100, height=100, fillColorSpace='rgb')

square1.draw()
win.flip()
core.wait(5)

win.close()
