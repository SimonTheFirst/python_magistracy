import re

if __name__ == "__main__":
    pattern = r'\b.*([0-9]).*(\1).*\b'
    word = input("Enter a word: ")
    if bool(re.match(pattern, word)):
        print("Word has recurring digits")
    else:
        print("Word doesn't have recurring digits")

