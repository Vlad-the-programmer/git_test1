from git_test1.Project2.Sort import Sort
from git_test1.Project2.Sort import Modified_Sort
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

Label_scope = Label(root, text="Enter a start and an end  to sort the list in-place: ").pack()
e3 = Entry(root, width=10)
e3.pack()
e4 = Entry(root, width=10)
e4.pack()
Label_algorithm = Label(root, text='Algorithms: Sortbubble -> 1, SortInsertion -> 2, SortSelection -> 3: ').pack()

e5 = Entry(root, width=10)
e5.pack()


def createNewWindow():
    submit2()
    app2 = Toplevel()
    app2.wm_title("Result")

    start = int(e3.get())
    end = int(e4.get())
    sorted_list_in_place = Modified_Sort(input_list, start, end)

    Label_sort = Label(app2, text='In-place Sort\n').pack()
    Label_str = Label(app2, text="Entered list is:\n " + str(list(e2.get()))).pack()
    Label_space = Label(app2, text='\n')

    if e5.get() == '1':
        Label4 = Label(app2, text="Sorted list is:\n " + str(sorted_list_in_place.SortBubble())).pack()
        return Label4
    elif e5.get() == '2':
        Label4 = Label(app2, text="Sorted list is:\n " + str(sorted_list_in_place.SortInsertion())).pack()
        return Label4
    elif e5.get() == '3':
        Label4 = Label(app2, text="Sorted list is:\n " + str(sorted_list_in_place.SortSelection())).pack()
        return Label4
    else:
        print('Enter 1, 2, or 3!')


button3 = Button(root, text='Sort', command=createNewWindow).pack()


def ordinary_sorting():
    app3 = Toplevel()
    app3.wm_title("Result1")

    submit2()
    sorted_list = Sort(input_list)
    Label_sort = Label(app3, text='Ordinary Sort\n').pack()
    Label_str = Label(app3, text="Entered list is:\n " + str(list(e2.get()))).pack()
    Label_space = Label(app3, text='\n')
    if e5.get() == '1':
        Label4 = Label(app3, text="Sorted list is:\n " + str(sorted_list.SortBubble())).pack()
        return Label4
    elif e5.get() == '2':
        Label4 = Label(app3, text="Sorted list is:\n " + str(sorted_list.SortInsertion())).pack()
        return Label4
    elif e5.get() == '3':
        Label4 = Label(app3, text="Sorted list is:\n " + str(sorted_list.SortSelection())).pack()
        return Label4
    elif e5.get() == '':
        pass
    else:
        print('Enter 1, 2, or 3!')


button4 = Button(root, text='Do ordinary sorting', command=ordinary_sorting).pack()

root.mainloop()
