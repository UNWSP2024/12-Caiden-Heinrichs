#Week 12, Program 1 - MPG Calculator
#Caiden Heinrichs
#04/24/26

import tkinter


class Gui:
    def __init__(self):
        #Create and set up the window
        self.window = tkinter.Tk()
        self.window.title('MPG Calculator')
        self.window.minsize(500, 250)
        self.window.maxsize(500, 250)

        #Make frames for the window
        self.frameBottom = tkinter.Frame(self.window, width = 400, height = 50, padx = 25, pady = 25)
        self.frameTopLeft = tkinter.Frame(self.window, width = 175, height = 50, padx = 25, pady = 25)
        self.frameTopRight = tkinter.Frame(self.window, width = 175, height = 50, padx = 25, pady = 25)
        #Create text and entry box for the car's capacity
        self.capacityInt = tkinter.IntVar()
        self.capacityLabel = tkinter.Label(self.frameTopLeft, text = 'How many gallons of gas can your car hold?')
        self.capacityEntry = tkinter.Entry(self.frameTopLeft, textvariable = self.capacityInt)
        #Create text and entry box for the car's range on a full tank
        self.rangeInt = tkinter.IntVar()
        self.rangeLabel = tkinter.Label(self.frameTopLeft, text = 'How far can your car drive from a full tank of gas?')
        self.rangeEntry = tkinter.Entry(self.frameTopLeft, textvariable = self.rangeInt)
        #Create buttons to calculate mpg or quit the program
        self.calculateButton = tkinter.Button(self.frameTopRight, text = 'Calculate MPG', command = self.calculateMethod)
        self.quitButton = tkinter.Button(self.frameTopRight, text = 'Quit', command = self.window.destroy)
        #Create and set up the message with the final mpg
        self.mpgValue = tkinter.StringVar()
        self.mpgValue.set('Enter your car\'s information to calculate milage.')
        self.mpgLabel = tkinter.Label(self.frameBottom, textvariable = self.mpgValue)

        #Add the frames to the window
        self.frameBottom.pack(side = 'bottom')
        self.frameTopLeft.pack(side = 'left')
        self.frameTopRight.pack(side = 'left')
        #Add all text, entry boxes, and buttons to the frames
        self.mpgLabel.pack()
        self.capacityLabel.pack(side = 'top')
        self.capacityEntry.pack(side = 'top')
        self.rangeLabel.pack(side = 'top')
        self.rangeEntry.pack(side = 'top')
        self.calculateButton.pack(side = 'top')
        self.quitButton.pack(side = 'top')

    #Calculate mpg when the calculate button is pressed
    def calculateMethod(self):
        mpg = self.rangeInt.get() / self.capacityInt.get()
        mpg = round(mpg, 4)
        self.mpgValue.set(f'Your car\'s mileage is about {mpg} mpg.')


if __name__ == '__main__':
    Gui()
    tkinter.mainloop()
