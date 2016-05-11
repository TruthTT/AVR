import os
from Tkinter import *
from tkFileDialog import *
mmcu='atmega8'
port='/dev/ttyACM0'
brate='19200'

class Proj:
    def __init__(self, master):
        self.master = master
        master.title("AVRISP python")

	self.myLabel2 = Label(master, text='Enter the MMCU word:')
        self.myLabel2.place(x=10,y=150)
        self.myEntryBox2 = Entry()
	self.myEntryBox2.insert(END, 'atmega8')        
	self.myEntryBox2.place(x=180,y=150)  
        

	self.mySubmitButton = Button(master, text='Hex!!', command=self.hexf)
        self.mySubmitButton.place(x=350,y=150)
	
	self.greet_button = Button(master, text="Greet", command=self.greet)
        self.greet_button.pack()

	self.browse_button = Button(master, text="Browse...", command=self.browse)
        self.browse_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()


	self.myLabel3 = Label(master, text='Enter the port')
	self.myLabel3.place(x=10,y=200)
        self.myEntryBox3 = Entry()
	self.myEntryBox3.insert(END, '/dev/ttyACM0')        
	self.myEntryBox3.place(x=180,y=200)  
        self.myLabel4 = Label(master, text='Enter the baudrate:')
        self.myLabel4.place(x=10,y=250)
        self.myEntryBox4 = Entry()
	self.myEntryBox4.insert(END, '19200')
        self.myEntryBox4.place(x=180,y=250)  
        	
	
        self.burn_button = Button(master, text="BURN !!", command=self.burn)
        self.burn_button.place(x=180,y=300)



    def browse(self):
	self.fileName = askopenfilename(parent=root)
	actualName=self.fileName.split('/')
	self.actualName=actualName[-1]
	
    def hexf(self):
 	hexf= self.myEntryBox2.get()	
	fileName=self.fileName	
	obfName = fileName.replace('.c','.o')	
	elfName = fileName.replace('.c','.elf')
	hexfName = fileName.replace('.c','.hex')	
	print hexf
	print "Creating object file..."
	os.system("avr-gcc -g -Os -mmcu="+hexf+" -c "+fileName)
	print "creating .elf file..."
	os.system("avr-gcc -g -mmcu="+hexf+" -o "+elfName+ " "+ obfName)
	print "creating .hex file..."	
        os.system("avr-objcopy -j .text -j .data -O ihex "+ elfName+" "+hexfName)
	print ".hex file created !!"

    def greet(self):
        print("Greetings!")

    def burn(self):
	hexf= self.myEntryBox2.get()
	port=self.myEntryBox3.get()
	baud=self.myEntryBox4.get()
	fileName=self.fileName
	hexfName = fileName.replace('.c','.hex')	
	os.system("sudo avrdude -c avrisp -p "+ hexf +" -P "+port+" -b "+baud+" -U flash:w:"+hexfName)
root = Tk()
my_gui = Proj(root)
root.geometry("450x370+200+200")
root.mainloop()

