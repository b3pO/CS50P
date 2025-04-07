import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py <filename.py>")
        sys.exit(1)
    
    if not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)

    try:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
    except OSError:
        print("File does not exist")
        sys.exit(1)
    
    trimmed = trim_lines(lines)
    
    print(f"Lines of code: {len(trimmed)}")


def trim_lines(lines):
    """Trim white space and return a new list excluding blank lines and comments."""
    trimmed = []

    for line in lines:
        line = line.strip()
        if line != '' and line.startswith("#") == False:
            trimmed.append(line)
    return trimmed


if __name__ == "__main__":
    main()