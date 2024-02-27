#Python Guess The Number GUI Game
from tkinter import *
import random

attempts = 5
answer = random.randint(1,20)
def check():
    global attempts
    global text
    attempts -= 1
    guess = int(entry.get())

    if answer == guess:
        text.set("Congratulations! You guessed correct!")
        checkbutton.pack_forget()
    elif attempts == 0:
        text.set("You dont have attempts left, Game over!!")
        checkbutton.pack_forget()
    elif guess < answer:
        text.set("You have"+  str(attempts) +"remaining-Go Higher")
    elif guess > answer:
        text.set("You have"+ str(attempts) +"remaining-Go Lower")
    return

screen = Tk()
screen.title("Guess The Number Game(GUI edition!)")
screen.configure(bg= "black")

label = Label(screen, text = "Guess the nmber between 1 till 20", bg= "light grey")
label.pack()

entry= Entry(screen, width=40 , borderwidth= 4)
entry.pack()

quitbutton = Button(screen, text="Quit", command= screen.quit, bg= "light grey")
quitbutton.pack()
checkbutton = Button(screen, text= "Check", command= check, bg= "light grey")
checkbutton.pack()
    
text = StringVar()
text.set("(You have only 5 attempts to guess the number, GOOD LUCK!)")

guessattempts = Label(screen, textvariable=text, bg= "light grey")
guessattempts.pack()

screen.mainloop()