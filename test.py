from tkinter import *
class InputPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)        

        label = Label(self, text="Zorgplan input")
        label.grid(row=0, column=0, sticky ='n', columnspan =2)

        # i brought your variable in the class for example sake 

        namesInput = ["First:", "second:", "Third:", "Fourth:", "Fifth:"]

        self.entryWidgets = [] # we want to call this in another function so we assign it as self.variableName

        labelWidgets = []

        #LOOP TO CREATE WIDGETS
        for i in range(0, len(namesInput)):
            labelWidgets.append(Label(self, text = namesInput[i]))
            self.entryWidgets.append(Entry(self))
            labelWidgets[-1].grid(row= i+1, column =0, sticky='e')
            self.entryWidgets[-1].grid(row= i+1, column = 1, sticky='w')

        submit = Button(self, text = "Submit", command = self.getEntries)
        submit.grid(row = 6, column =0, columnspan =2)

    def getEntries(self):
        results = []

        for x in self.entryWidgets: # i.e for each widget in entryWidget list
            results.append(x.get())
        print(results)

app = ZorgplanGrafiek()
app.mainloop()