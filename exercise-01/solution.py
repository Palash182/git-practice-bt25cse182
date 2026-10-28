import sys

def main():
    name = sys.stdin.read().strip()
    if name:
        print(f"Hello, {name}! Exercise 01 completed successfully.")
    else:
        print("Hello, World! Exercise 01 completed successfully.")

if __name__ == "__main__":
    main()
