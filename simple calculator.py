from tkinter import *

root=Tk()
root.title("Simple Calculator")

e = Entry(width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3)

def ButtonClick(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))
    
def ButtonClear():
    e.delete(0, END)
    
def ButtonAdd():
    global f_num
    global math
    math = 1
    firstnumber=e.get()
    f_num =int(firstnumber)
    e.delete(0, END)
      
def ButtonSub():
    global f_num
    global math
    math = 2 
    firstnumber=e.get()
    f_num =int(firstnumber)
    e.delete(0, END)
    
def ButtonMul():
    global f_num
    global math
    math = 3 
    firstnumber=e.get()
    f_num =int(firstnumber)
    e.delete(0, END)
    
def ButtonDiv():
    global f_num
    global math
    math = 4 
    firstnumber=e.get()
    f_num =int(firstnumber)
    e.delete(0, END) 
    

def ButtonEqual():
    secondnumber=e.get()
    e.delete(0, END)
    
    if math ==1:
        e.insert(0, f_num+int(secondnumber))
        
    elif math ==2:
        e.insert(0, f_num-int(secondnumber))
        
    elif math ==3:
        e.insert(0, f_num*int(secondnumber))
        
    else:
        e.insert(0, f_num/int(secondnumber))

button1=Button(text=1,padx=40,pady=20, command = lambda: ButtonClick(1)).grid(row=1,column=0)
button2=Button(text=2,padx=40,pady=20, command = lambda: ButtonClick(2)).grid(row=1,column=1)
button3=Button(text=3,padx=40,pady=20, command = lambda: ButtonClick(3)).grid(row=1,column=2)

button4=Button(text=4,padx=40,pady=20, command = lambda: ButtonClick(4)).grid(row=2,column=0)
button5=Button(text=5,padx=40,pady=20, command = lambda: ButtonClick(5)).grid(row=2,column=1)
button6=Button(text=6,padx=40,pady=20, command = lambda: ButtonClick(6)).grid(row=2,column=2)

button7=Button(text=7,padx=40,pady=20, command = lambda: ButtonClick(7)).grid(row=3,column=0)
button8=Button(text=8,padx=40,pady=20, command = lambda: ButtonClick(8)).grid(row=3,column=1)
button9=Button(text=9,padx=40,pady=20, command = lambda: ButtonClick(9)).grid(row=3,column=2)

button0=Button(text=0,padx=40,pady=20, command = lambda: ButtonClick(0)).grid(row=4,column=0)
buttonClear=Button(text="Clear",padx=78,pady=20, command=ButtonClear).grid(row=4,column=1,columnspan=2)
buttonAdd=Button(text="+",padx=40,pady=20, command=ButtonAdd).grid(row=5,column=0)
buttonEqual=Button(text="=",padx=88,pady=20, command=ButtonEqual).grid(row=5,column=1,columnspan=2)

buttonSub=Button(text="-",padx=40,pady=20, command=ButtonSub).grid(row=6,column=0)
buttonMul=Button(text="*",padx=40,pady=20, command=ButtonMul).grid(row=6,column=1)
buttonDiv=Button(text="/",padx=40,pady=20, command=ButtonDiv).grid(row=6,column=2)

root.mainloop()