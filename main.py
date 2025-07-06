import os
n = 0
tasks = {}

path = (os.path.dirname(os.path.abspath(__file__))+"\list.txt")

#loading saved tasks
if os.stat(path).st_size == 0:
    tasks = {}
else:
    with open(path, "r") as f:
        for i in f.readlines():
            n+=1
            task = i.split()
            tasks.update({f"task {n}" : " ".join(task[0].split("-")), f"done {n}" : task[1]})

def saveToFile(dicti):
    if len(dicti) != 0:
            with open(path, "w") as f:
                for i in range(int(len(dicti)/2)):
                    f.write(f"{'-'.join((dicti.get(f'task {i+1}')).split(' '))} {dicti.get(f'done {i+1}')}\n")
                print("tasks saved successfuly")
    else:
        print("no tasks to be saved")

#main loop
while True:
    print("\n1. add task \n2. view tasks \n3. mark task complete \n4. delete task \n5. save to computer\n6. exit\n")
    try:
       choice = int(input("choice: "))
    except:
        print("invalid input")
        continue
    
    #adding tasks
    if choice == 1:
        n += 1
        task = input("task: ")
        tasks.update({f"task {n}" : task, f"done {n}" : "no"})
        saveToFile(tasks)
    
    #viewing tasks
    if choice == 2:
        if len(tasks) != 0:
            for i in range(int(len(tasks)/2)):
                print(f"{i+1}. {tasks.get(f'task {i+1}')} , Done: {tasks.get(f'done {i+1}')}")
        else:
            print("no tasks to be viewed")

    #editing tasks
    if choice == 3:
        if len(tasks) == 0:
            print("no tasks to be changed")
        if len(tasks) != 0:
            taskNum = int(input("enter the task number: "))
            if taskNum <= n:
                tasks[f"done {taskNum}"] = "yes"
            else:
                print("task does not exist.")
    
    #deleting tasks
    if choice == 4:
        if len(tasks) == 0:
            print("no tasks to be deleted")
        if len(tasks) != 0:
            taskNum = int(input("enter the task number: "))
            if taskNum <= n:
                confirm = input(f"are you sure you want to delete the task {tasks[f'task {taskNum}']}? ")
                if confirm == "yes":
                    tasks.pop(f"task {taskNum}")
                    tasks.pop(f"done {taskNum}")
                    print("task deleted successfuly")
            else:
                print("task does not exist.")

    #Saving tasks
    if choice == 5:
        saveToFile(tasks)
    
    #exiting
    if choice == 6:
        saveToFile(tasks)
        break