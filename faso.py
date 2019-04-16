from tkinter import *

# Define ventana
root = Tk()
root.title('Matematica Superior')
root.resizable(0, 0)  

# Frame 1 para primer numero
frame1 = Frame(root)
frame1.pack()
real1 = Entry(frame1)
imaginario1 = Entry(frame1)
real1.pack(side=RIGHT)
imaginario1.pack(side=RIGHT)
label = Label(frame1, text='Ingrese el primer campo:').pack(side=LEFT)

# Frame 2 para primer numero
frame2 = Frame(root)
frame2.pack()
real2 = Entry(frame2)
imaginario2 = Entry(frame2)
real2.pack(side=RIGHT)
imaginario2.pack(side=RIGHT)
label = Label(frame2, text='Ingrese el segundo campo:').pack(side=LEFT)


root.mainloop()
