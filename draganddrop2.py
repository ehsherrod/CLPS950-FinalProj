# Code for dragging individual shapes
from tkinter import * # import this package
def drag_start(event): # drag function
    widget = event.widget
    widget.startX = event.x #this is where we click within the widget. i.e the coordinates where we click inside the lable
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x #defines the new coordinates of where you want to drag the shape
    # widget.winfo_x(): this defines the top left corner of shape relative to the window
    # widget.startX: place where you click within the lable
    y = widget.winfo_y() - widget.startY + event.y #position of second shape
    widget.place(x=x,y=y) # the new x and y coordinates after you've moved it

window = Tk()# This is the window where all the shapes will be displayed

label = Label(window,bg="#EED938",width=10,height=15)
# label = Label(window,... :creating the image in the window
# bg="red"... :defining the colour of the shape
# width=10,height=5... :size of widget  of the
label.place(x=0,y=0) # position of shape on window at position (x,y))

label2 = Label(window,bg="#FAD440",width=10,height=15)
label2.place(x=50,y=50)

label3 = Label(window, bg='#F4B63D', width=10, height = 15)
label3.place(x=100,y=100)

label4 = Label(window, bg='#F3953F', width=10, height = 15)
label4.place(x=150,y=150)

label5 = Label(window, bg='#EC743C', width=10, height = 15)
label5.place(x=200,y=200)

label6 = Label(window, bg='#E85440', width=10, height = 15)
label6.place(x=250,y=250)

label.bind("<Button-1>",drag_start)# calls the drag start function.
# allows you to click on shape on screen.
label.bind("<B1-Motion>",drag_motion) # calls the drag motion function

label2.bind("<Button-1>",drag_start)
label2.bind("<B1-Motion>",drag_motion)

label3.bind("<Button-1>",drag_start)
label3.bind("<B1-Motion>",drag_motion)

label4.bind("<Button-1>",drag_start)
label4.bind("<B1-Motion>",drag_motion)

label5.bind("<Button-1>",drag_start)
label5.bind("<B1-Motion>",drag_motion)

label6.bind("<Button-1>",drag_start)
label6.bind("<B1-Motion>",drag_motion)

window.mainloop()
