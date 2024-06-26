tasks = [] 
deleted_tasks = [] 
all_deleted_tasks=[]

def add_task():
   global tasks, deleted_tasks
   task_name = input("Please enter the name of the task: ")  
  
   if deleted_tasks:
       task_index = min(deleted_tasks)
       deleted_tasks.remove(task_index) 
   else:
       task_index = len(tasks) + 1 
  
   task = {"Sequence Number": task_index, "Name": task_name, "Status": "Pending"}
   tasks.append(task) 
   print(f"Task '{task_name}' successfully added. Sequence number: {task_index}")
   

def complete_task():
   global tasks
   task_index = int(input("Please enter the number of the task to complete: "))
   for task in tasks:
       if task["Sequence Number"] == task_index:
           task["Status"] = "Successful"
           print(f"Task '{task['Name']}' successfully completed.")
           return
   print("No task found with the specified sequence number.")


def delete_task():
   global tasks, deleted_tasks, all_deleted_tasks
   task_index = int(input("Please enter the number of the task to delete: "))
   for task in tasks:
       if task["Sequence Number"] == task_index:
           deleted_tasks.append(task_index)
           all_deleted_tasks.append(task)
           tasks.remove(task)
           print(f"Task '{task['Name']}' successfully deleted. Sequence number: {task_index}")
           return
   print("No task found with the specified sequence number.")


def list_completed_tasks():
   completed_tasks = [task for task in tasks if task["Status"] == "Successful"]
   if completed_tasks:
       print("Succesfuly Completed Tasks:")
       for task in completed_tasks:
           print(f"{task['Sequence Number']}. {task['Name']}")
   else:
       print("There are no completed tasks.")


def list_all_tasks():
   sorted_tasks = sorted(tasks, key=lambda x: x["Sequence Number"])
   print("All Current Tasks:")
   for task in sorted_tasks:
       print(f"{task['Sequence Number']} - {task['Name']} - {task['Status']}")
   print("\nDeleted Tasks:")
   for task in all_deleted_tasks:
       print(f"{task['Sequence Number']}. {task['Name']}")


while True:
   print("\nTask Manager Menu:")
   print("1. Add a New Task")
   print("2. Complete a Task")
   print("3. Delete a Task")
   print("4. List Completed Tasks")
   print("5. List All Tasks")
   print("6. Exit")


   choice = input("Please enter one of the number above): ")

   if choice == "1":
       add_task()
   elif choice == "2":
       complete_task()
   elif choice == "3":
       delete_task()
   elif choice == "4":
       list_completed_tasks()
   elif choice == "5":
       list_all_tasks()
   elif choice == "6":
       print("Exiting the program...")
       break
   else:
       print("Invalid choice, please try again.")
