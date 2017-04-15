#!/usr/bin/python3

import telnetlib
import socket
import tkinter as inter
import time
class interface(inter.Tk):
	def __init__(self,parent):
		inter.Tk.__init__(self,parent)
		self.parent = parent
		self.startup()
	
	def startup(self):
		self.geometry("900x450")
		self.X = 50
		self.Y = 50
		self.A = 1
		self.b = 1
		
		def conToServer():
			IP = self.inIP.get()
			Port = self.inPort.get()
			self.Host = IP
			self.Port = Port
			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket.connect((IP,int(Port)))
			self.socket.recv(1024)
			#time.sleep(10)
			#self.socket.send("lubrpo\n")
			self.socket.send(("n " + self.nick.get() + "\n").encode('utf-8'))
			#recv(1024)
		
		def shoootToServer():
			v = self.e2.get()
			grad = self.e1.get()
			print("shoot")
			self.socket.send(("v "+ str(v)+"\n").encode('utf-8'))
			time.sleep(0.1)
			#recv(1024)
			self.socket.send((str(grad) + "\n").encode('utf-8'))
			#recv(1024)c
			
		def calcEnergie():
			minFloat = float(self.minIn.get())
			maxFloat = float(self.maxIn.get())
			Power = float(self.e2.get())
			schritFloat = float(self.schritt.get())
			
			Energie =((maxFloat-minFloat)/schritFloat)*Power
			if(Energie<0):
				Energie = Energie*(-1)
			#self.enZeige.delete(0,END)
			#print(event.widget.get())
			#self.enZeige.insert(0,Energie)
			self.energieAnz['text'] = str(Energie)
			print(Energie)
			
			
		def aimThem():
			momentan = float(self.e1.get())
			save = momentan
			minimum = momentan + float(self.minIn.get())
			maximum = momentan + float(self.maxIn.get())
			zschrit = float(self.schritt.get())
			grad = minimum
			while(grad<=maximum):
				END = len(str(self.e1.get()))
				print(grad)
				self.e1.delete(0,END)
				self.e1.insert(0,str(grad))
				shoootToServer()
				grad += zschrit
			END = len(str(self.e1.get()))
			self.e1.delete(0,END)
			self.e1.insert(0,str(save))
			
			
		def retdrck(event):
			#print(["activeforeground"])
			print("Enter")
			#print(event.widget.get())
			#print ("return: event.widget is",this.event.widge)
			#print("enter")
			shoootToServer()
			
		def up(event):
			variable = float(event.widget.get())
			strlen = str(event.widget.get())
			END = len(strlen)
			variable += 1.0
			strvari = str(variable)
			#print(variable)
			event.widget.delete(0,END)
			#print(event.widget.get())
			event.widget.insert(0,strvari)
			
		def down(event):
			variable = float(event.widget.get())
			strlen = str(event.widget.get())
			END = len(strlen)
			variable -= 1.0
			strvari = str(variable)
			#print(variable)
			event.widget.delete(0,END)
			#print(event.widget.get())
			event.widget.insert(0,strvari)
			
		def upSmall(event):
			variable = float(event.widget.get())
			strlen = str(event.widget.get())
			END = len(strlen)
			variable += 0.01
			strvari = str(variable)
			#print(variable)
			event.widget.delete(0,END)
			#print(event.widget.get())
			event.widget.insert(0,strvari)
					
		def downSmall(event):
			variable = float(event.widget.get())
			strlen = str(event.widget.get())
			END = len(strlen)
			variable -= 0.01
			strvari = str(variable)
			#print(variable)
			event.widget.delete(0,END)
			#print(event.widget.get())
			event.widget.insert(0,strvari)
		
		def callEnergie(event):
			calcEnergie()
			
		#Keybinds
		self.bind('<Control-Down>',downSmall)
		self.bind('<Control-Up>',upSmall)
		self.bind('<Up>',up)
		self.bind('<Down>',down)
		self.bind('<Return>',retdrck)
		self.bind('<Right>',callEnergie)
		
		
		#Labels and buttons Standard client
		self.lickLabel=inter.Label(self,text="Nick")
		self.lickLabel.place(x = 50,y=255,width=200,height=45)
		self.nick = inter.Entry(self,font="Helvetica 15")
		self.nick.place(x =50,y=300,width=200,height=45)
		#connect to server below
		self.btn1 = inter.Button(self, text='Connect',command=conToServer)
		self.btn1.place(x=50, y=345, width=200, height=45)
		self.inIP = inter.Entry(self,font="Helvetica 11")
		self.inIP.place(x=50, y=390, width=130, height=45)
		self.inPort = inter.Entry(self,font="Helvetica  11")
		self.inPort.place(x=180,y=390,width=70,height=45)
		
		self.btn2 = inter.Button(self, text='SHOOT!',command=shoootToServer)
		self.btn2.place(x=350,y=300,width=200,height=105)
		
		self.e1 = inter.Entry(self,font="Helvetica 25",justify="center")
		self.e1.place(x=350, y=40,width=200,height=80)
		
		self.e2 = inter.Entry(self,font="Helvetica 25",justify="center")
		self.e2.place(x=350, y=160,width=200,height=80)
		
		self.lb1 = inter.Label(self,font="Helvetica 25",text='Direction',justify="right")
		self.lb1.place(x=50,y=40,width=300,height=80)
		
		self.lb2 = inter.Label(self,font="Helvetica 25",text='Speed',justify="right")
		self.lb2.place(x=50,y=160,width=300,height=80)
		
		
		#Labels and Input Aim-Help
		self.enZeige = inter.Label(self,font="Helvetica 12", text="Ben-Energie:")
		self.enZeige.place(x=760,y=40,width=100,height=50)
		self.energieAnz = inter.Label(self,font="Helvetica 12", text="0")
		self.energieAnz.place(x=760,y=100,width=100,height=50)
		
		self.mini = inter.Label(self,font="Helvetica 12",text='Min Korrektur')
		self.mini.place(x=600,y=40,width=150,height=45)
		self.minIn = inter.Entry(self,font="Helvetica 11")
		self.minIn.place(x=600,y=100,width=150,height=45)
		
		self.maxi = inter.Label(self,font="Helvetica 12",text='Max Korrektur',justify="right")
		self.maxi.place(x=600,y=150,width=150,height=45)
		self.maxIn = inter.Entry(self,font="Helvetica 11")
		self.maxIn.place(x=600,y=200,width=150,height=45)
		
		self.schrittl = inter.Label(self,font="Helvetica 12",text='Korrektur Schritt',justify="right")
		self.schrittl.place(x=600,y=250,width=150,height=45)
		self.schritt = inter.Entry(self,font="Helvetica 11")
		self.schritt.place(x=600,y=300,width=150,height=45)
		
		#Labels and Input
		self.aimIt = inter.Button(self, text='Auto',command=aimThem)
		self.aimIt.place(x=760,y=175,width=100,height=50)
			
if __name__ =="__main__":
	app = interface(None)
	app.title("Interface")
	app.mainloop()
	
