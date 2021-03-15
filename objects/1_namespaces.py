"""Demo namespaces."""


global_x = 1
x = 1


def function():

    function_x = 3
    x = 3

    print(f"Function: global_x equals {global_x}.")
    print(f"Function: x equals {x}.")

    def inner():
        print(f"Inner: global_x equals {global_x}.")
        print(f"Inner: function_x equals {function_x}.")
        print(f"Inner: x equals {x}.")

    inner() #bp


def main():

    x = 2

    print(f"Main: global_x equals {global_x}.")
    print(f"Main: x equals {x}.")

    function() #bp


if __name__ == "__main__":

    print(f"Global: global_x equals {global_x}.")
    print(f"Global: x equals {x}.")

    main() #bp