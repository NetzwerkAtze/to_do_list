from datetime import datetime

task_list = []
task_time = datetime.now()
formatted_task_time = task_time.strftime("%Y-%m-%d %H:%M:%S")

def print_menu():
    print("1. add task\n2. display tasks\n3. mark task as done\n4. delete task\n5. end\n")

def add_task(task_list, formatted_task_time, task_name, task_priority):
    new_task = {"name": task_name, "priority": task_priority, "time": formatted_task_time}
    task_list.append(new_task)

def display_tasks():
    print()

def mark_task_as_done():
    print()

def delete_task():
    print()

def end_program():
    running = False
    return running

command_mapping = {
    "add_task": {
        "function": add_task, 
        "fixed_params": [task_list, formatted_task_time],
        "user_params": ["task_name", "task_priority"] 
        }
    }