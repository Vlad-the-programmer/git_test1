from Sort import Sort
from Sort import Modified_Sort
from tkinter import *

root = Tk()

Label0 = Label(root, text="What is your name: ")
Label0.pack()

e = Entry(root, width=12, bg='purple', fg='white')
e.pack()


def submit_name():
    label1 = Label(root, text="Hello, " + e.get() + " !")
    label1.pack()


submit_name()


def submit2():
    global input_list
    input_list = e2.get()
    label3 = Label(root, text='Wonderful! Now let me process that up....')
    label3.pack()


def submit3():
    Label3 = Label(root, text="Enter start and end to sort the list in place: ")
    Label3.pack()



button1 = Button(root, text='Submit', command=submit_name())
button1.pack()

Label2 = Label(root, text="Enter a list you want to sort: ")
Label2.pack()

e2 = Entry(root, width=30, bg='blue', fg='white')
e2.pack()

button3 = Button(root, text='Submit', command=submit2()).pack()

submit3()

e3 = Entry(root, width=10)
e3.pack()

e4 = Entry(root, width=10)
e4.pack()

button2 = Button(root, text='Submit', command=submit2()).pack()

Label4 = Label(root, text="If you want to sort the entire list, then enter 0: ")
Label4.pack()

e4 = Entry(root, width=10)
e4.pack()


input_list = []


myButton = Button(root, text='Submit', command=submit2())
myButton.pack()

start = e3.get()
end = e4.get()

def createNewWindow():
    newWindow = Toplevel(app)
    if Label4 == '':
        sorted_list = Modified_Sort(input_list, start, end)
        Label5 = Label(root, text="Sorted list is: " + sorted_list)
        Label5.pack()
    elif Label4 == 0:
        sorted_list = Sort(input_list, start, end)
        Label5 = Label(root, text="Sorted list is: " + sorted_list)
        Label5.pack()
    else:
        Label5 = Label(root, text="Enter 0 or nothing!")
        Label5.pack()


app = Tk()











root.mainloop()





