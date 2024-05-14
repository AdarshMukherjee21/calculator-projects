from tkinter import *
root = Tk()
root.title("simple calculator")

calc_input=Entry(root, width=60, borderwidth=10,) 
calc_input.grid(row=0,column=0,columnspan= 4,padx=2,  pady=2 )
# calc_input.insert(0)

def button_click(number ):
    # calc_input.delete(0,END)
   
    current=calc_input.get()
    calc_input.delete(0,END)

    calc_input.insert(0,str(current) + str(number))
 
def clear():
    calc_input.delete(0,END)

def button_add():
    var1= float(calc_input.get())
    global first_num
    first_num= var1
    global operator 
    operator = "+"
    calc_input.delete(0,END)
def button_sub():
    if calc_input.get() == "":
        calc_input.insert(0,"-")
    else:
        var1= float(calc_input.get())
        global first_num
        first_num= var1
        global operator 
        operator = "-"
        calc_input.delete(0,END)


def button_mul():
    var1= float(calc_input.get())
    global first_num
    first_num= var1
    global operator 
    operator = "x"
    calc_input.delete(0,END)

def button_div():
    var1= float(calc_input.get())
    global first_num
    first_num= var1
    global operator 
    operator = "/"
    calc_input.delete(0,END)

def button_power():
    var1= float(calc_input.get())
    global first_num
    first_num= var1
    global operator 
    operator = "^"
    calc_input.delete(0,END)

def button_root():
    var1= float(calc_input.get())
    global first_num
    first_num= var1
    global operator 
    operator = "root"

    if var1 < 0:
        calc_input.delete(0,END)
        calc_input.insert(0," Please only use positve values")
    else:
        calc_input.delete(0,END)

def button_root_any():
    var1= float(calc_input.get())
    global first_num
    first_num= var1
    global operator 
    operator = "root_any"

    if var1 < 0:
        calc_input.delete(0,END)
        calc_input.insert(0," Please only use positve values")
    else:
        calc_input.delete(0,END)

    
def button_equal():
    second_number= calc_input.get()
    calc_input.delete(0, END)
    if operator == "+":
        calc_input.insert(0, first_num + float(second_number))
    elif operator == "-":
        calc_input.insert(0, first_num - float(second_number))
    elif operator == "x":
        calc_input.insert(0, first_num * float(second_number))
    elif operator == "/":
        calc_input.insert(0, first_num / float(second_number))
    elif operator == "^":
        calc_input.insert(0, first_num ** float(second_number))    
    elif operator == "root":
        calc_input.insert(0, first_num ** (1/2))  
    elif operator == "root_any":
        calc_input.insert(0, first_num ** (1/float(second_number))) 


# makig buttons
button_1=Button(root, text="1", padx=40,pady=20, command=lambda: button_click(1),borderwidth=3)
button_2=Button(root, text="2", padx=40,pady=20, command=lambda: button_click(2),borderwidth=3)
button_3=Button(root, text="3", padx=40,pady=20, command=lambda: button_click(3),borderwidth=3)
button_4=Button(root, text="4", padx=40,pady=20, command=lambda: button_click(4),borderwidth=3)
button_5=Button(root, text="5", padx=40,pady=20, command=lambda: button_click(5),borderwidth=3)
button_6=Button(root, text="6", padx=40,pady=20, command=lambda: button_click(6),borderwidth=3)
button_7=Button(root, text="7", padx=40,pady=20, command=lambda: button_click(7),borderwidth=3)
button_8=Button(root, text="8", padx=40,pady=20, command=lambda: button_click(8),borderwidth=3)
button_9=Button(root, text="9", padx=40,pady=20, command=lambda: button_click(9),borderwidth=3)
button_0=Button(root, text="0", padx=40,pady=20, command=lambda: button_click(0),borderwidth=3)
button_add=Button(root,text="+",padx=39,pady=20, command=button_add,borderwidth=3)
button_equal=Button(root,text="=",padx=40,pady=20, command=button_equal, bg= "#00f000",borderwidth=5)
button_clear=Button(root, text="Clear", padx=79,pady=20, command=clear,borderwidth=3)
button_sub=Button(root,text="-",padx=40,pady=20, command=button_sub,borderwidth=3)
button_mul=Button(root,text="x",padx=40,pady=20, command=button_mul,borderwidth=3)
button_div=Button(root,text="/",padx=40,pady=20, command=button_div,borderwidth=3)
button_power=Button(root,text="^",padx=40,pady=20, command=button_power ,borderwidth=3)
button_rootb=Button(root,text="root(2)",padx=40,pady=20, command=button_root ,borderwidth=3)
button_decimalpoint=Button(root,text="  .  ", padx=35,pady=20, command=lambda: button_click("."),borderwidth=3)
button_root_anyb=Button(root,text="root(X)",padx=23,pady=20, command=button_root_any ,borderwidth=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_mul.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_sub.grid(row=2,column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1,column=3)


button_0.grid(row=4, column=0)
button_equal.grid(row=4,column=2)
button_decimalpoint.grid(row=4,column=1)
button_div.grid(row=4, column=3)

button_clear.grid(row=5, column=2, columnspan=2 )
button_power.grid(row=5,column=0)
button_root_anyb.grid(row=5,column=1)




# button_rootb.grid(row=7,column=2)


root.mainloop()