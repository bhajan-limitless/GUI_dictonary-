from tkinter import *
import Backend0

def fetch_and_view():
    list1.delete(0, END)
    for row in Backend0.find_meaning(search_word.get()):
        list1.insert(END, row)


gui = Tk()

l1 = Label(gui, text = "Enter The Word")
l1.grid(row=0, column=0)


search_word = StringVar()
s1=Entry(gui, textvariable=search_word)
s1.grid(row=1, column=0)

b1 = Button(gui, text="Search", width=12, command=fetch_and_view)
b1.grid(row=1, column=2)

l1 = Label(gui, text = "Meaning")
l1.grid(row=2, column=0)

list1 = Listbox(gui, height=10, width = 30)
list1.grid(row=3, column=0, columnspan=2)





gui.mainloop()
