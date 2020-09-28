import os
import sys

import calc



# get value from user and return an integer number
def get_number():
    try:
        return int(input("Enter an integer number: "))
    except ValueError:
        return None

def menu():
    items = [
        "1) Addition",
        "2) Substraction",
        "3) Multipication",
        "4) Division",
        "5) Quit"
    ]

    for item in items:
        print(item)
        
    return input("Choose from menu pls: ")


def main():
    operations = {
        "1": calc.add,
        "2": calc.minus,
        "3": calc.mul,
        "4": calc.div,
    }
    
    op_symbols = {
        "1": "+",
        "2": "-",
        "3": "*",
        "4": "/",
    }
    
    while True:
        os.system("clear")
        response = menu()
        if operations.get(response) is not None:
            num1 = get_number()
            num2 = get_number()
            if num1 is not None  and num2 is not None:
                res = operations[response](num1, num2)
                print(f"{num1} {op_symbols[response]} {num2} = {res}")
            else:
                print("Invalid number. You should enter and integer number.")
        elif response == '5':
            sys.exit()
        else:
            print("Invalid choose!")
            
        input("Press any key to back to menu ...")
        
        
if __name__ == "__main__":
    main()
