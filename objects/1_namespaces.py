"""Demo namespaces, run through debugger with breakpoints at #bp comments."""


global_x = 1
x = 1


def main():

    main_x = 2
    x = 2

    print(f"Main: global_x equals {global_x}.")
    print(f"Main: x equals {x}.")

    def inner():
        x = 3

        print(f"Inner: global_x equals {global_x}.")
        print(f"Inner: main_x equals {main_x}.")
        print(f"Inner: x equals {x}.")

    inner()  # breakpoint


if __name__ == "__main__":

    print(f"Global: global_x equals {global_x}.")
    print(f"Global: x equals {x}.")

    main()  # breakpoint

