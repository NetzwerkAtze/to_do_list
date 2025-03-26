from datetime import datetime
import json

try: 
    with open("/home/netzwerk_atze/python-projects/to_do_list/data/tasks.json", "r") as file:
        task_list = json.load(file)
except FileNotFoundError:
    task_list = []

task_time = datetime.now()
formatted_task_time = task_time.strftime("%Y-%m-%d %H:%M:%S")
task_priority_list = ("high", "medium" ,"low")

def print_menu():
    print("\nMain Menu\n\n1. add task\n2. display tasks\n3. mark task as done\n4. delete task\n5. save & end\n")

def save_task_list(task_list):
    with open("/home/netzwerk_atze/python-projects/to_do_list/data/tasks.json", "w") as file:
        json.dump(task_list, file, indent=4)
    
def add_task(task_list, formatted_task_time, task_priority_list, task_name, task_priority):
    for task in task_list:
        if task["name"] == task_name.capitalize():
            print("Task is already existing.")
            break
    else:
        new_task = {"name": task_name, "priority": task_priority_list[task_priority-1], "time": formatted_task_time, "done": False}
        task_list.append(new_task)
        print("Task added.")

def display_tasks(task_list):
    if not task_list:
        print("The task list is empty!")
    else:
        print("\nTask list:")
        for task in task_list:
            task_done = "[ ]"
            if task["done"] == True:
                task_done = "[x]"
            print(f"name: {task["name"]}    priority: {task["priority"]}    time: {task["time"]}    done: {task_done}\n")

def mark_task_as_done(task_list, task_name):
    for task in task_list:
        if task["name"].capitalize() == task_name.capitalize():
            if task["done"]:  
                print("Task already marked as done.")
            else:
                task["done"] = True
                print("\nTask marked as done.\n")
            return  

    print("Task not found.")

def delete_task(task_list, task_name):
    original_length = len(task_list)
    
    task_list[:] = [task for task in task_list if task["name"].capitalize() != task_name.capitalize()]

    if len(task_list) == original_length:
        print("Task not found.")
    else:
        print("\nTask deleted.\n")

command_mapping = {
    "add_task": {
        "function": add_task, 
        "fixed_params": [task_list, formatted_task_time, task_priority_list],
        "user_params": [{"name": "task_name", "type": str, "help": "Enter the name of the task"}, {"name": "task_priority", "type": int, "valid_values": (1, 2, 3), "help":"\nchoose a priority:\n\n 1. high\n 2. medium\n 3. low"}] 
        },
    "display_tasks": {
        "function": display_tasks, 
        "fixed_params": [task_list],
        "user_params": [] 
        },
    "mark_task_as_done": {
        "function": mark_task_as_done,
        "fixed_params": [task_list],
        "user_params": [{"name": "task_name", "type": str, "help": "Enter the name of the task"}]
        },
    "delete_task": {
        "function": delete_task,
        "fixed_params": [task_list],
        "user_params": [{"name": "task_name", "type": str, "help": "Enter the name of the task"}] 
        }
    }