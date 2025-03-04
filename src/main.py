from task_manager import *


def main():

    command_list = ["add_task", "display_tasks", "mark_task_as_done", "delete_task", "end_program"]
    running = True

    print("Welcome to To-Do-List!\n")

    while running == True:
        print_menu()
        try:
            choice = int(input("What would you like to do?\n"))-1
            
            func_info = command_mapping[command_list[choice]]
            func = func_info["function"]
            fixed_params = func_info["fixed_params"]
            user_params = func_info["user_params"]

            args = {}
            for param in user_params:
                args[param] = input(f"Please input {param}: ")
            
            func(*fixed_params, **args)

            print(task_list)

        except (NameError, IndexError, ValueError):
            print("\ninvalid input\n")

if __name__ == "__main__":
    main()