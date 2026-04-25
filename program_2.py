#Week 12, Program 2 - Joe's Automotive
#Caiden Heinrichs
#04/24/26

import tkinter


class Gui():
    def __init__(self):
        #Create and set up window
        self.window = tkinter.Tk()
        self.window.title('Joe\'s Automotive Cost Calculator')
        self.window.minsize(500, 250)
        self.window.maxsize(500, 250)
        #Create frames
        self.leftFrame = tkinter.Frame(self.window, width = 250, height = 250)
        self.rightFrame = tkinter.Frame(self.window, width = 250, height = 250)

        #Create variables to store the cost of each service and the total
        self.totalCost = tkinter.IntVar()
        self.oilChangeCost = tkinter.IntVar()
        self.lubeJobCost = tkinter.IntVar()
        self.radiatorFlushCost = tkinter.IntVar()
        self.transmissionFluidCost = tkinter.IntVar()
        self.inspectionCost = tkinter.IntVar()
        self.mufflerReplacementCost = tkinter.IntVar()
        self.tireRotationCost = tkinter.IntVar()
        #Text displays for instruction and total cost
        self.instructionText = tkinter.Label(self.leftFrame, text = 'Check all desired services to calculate the cost:')
        self.totalCostDisplayText = tkinter.Label(self.rightFrame, text = 'The total cost is:')
        self.totalCostDisplayNumber = tkinter.Label(self.rightFrame, textvariable = self.totalCost)
        #Create check buttons for each service and quit button
        self.quitButton = tkinter.Button(self.rightFrame, text = 'Quit', command = self.window.destroy)
        self.oilChangeButton = tkinter.Checkbutton(self.leftFrame, text = 'Oil Change ($30.00)', variable = self.oilChangeCost, offvalue = 0, onvalue = 30, command = self.updateTotalCost)
        self.lubeJobButton = tkinter.Checkbutton(self.leftFrame, text = 'Lube Job ($20.00)', variable = self.lubeJobCost, offvalue = 0, onvalue = 20, command = self.updateTotalCost)
        self.radiatorFlushButton = tkinter.Checkbutton(self.leftFrame, text = 'Radiator Flush ($40.00)', variable = self.radiatorFlushCost, offvalue = 0, onvalue = 40, command = self.updateTotalCost)
        self.transmissionFluidButton = tkinter.Checkbutton(self.leftFrame, text = 'Transmission Fluid ($100.00)', variable = self.transmissionFluidCost, offvalue = 0, onvalue = 100, command = self.updateTotalCost)
        self.inspectionButton = tkinter.Checkbutton(self.leftFrame, text = 'Inspection ($35.00)', variable = self.inspectionCost, offvalue = 0, onvalue = 35, command = self.updateTotalCost)
        self.mufflerReplacementButton = tkinter.Checkbutton(self.leftFrame, text = 'Muffler Replacement ($200.00)', variable = self.mufflerReplacementCost, offvalue = 0, onvalue = 200, command = self.updateTotalCost)
        self.tireRotationButton = tkinter.Checkbutton(self.leftFrame, text = 'Tire Rotation ($20.00)', variable = self.tireRotationCost, offvalue = 0, onvalue = 20, command = self.updateTotalCost)
        #Pack all frames, buttons, and labels
        self.leftFrame.pack(side = 'left')
        self.rightFrame.pack(side = 'left')
        self.totalCostDisplayText.pack(side = 'top')
        self.totalCostDisplayNumber.pack(side = 'top')
        self.quitButton.pack(side = 'top')
        self.instructionText.pack(side = 'top')
        self.oilChangeButton.pack(side = 'top')
        self.lubeJobButton.pack(side = 'top')
        self.radiatorFlushButton.pack(side = 'top')
        self.transmissionFluidButton.pack(side = 'top')
        self.inspectionButton.pack(side = 'top')
        self.mufflerReplacementButton.pack(side = 'top')
        self.tireRotationButton.pack(side = 'top')

    #Update the total cost by recalculating the sum
    def updateTotalCost(self):
        self.totalCost.set(self.oilChangeCost.get() + self.lubeJobCost.get() + self.radiatorFlushCost.get() + self.transmissionFluidCost.get() +
                          self.inspectionCost.get() + self.mufflerReplacementCost.get() + self.tireRotationCost.get())


if __name__ == '__main__':
    Gui()
    tkinter.mainloop()
