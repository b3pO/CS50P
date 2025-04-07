import csv
import sys
from tabulate import tabulate


def main():
    if len(sys.argv) != 2:
        print("Usage: python lines.py <filename.csv>")
        sys.exit(1)
    
    if not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)

    table = table_list(sys.argv[1])
    print(tabulate(table, headers="firstrow", tablefmt="grid"))

def table_list(file):
    table = []

    try:
        with open(file, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                table += [row]
    except OSError:
        print("File does not exist")
        sys.exit(1)

    return table


if __name__ == "__main__":
    main()

