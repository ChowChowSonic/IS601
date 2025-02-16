from calculator import Calculator
import sys


@staticmethod
def calculate_and_print(argv: list[str]) -> float | int:
    if len(argv) == 0:
        ctr = 0
        x = " "
        while x != "":
            try:
                x = input("!" + str(ctr) + ": ")
            except EOFError:
                # Useful for when we pipe something as input rather than manually inputting something
                break
            ctr += 1
            if x != "":
                Calculator._print_result(x)
    else:
        return Calculator._print_result(*argv)


if __name__ == "__main__":
    calculate_and_print(sys.argv[1:])
