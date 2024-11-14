import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <your_argument>")
        sys.exit(1)

    argument = sys.argv[1]
    print(argument)

if __name__ == "__main__":
    main()