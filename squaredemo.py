from psychopy import visual, monitors
from psychopy.visual import Window
from psychopy import core, event
import csv
import numpy as np
import pandas as pd

win = win = visual.Window([1440,900], color='black', fullscr=0)

square1 = visual.Rect(win, units='pix', pos=(200,200), fillColor=(238,217,56), lineColor=(238,217,56), width=100, height=100, fillColorSpace='rgb255', lineColorSpace='rgb255')

square1.draw()
win.flip()
core.wait(5)

win.close()
