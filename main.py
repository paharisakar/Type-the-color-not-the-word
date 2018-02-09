import tkinter
import random
colors = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White']
score=0
timeleft=10
def startGame(event):


    if timeleft == 10:
        countdown()
    nextColor()
    if timeleft == 0:
        gameend()

def nextColor():

    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1
        e.delete(0, tkinter.END)
        random.shuffle(colors)
        label.config(fg=str(colors[1]), text=str(colors[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)

def gameend():
    final_score  = tkinter.Label(root, text="Your final score is: "+str(score), font=('Helvetica', 17))
    final_score.pack()

root = tkinter.Tk()

root.title("Sakar's Game")

root.geometry("500x230")

head = tkinter.Label(root, text="Welcome to Sakar's game. Instructions are as follow.", font=('Helvetica', 17))
head.pack()

instructions = tkinter.Label(root, text="Type in the color of the words, and not the word text!", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()



timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()


label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()


root.mainloop()
