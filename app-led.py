from tkinter import Tk, Widget, ttk
import serial
import time
ser = serial.Serial('/dev/ttyUSB0',9600,timeout = 1)
def encendido():
    ser.write(b'e')
def apagado():
    ser.write(b'a')
def cerrar():
    ser.write(b'c')
    exit()
    
raiz = Tk()
raiz.config(width=400,height=200)
raiz.title('Blink')
boton =ttk.Button(text='encendido',command=encendido)
boton.place(x=50,y=50)
boton =ttk.Button(text='apagado',command=apagado)
boton.place(x=150,y=50)
boton =ttk.Button(text='cerrar',command=cerrar)
boton.place(x=250,y=50)
raiz.mainloop()
