# an empty list is needed

todo_list = []

# first functionality
# adding to the list

def add():
    # what to be added
    item = input("enter a todo item🔕: ")
    todo_list.append(item)
    print("successfully added todo item")

# delete todo

def delete():
    if len(todo_list) == 0:
        print("no todo items❌")
    else:
        for index, item in enumerate(todo_list):
            # print("to do items ✅\n")
            print(f"{index+1}. {item}")
    item_to_delete = int(input("enter item number to remove"))-1
    if item_to_delete<0 or item_to_delete>=len(todo_list):
        print("out of range________________________________")
    else:
        del todo_list[item_to_delete]
        print("item successfully deleted❌")


# update

def update():
    if len(todo_list) == 0:
        print("no todo items❌")
    else:
        for index, item in enumerate(todo_list):
            # print("to do items ✅\n")
            print(f"{index+1}. {item}")
    item_to_update = int(input("enter item number to update"))-1
    if item_to_update<0 or item_to_update>=len(todo_list):
        print("out of range________________________________")
    else:
        new_item= input("enter new item")
        todo_list[item_to_update]=new_item
      
        print("item successfully updated.✅")

# view list

def view():
    if len(todo_list) == 0:
        print("no todo items❌")
    else:
        # show items inside list
        for index,item in enumerate(todo_list):
            print(f'{index+1}. {item}')

while True:
    print("My to do app\n")
    print("1. Add to do")
    print("2. Remove from to do")
    print("3. Update to do")
    print("4. View to do")
    print("5. exit")
    choice= input("enter activity number: ")
    if choice =="1":
        add()
    elif choice=="2":
        delete()
    elif choice=="3":
        update()
    elif choice=="4":
        view()
    elif choice=="5":
        print("Thanks for using this app.")
        break
    else:
        print("let your activity number be in the given activity numbers.")
        

