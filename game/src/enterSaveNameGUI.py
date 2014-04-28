from Tkinter import *

class EnterSaveNameGUI:

	def __init__(self, master=None):
		self.saveName = ''
		self.master = Tk()
		self.master.title("Enter Save Name")
		self.master.geometry("300x100")
		self.textbox = Entry(self.master)
		self.enter = Button(self.master, text="Enter", width=20, command=self.enter)
		self.textbox.pack()
		self.enter.pack()
		self.master.mainloop()

	def enter(self):
		self.saveName = self.textbox.get()
		self.master.quit()
		self.master.destroy()
