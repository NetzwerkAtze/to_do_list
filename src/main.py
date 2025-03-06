from task_manager import *
import json

def main():

    command_list = ["add_task", "display_tasks", "mark_task_as_done", "delete_task"]
    exit_choice = len(command_list) + 1

    print("Welcome to To-Do-List!\n")

    while True:
        print_menu()
        try:
            choice = int(input("What would you like to do?\n"))

            if choice == exit_choice:
                confirmation = ""
                while confirmation != "y" and confirmation != "n":
                    confirmation = input("Save Task list? (y/n)")
                if confirmation == "y":
                    save_task_list(task_list)

                confirmation = ""
                while confirmation != "y" and confirmation != "n":
                    confirmation = input("End program? (y/n)")
                if confirmation == "y":
                    break
                continue

            func_info = command_mapping[command_list[choice-1]]
            func = func_info["function"]
            fixed_params = func_info["fixed_params"]
            user_params = func_info["user_params"]

            args = {}
            for param in user_params:
                print(f"{param["help"]}\n")

                while True:
                    user_input = input(f"{param["name"]}: ")
                    if param["type"] == str:
                        user_input = user_input.capitalize()

                    if param["type"] == int:
                        try:
                            user_input = int(user_input)
                        except ValueError:
                            print("\nPlease enter a number.\n")
                            continue

                    if "valid_values" in param and user_input not in param["valid_values"]:
                        print("\nPlease enter a valid value.\n")
                        continue

                    break   

                args[param["name"]] = user_input
            
            func(*fixed_params, **args)
            input("Press Enter to continue...")

        except (NameError, IndexError, ValueError):
            print("\ninvalid input\n")

if __name__ == "__main__":
    main()