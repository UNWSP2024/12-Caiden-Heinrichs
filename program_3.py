#Week 12, Program 3 - Long-Distance Calls
#Caiden Heinrichs
#04/24/26

import tkinter
from tkinter import messagebox


class Gui():
    def __init__(self):
        #Create and set up the window
        self.window = tkinter.Tk()
        self.window.title('Long Distance Call Cost Calculator')
        self.window.minsize(500, 250)
        self.window.maxsize(500, 250)
        #Create frames
        self.leftFrame = tkinter.Frame(self.window, width = 250, height = 250)
        self.rightFrame = tkinter.Frame(self.window, width = 250, height = 250)

        #Create instructional text for inputs
        self.entryBoxInstruction = tkinter.Label(self.leftFrame, text = 'Enter the length of the call (minutes):')
        self.radioButtonInstruction = tkinter.Label(self.leftFrame, text = 'Select the correct time frame for the call:')
        #Create variables to store input
        self.costPerMinute = tkinter.DoubleVar()
        self.callLength = tkinter.DoubleVar()
        #Create radio buttons and the entry box
        self.daytimeButton = tkinter.Radiobutton(self.leftFrame, text = 'Daytime (6:00 A.M. through 5:59 P.M.)', variable = self.costPerMinute, value = 0.02)
        self.eveningButton = tkinter.Radiobutton(self.leftFrame, text = 'Evening (6:00 P.M.  through 11:59 P.M.)', variable = self.costPerMinute, value = 0.12)
        self.nightButton = tkinter.Radiobutton(self.leftFrame, text = 'Night (midnight through 5:59 P.M.)', variable = self.costPerMinute, value = 0.05)
        self.entryBox = tkinter.Entry(self.leftFrame, textvariable = self.callLength)
        #Create calculate and quit buttons
        self.calculateButton = tkinter.Button(self.rightFrame, text = 'Calculate Cost', command = self.displayCost)
        self.quitButton = tkinter.Button(self.rightFrame, text = 'Quit', command = self.window.destroy)
        #Pack all frames, labels, entries, radio buttons, and buttons
        self.leftFrame.pack(side = 'left')
        self.rightFrame.pack(side = 'left')
        self.entryBoxInstruction.pack(side = 'top')
        self.entryBox.pack(side = 'top')
        self.radioButtonInstruction.pack(side = 'top')
        self.daytimeButton.pack(side = 'top')
        self.eveningButton.pack(side = 'top')
        self.nightButton.pack(side = 'top')
        self.calculateButton.pack(side = 'top')
        self.quitButton.pack(side = 'top')

    #Calculate the total cost of the call and display
    def displayCost(self):
        totalCost = self.costPerMinute.get() * self.callLength.get()
        totalCost = format(round(totalCost, 2), '.2f')
        messagebox.showinfo('Final cost', f'The call will cost ${totalCost}.')


if __name__ == '__main__':
    Gui()
    tkinter.mainloop()
