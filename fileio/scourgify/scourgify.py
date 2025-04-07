import csv
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <filename.csv> <filename.csv>")
        sys.exit(1)

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        print("Usage: python scourgify.py <filename.csv> <filename.csv>")
        sys.exit(1)

    table = []

    try:
        with open(sys.argv[1], "r", newline='') as file:
            reader = csv.reader(file)
            iterreader = iter(reader)
            next(iterreader)
            for row in iterreader:
                last, first = row[0].split(", ")
                house = row[1]
                table.append([first, last, house])
    except OSError:
        print("File not found")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    table.insert(0, ["first","last","house"])

    try:
        with open(sys.argv[2], "w", newline='') as newfile:
            writer = csv.writer(newfile)
            writer.writerows(table)
    except OSError as e:
        print(f"Something went wrong: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()