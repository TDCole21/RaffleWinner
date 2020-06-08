import csv
import random
import tkinter as tk 
from tkinter import *
from time import time, sleep

csvNames = []
with open('RaffleNames.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        csvNames.append(', '.join(row))
del(csvNames[0])

capNames = []
for x in csvNames:
    capNames.append(x.upper())

listNames = []
for x in capNames:
    y=x.split(",")
    listNames.append(y)

for x in range(len(listNames)):
    listNames[x][1] = str(listNames[x][1]) + " " + str(listNames[x][2])
    del(listNames[x][2])
    
finalNames = []
for x in range(len(listNames)):
    ents = int(listNames[x][0])
    name = str(listNames[x][1])
    for y in range(ents):
        finalNames.append(name)

pickNames = finalNames
winnersList = []


class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.remaining = 0
        self.title('Raffle Winners')
        w = Canvas(self, width=0, height=0)
        self.configure(bg='black')
        w.pack() 

        self.label = tk.Label(self, bg="black", fg="gold", pady=25, font='Helvetica 24 bold')
        self.label.pack()
        self.label.config(text="Welcome to the CR Raffle!") # starting message

        self.label2 = tk.Label(self, bg="black", fg="gold", pady=25, font='Helvetica 18 bold')
        self.label2.pack()
        self.label2.config(text="5 - £50 winners\n15 - £25 winners") # starting message

        self.frame = Frame(self)
        self.frame.pack()
        self.winnerbutton = Button(self.frame, text='Pick Winner', font='Helvetica 18 bold', activebackground="gold", fg='gold', bg="black", padx=25, pady=25, width=20, command=self.winners)
        self.winnerbutton.pack(side=LEFT) 
        self.quitbutton = Button(self.frame, text='Quit', font='Helvetica 18 bold', activebackground="red", fg='Red', bg="black", padx=25, pady=25, width=20, command=quit) 
        self.quitbutton.pack() 


    def winners(self): # Randomly selects a person from the raffle list, and moves them to the winners list
        if len(winnersList)<20:
            random.shuffle(pickNames)
            winnersList.append(pickNames[0])
            del(pickNames[0])
            self.countdown(len(pickNames))
            if len(winnersList)<6:
                self.label.config(text="CR Raffle - £50 Winners!")
            else:
                self.label.config(text="CR Raffle - £25 Winners!")
        else:
            self.label.config(text="Thank you for playing!")
            self.label2.config(text="Good Night")
            f = open("winners.csv", "w")
            for i in range(5):
                f.write("50,"+winnersList[i]+"\n")
            for i in range(5,len(winnersList)-1):
                f.write("25,"+winnersList[i]+"\n")
            f.write("25,"+winnersList[-1])
            f.close()

            # f = open("losers.csv", "w")
            # for i in range(len(pickNames)-1):
            #     f.write(pickNames[i]+"\n")
            # f.write(pickNames[-1])
            # f.close()

            # f = open("people.csv", "w")
            # for i in range(len(listNames)-1):
            #     f.write(listNames[i][1]+"\n")
            # f.write(listNames[-1][1])
            # f.close()


    def countdown(self, remaining = None):
        random.shuffle(listNames)
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            if len(winnersList)<6:
                self.label2.config(text=str(len(winnersList))+": "+str(winnersList[-1]))
            else:
                self.label2.config(text=str(len(winnersList)-5)+": "+str(winnersList[-1]))
        else:
            self.label2.configure(text=listNames[0][1])
            self.remaining = self.remaining - 1
            self.after(len(listNames)+50-self.remaining, self.countdown)


if __name__ == "__main__":
    root = ExampleApp()
    root.mainloop()
