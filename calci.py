from tkinter import *
def click(event):
    global stringvar
    text = event.widget.cget("text")
    print(text)
    
    if text == "=":
        if stringvar.get().isdigit():
            value = int(stringvar.get())
        else:
            value = eval(screen.get())
        stringvar.set(value)
        screen.update()                 
    elif text == "C":
        stringvar.set("")
        screen.update()
    else:
        
        stringvar.set(stringvar.get() + text)
        screen.update()
def backspace(event):
    global stringvar
    current_text = stringvar.get()
    stringvar.set(current_text[:-1])
    screen.update()
root = Tk()
root.title("Mini Calculator")
root.geometry("700x900")

stringvar = StringVar()
stringvar.set("") 
screen = Entry(root, textvar=stringvar, font="lucida 40 bold", bg="cyan", bd=40)
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="yellow")
b = Button(f, text="9", font="lucida 30 bold", padx=14, pady=12 )
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="8", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="7", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")
b = Button(f, text="6", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="5", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="4", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")
b = Button(f, text="3", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="2", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="1", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")
b = Button(f, text="0", font="lucida 30 bold", padx=15, pady=15)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="-", font="lucida 30 bold", padx=17, pady=15)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="*", font="lucida 30 bold", padx=16, pady=15)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")
b = Button(f, text="/", font="lucida 30 bold", padx=14, pady=11)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="%", font="lucida 28 bold", padx=14, pady=11)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="=", font="lucida 30 bold", padx=14, pady=11)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

f.pack()
f = Frame(root, bg="grey")
b = Button(f, text="C", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="+", font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", click)

b = Button(f, text="AC",font="lucida 30 bold", padx=14, pady=12)
b.pack(side=LEFT)
b.bind("<Button-1>", backspace)

f.pack()
root.mainloop()
