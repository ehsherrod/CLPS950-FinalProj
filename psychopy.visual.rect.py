# Making rectangles

# Import packages first
import numpy as np
import psychopy
import psychopy.visual
import psychopy.event

# create initial window
win = psychopy.visual.Window(
    size = [800,600],
    units = 'pix',
    fullscr = False,
    color = [1,1,1]
)

# now set parameters for the rectangle
rect = psychopy.visual.Rect(win=win, units='pix')
n_rect = 5
rect_colors_1 = ['#E85440', '#EC743C', '#F3953F', '#F4B63D', '#FAD440']

# for loop to draw each rectangle
for ii in range(n_rect):
    rect.width = 50
    rect.height = 100
    rect.fillColor = rect_colors_1[ii]
    rect.pos = [-100+(50*ii), 0]
    rect.draw()

win.flip()
psychopy.event.waitKeys()
win.close()
