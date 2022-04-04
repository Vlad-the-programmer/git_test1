from Sort import Sort
from Sort import Modified_Sort
from tkinter import *


root = Tk()

# global var
input_list = []


def submit2():
    global input_list
    input_list = list(e2.get())
    Label3 = Label(root, text='Wonderful! Now let me process that up....').pack()


Label2 = Label(root, text="Enter a list you want to sort: ").pack()

e2 = Entry(root, width=30, bg='blue', fg='white', selectforeground='black')
e2.pack()


Label3 = Label(root, text="Enter a start, an end and an algorithm to sort the list in-place: ").pack()
Label_3 = Label(root, text='Algorithms: Sortbubble -> 1, SortInsertion -> 2, SortSelection -> 3: ').pack()

e3 = Entry(root, width=10)
e3.pack()
e4 = Entry(root, width=10)
e4.pack()
e5 = Entry(root, width=10)
e5.pack()


def createNewWindow():
    submit2()
    app2 = Toplevel()
    app2.wm_title("Result")

    start = int(e3.get())
    end = int(e4.get())
    sorted_list = Modified_Sort(input_list, start, end)

    Label_str = Label(app2, text="Entered list is: " + str(list(e2.get()))).pack()
    if e5.get() == '1':
        Label4 = Label(app2, text="Sorted list is: " + str(sorted_list.SortBubble())).pack()
        return Label4
    elif e5.get() == '2':
        Label4 = Label(app2, text="Sorted list is: " + str(sorted_list.SortInsertion())).pack()
        return Label4
    elif e5.get() == '3':
        Label4 = Label(app2, text="Sorted list is: " + str(sorted_list.SortSelection())).pack()
        return Label4
    else:
        print('Enter 1, 2, or 3!')


button3 = Button(root, text='Submit', command=createNewWindow).pack()


root.mainloop()






