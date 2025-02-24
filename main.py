"""Main (driver) code """

from app import App
import sys


def calculate_and_print(argv: list[str]) -> float | int:
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
        app=App()
        app.start()
        app.execute_command(argv[-1], argv[:-1])
    except ZeroDivisionError: 
        print("An error occurred: Cannot divide by zero")
    except KeyError:
        print("Unknown operation:", argv[-1])
    except ValueError:
        print(f"Invalid number input: {argv[0]} or {argv[1]} is not a valid number.")

if __name__ == "__main__":
    calculate_and_print(sys.argv[1:])  # pragma: no cover
