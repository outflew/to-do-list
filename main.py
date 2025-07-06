import os
n = 0
tasks = {}
if os.stat("C:/to-do-list/to-do-list/list.txt").st_size == 0:
    tasks = {}
else:
    with open("C:/to-do-list/to-do-list/list.txt", "r") as f:
        for i in f.readlines():
            n+=1
            task = i.split()
            tasks.update({f"task {n}" : " ".join(task[0].split("-")), f"done {n}" : task[1]})

while True:
    print("\n1. add task \n2. view tasks \n3. mark task complete \n4. delete task \n5. save to computer\n6. exit\n")
    try:
       choice = int(input("choice: "))
    except:
        print("invalid input")
        continue

    if choice == 1:
        n += 1
        task = input("task: ")
        tasks.update({f"task {n}" : task, f"done {n}" : "no"})
    
    if choice == 2:
        if len(tasks) != 0:
            for i in range(int(len(tasks)/2)):
                print(f"{i+1}. {tasks.get(f'task {i+1}')} , Done: {tasks.get(f'done {i+1}')}")
        else:
            print("no tasks to be viewed")

    if choice == 3:
        if len(tasks) == 0:
            print("no tasks to be viewed")
        if len(tasks) != 0:
            taskNum = int(input("enter the task number: "))
            if taskNum <= n:
                tasks[f"done {taskNum}"] = "yes"
            else:
                print("task does not exist.")

    if choice == 4:
        if len(tasks) == 0:
            print("no tasks to be viewed")
        if len(tasks) != 0:
            taskNum = int(input("enter the task number: "))
            if taskNum <= n:
                confirm = input(f"are you sure you want to delete task {taskNum}? ")
                if confirm == "yes":
                    tasks.pop(f"task {taskNum}")
                    tasks.pop(f"done {taskNum}")
            else:
                print("task does not exist.")

    if choice == 5:
        if len(tasks) != 0:
            with open("C:/to-do-list/to-do-list/list.txt", "w") as f:
                for i in range(int(len(tasks)/2)):
                    f.write(f"{'-'.join((tasks.get(f'task {i+1}')).split(' '))} {tasks.get(f'done {i+1}')}\n")
                print("tasks saved successfuly")
        else:
            print("no tasks to be saved")

    if choice == 6:
        if len(tasks) != 0:
            with open("C:/to-do-list/to-do-list/list.txt", "w") as f:
                for i in range(int(len(tasks)/2)):
                    f.write(f"{'-'.join((tasks.get(f'task {i+1}')).split(' '))} {tasks.get(f'done {i+1}')}\n")
                print("tasks saved successfuly")
        break