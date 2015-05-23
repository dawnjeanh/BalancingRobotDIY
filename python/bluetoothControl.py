from Tkinter import *
import tkMessageBox
import serial, time
import serial.tools.list_ports


class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.master.title('bluetooth control')
        self.master.geometry("300x150+300+300")
        self.isSerialOpen = 0

    def createWidgets(self):
        self.helloLabel = Label(self, text = 'bluetooth control v1.0')
        self.helloLabel.grid(row=0, column=1)
        self.buttonUp = Button(self, text="Up", height=1, width=10, command=self.onButtonUp)
        self.buttonUp.grid(row=1, column=1)
        self.buttonLeft = Button(self, text="Left", height=1, width=10, command=self.onButtonLeft)
        self.buttonLeft.grid(row=2, column=0)
        self.buttonRight = Button(self, text="Right", height=1, width=10, command=self.onButtonRight)
        self.buttonRight.grid(row=2, column=2)
        self.buttonDown = Button(self, text="Down", height=1, width=10, command=self.onButtonDown)
        self.buttonDown.grid(row=3, column=1)
        self.serialNumLabel = Label(self, text = 'serial num:')
        self.serialNumLabel.grid(row=4, column=0)
        self.serialNumEntry = Entry(self, width=10)
        self.serialNumEntry.grid(row=4, column=1)
        self.buttonSerial = Button(self, text="open", height=1, width=10, command=self.onButtonSerial)
        self.buttonSerial.grid(row=4, column=2)

    def onButtonSerial(self):
        if self.isSerialOpen==0:
            com = self.serialNumEntry.get()
            if com is '':
                tkMessageBox.showinfo("info", "com is null")
            else:
                self.serial = serial.Serial("com"+com, 115200)
                self.isSerialOpen = 1
                self.buttonSerial["text"] = self.isSerialOpen and "opened" or "open"

    def onButtonUp(self):
        if self.isSerialOpen:
            self.serial.write("\x01")
            time.sleep(0.1)
            self.serial.write("\x00")

    def onButtonLeft(self):
        if self.isSerialOpen:
            self.serial.write("\x03")
            time.sleep(0.1)
            self.serial.write("\x00")

    def onButtonRight(self):
        if self.isSerialOpen:
            self.serial.write("\x07")
            time.sleep(0.1)
            self.serial.write("\x00")

    def onButtonDown(self):
        if self.isSerialOpen:
            self.serial.write("\x05")
            time.sleep(0.1)
            self.serial.write("\x00")


app = Application()
app.mainloop()