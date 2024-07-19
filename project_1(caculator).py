from tkinter import *
from tkinter import messagebox

root =Tk()
root.title("Calculator")
root.geometry("450x600")
root.resizable(False,False)
root.configure(background='#6b83b2')

exp=''

equation = StringVar() 
def total_1():
    try:
        global exp
        total=str(eval(exp))
        equation.set(total)
        exp=''
    except:
        equation.set("Error")
        exp=''
        
def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)
    
def clear():
    global exp
    exp=''
    equation.set('')
    


button_1=Button(root,text="1",fg='white',width=10,height=3,command=lambda: press(1),bg='#83b26b').place(x=20,y=350)
button_2=Button(root,text="2",fg='white',width=10,height=3,command=lambda: press(2),bg='#83b26b').place(x=130,y=350)
button_3=Button(root,text="3",fg='white',width=10,height=3,command=lambda: press(3),bg='#83b26b').place(x=240,y=350)
button_4=Button(root,text="4",fg='white',width=10,height=3,command=lambda: press(4),bg='#83b26b').place(x=20,y=250)
button_5=Button(root,text="5",fg='white',width=10,height=3,command=lambda: press(5),bg='#83b26b').place(x=130,y=250)
button_6=Button(root,text="6",fg='white',width=10,height=3,command=lambda: press(6),bg='#83b26b').place(x=240,y=250)
button_7=Button(root,text="7",fg='white',width=10,height=3,command=lambda: press(7),bg='#83b26b').place(x=20,y=150)
button_8=Button(root,text="8",fg='white',width=10,height=3,command=lambda: press(8),bg='#83b26b').place(x=130,y=150)
button_9=Button(root,text="9",fg='white',width=10,height=3,command=lambda: press(9),bg='#83b26b').place(x=240,y=150)
button_10=Button(root,text="0",fg='white',width=10,height=3,command=lambda: press(0),bg='#83b26b').place(x=20,y=430)
button_11=Button(root,text="+",fg='white',width=10,height=3,command=lambda: press('+'),bg='#83b26b').place(x=350,y=150)
button_12=Button(root,text="-",fg='white',width=10,height=3,command=lambda: press('-'),bg='#83b26b').place(x=350,y=250)
button_13=Button(root,text="*",fg='white',width=10,height=3,command=lambda: press('*'),bg='#83b26b').place(x=350,y=350)
button_14=Button(root,text="/",fg='white',width=10,height=3,command=lambda: press('/'),bg='#83b26b').place(x=350,y=430)
button_15=Button(root,text="clear",fg='white',width=51,height=3,command=clear,bg='#83b26b').place(x=20,y=510)
button_16=Button(root,text="=",fg='white',width=10,height=3,command=total_1,bg='#83b26b').place(x=240,y=430)
button_17=Button(root,text=".",fg='white',width=10,height=3,command=lambda: press('.'),bg='#83b26b').place(x=130,y=430)


entry_1 = Entry(root, width=25, textvariable=equation, font=("Arial", 20), borderwidth=2, relief="solid")
entry_1.place(x=20, y=50, width=410, height=50)

root.mainloop()