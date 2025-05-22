# example_module.py
def greet(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    import sys
    greet(sys.argv[1])