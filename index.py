from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
import sqlite3

class DB:
	def __init__(self):
		self.db = 'database.db' #Base de datos
	def run_query(self,query,parameters=()):
		with sqlite3.connect(self.db) as conn:
			cursor = conn.cursor()
			result = cursor.execute(query,parameters)
			conn.commit()
			return result
	def consult(self,user,passoword):
		sql = 'SELECT * FROM login WHERE Nombre_user=? AND Clave_user=?' #Consulta
		parameters = (user,passoword)
		result = self.run_query(sql,parameters)
		if(result.fetchall()):
			print("Tienes acceso")
			window1 = Toplevel()
			window1.title("Panel")
			Label(window1,text='Bienvenido',font=('Arial',12)).grid(row=0,column=0)
		else:
			print("No tienes acceso")
			msg.showerror(message='Usuario y contraseña',title='Incorrecto')

class App:
	def __init__(self,window):
		self.window0 = window
		self.window0.title("Panel")
		self.database = DB()
		#Frontend
		frame = LabelFrame(self.window0,text='Login')
		frame.grid(row=0,column=0)
		#input
		Label(frame,text='User').grid(row=1,column=1)
		self.Entry_user = Entry(frame)
		self.Entry_user.grid(row=1,column=2)

		Label(frame,text='Password').grid(row=2,column=1)
		self.Entry_password = Entry(frame,show='*')
		self.Entry_password.grid(row=2,column=2)

		ttk.Button(frame,text='Login',command=self.login).grid(row=3,column=1)

	def login(self):
		user = self.Entry_user.get()
		passoword = self.Entry_password.get()
		if(user !='' and passoword !=''):
			self.database.consult(user,passoword)
		else:
			msg.showerror(message='Los campos son requeridos',title='Info')


if __name__==('__main__'):
	root = Tk()
	login = App(root)
	root.mainloop()
