def main():
    response = input("Enter word: ")
    stripped = remove_vowels(response)
    print(f"Stripped: {stripped}")

def remove_vowels(word):
    word = word.lower()
    vowels = "aeiou"
    stripped = word.translate({ord(v): None for v in vowels})
    return stripped


if __name__ == "__main__":
    main()