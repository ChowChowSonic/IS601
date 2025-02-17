"""Main (driver) code """

from calculator import Calculator
import sys


def calculate_and_print(argv: str, arg2: str, op: str) -> float | int:
    """Originally, this function was able to take in a mathematical equation 
        (for example: 1.0+3*6) from either a pipe or split across sys.argv; 
        However, I had to rewrite this to be compliant with our class's output requirements"""
    # if len(argv) == 0:
    #     ctr = 0
    #     x = " "
    #     while x != "":
    #         try:
    #             x = input("!" + str(ctr) + ": ")
    #         except EOFError:
    #             # Useful for when we pipe something as input rather than manually inputting something
    #             break
    #         ctr += 1
    #         if x != "":
    #             Calculator._print_result(x)
    # else:
    try: 
        print("The result of",argv,op,arg2,"is equal to",Calculator.get_result(argv, arg2, op)) 
    except ZeroDivisionError: 
        print("An error occurred: Cannot divide by zero")
    except KeyError:
        print("Unknown operation:", op)
    except ValueError:
        print(f"Invalid number input: {argv} or {arg2} is not a valid number.")

if __name__ == "__main__":
    calculate_and_print(sys.argv[1], sys.argv[2], sys.argv[3])  # pragma: no cover
