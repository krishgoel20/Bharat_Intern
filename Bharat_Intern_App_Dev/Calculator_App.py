from tkinter import *

app = Tk()  # Create a Window
app.title("Calculator App")  
app.geometry("300x334")  # Size of Window
app.resizable(0,0)  # Prevents the Window from Resizing itself

def click_button(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def clear_button():
    global expression
    expression = ""
    input_text.set("")

def equal_button():
    global expression
    result = str(eval(expression)) 
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

# Frame for Input
input_frame = Frame(app,width=312,height=50,bd=0,highlightbackground="yellow",highlightcolor="yellow",highlightthickness=2)
input_frame.pack(side=TOP)

# Input Field inside 'Frame'
input_field = Entry(input_frame,font=('arial',18,'bold'),textvariable=input_text,width=50,bg="yellow",bd=0,justify=RIGHT)
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)  

frame_btn = Frame(app,width=312,height=272.5,bg="black")
frame_btn.pack()

# 1st Row of Buttons
clear = Button(frame_btn,text="C",fg="red",width=32,height=3,bd=0,bg="light blue",command=lambda: clear_button()).grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide = Button(frame_btn,text="/",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button("/")).grid(row=0,column=3,padx=1,pady=1)

# 2nd Row of Buttons
seven = Button(frame_btn,text="7",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(7)).grid(row=1,column=0,padx=1,pady=1)
eight = Button(frame_btn,text="8",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(8)).grid(row=1,column=1,padx=1,pady=1)
nine = Button(frame_btn,text="9",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(9)).grid(row=1,column=2,padx=1,pady=1)
multiply = Button(frame_btn,text="*",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button("*")).grid(row=1,column=3,padx=1,pady=1)

# 3rd Row of Buttons
four = Button(frame_btn,text="4",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(4)).grid(row=2,column=0,padx=1,pady=1)
five = Button(frame_btn,text="5",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(5)).grid(row=2,column=1,padx=1,pady=1)
six = Button(frame_btn,text="6",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(6)).grid(row=2,column=2,padx=1,pady=1)
minus = Button(frame_btn,text="-",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button("-")).grid(row=2,column=3,padx=1,pady=1)

# 4th Row of Buttons
one = Button(frame_btn,text="1",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(1)).grid(row=3,column=0,padx=1,pady=1)
two = Button(frame_btn,text="2",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(2)).grid(row=3,column=1,padx=1,pady=1)
three = Button(frame_btn,text="3",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(3)).grid(row=3,column=2,padx=1,pady=1)
plus = Button(frame_btn,text="+",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button("+")).grid(row=3,column=3,padx=1,pady=1)

# 5th Row of Buttons
zero = Button(frame_btn,text="0",fg="red",width=21,height=3,bd=0,bg="light blue",command=lambda: click_button(0)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
point = Button(frame_btn,text=".",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: click_button(".")).grid(row=4,column=2,padx=1,pady=1)
equals = Button(frame_btn,text="=",fg="red",width=10,height=3,bd=0,bg="light blue",command=lambda: equal_button()).grid(row=4,column=3,padx=1,pady=1)

app.mainloop()