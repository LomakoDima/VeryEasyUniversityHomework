letter = input("Enter a letter: ").lower()

if len(letter) != 1 or not letter.isalpha() or not letter.isascii():
    print("Please enter one English letter")
elif letter in "aeiou":
    print("Vowel")
else:
    print("Consonant")
