import random
from ttkthemes import ThemedTk
import ttkthemes
from tkinter import END
from tkinter import*
window=ThemedTk(theme="ubuntu")
window.geometry('800x600')
window.title("ColorGame")
colors=[("Red"), ("Pink"), ("Yellow"), ("Blue"), ("Green"), ("Purple"), ("Black"), ("White"), ("Orange"), ("Brown"), ("Grey"), ("Maroon"), ("Cyan")]
score=0
timeleft=30
def startGame(event):
    if timeleft==30:
        countdown()
    nextColor()
def countdown():
    global timeleft
    if timeleft>0:
        timeleft-=1
        lbl2.config(text="Time left:" + str(timeleft))
        lbl2.after(1000,countdown)
def nextColor():
    global score
    global timeleft
    if timeleft>0:
        lbl3.config(fg=str(colors[1]), text=str(colors[0]))
        if txt.get().lower()==colors[1].lower():
            score+=1
            lbl1.config(text="Score:"+ str(score))
            txt.delete(0,END)
            random.shuffle(colors)
            lbl3.config(fg=str(colors[1]), text=str(colors[0]))
lbl=Label(window,text="Type in the color of the words but not the text")
lbl.place(x=250,y=10)
lbl1=Label(window,text="Press Enter to start")
lbl1.place(x=350,y=50)
lbl2=Label(window,text="Time left:30")
lbl2.place(x=360,y=90)
lbl3=Label(window,text="Red",font=("Helvetica",100))
lbl3.place(x=270,y=110)
txt=Entry(window)
txt.place(x=340,y=270)
window.bind('<Return>',startGame)
window.mainloop()