from List import LinkedList, Queue, Stack

choice = input("[1]- Stack\n[2]- Queue\n[3]- LinkedList\n")

user_input = list(input("list= "))
for i in range(len(user_input)):
    user_input[i] = int(user_input[i])


def input_stack():

    if choice:
        methods = input("[1]- pop\n[2]- push\n[3]- show\n[4]- exit\n")
        stack = Stack(user_input)
        if methods == '4':
            exit()
        if methods == '2':
            data = int(input("data= "))

            print(f"Stack= {stack.push(data)}")


        else:
            if methods == "1":
                print(f"Stack= {stack.pop_the_first_el()}")

            elif methods == "3":
                stack.show()
            elif methods == "4":
                stack.exit()



def input_queue():

    if choice:
        methods = input("[1]- enqueue\n[2]- dequeue\n[3]- show\n[4]- exit\n")

        if methods == '4':
            return exit()

        if methods == '1':
            data = int(input("data= "))
            queue = Queue(user_input, data)
            if data:
                    print(f"Queue= {queue.enqueue()}")
        else:
                queue = Queue(user_input)
                if methods == "2":
                    print(f"Queue= {queue.dequeue()}")
                elif methods == "3":
                   queue.show()


def linkedList_input():

    if choice:
        methods = input("[1]- add_begin\n[2]- add_end\n[3]- del_begin\n[4]- del_end\n[5]- add_mid\n[6]- del_mid\n[7]- search\n[8]- show\n[9]- exit\n")

        if methods == '9':
                exit()
        if methods == '3' or methods == '4' or methods == '5' or methods == '8' or methods == '9':
            linked_list = LinkedList(user_input)
            if methods == "3":
                print(f"LinkedList= {linked_list.del_begin()}")

            elif methods == "4":
                print(f"LinkedList= {linked_list.del_end()}")
            elif methods == "5":
                el_add = int(input("Enter an element to add: "))
                el_after = int(input("Enter an element that will be before the element: "))
                print(f"LinkedList= {linked_list.add_mid(el_add, el_after)}")
            elif methods == "8":
                linked_list.show()

            elif methods == "9":
                exit()

        else:
            data = int(input("data= "))
            linkedList = LinkedList(user_input, data)
            if data:
                if methods == "1":
                    print(f"LinkedList= {linkedList.add_begin()}")

                elif methods == "2":
                    print(f"LinkedList= {linkedList.add_end()}")

                elif methods == "6":
                    el_after = int(input("Enter an element that is before the element: "))
                    print(f"LinkedList= {linkedList.del_mid()}")
                elif methods == "7":
                    linkedList.search()

                elif methods == "8":
                    linkedList.show()

                elif methods == "9":
                    exit()


while True:
    if choice == "1":
        print("~~~~Stack~~~~")
        input_stack()
    elif choice == "2":
        print("~~~~Queue~~~~")
        input_queue()
    elif choice == "3":
        print("~~~~LinkedList~~~~")
        linkedList_input()

