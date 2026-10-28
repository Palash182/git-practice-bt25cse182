import sys

def main():
    data = sys.stdin.read().split()
    if len(data) >= 2:
        a, b = int(data[0]), int(data[1])
        print(f"Sum of {a} and {b} is: {a + b}")
    else:
        print("Please provide two numbers.")

if __name__ == "__main__":
    main()
