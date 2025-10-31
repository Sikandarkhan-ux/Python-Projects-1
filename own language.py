

def translate (word):
    translation = ""
    for letter in word:
        if letter in "AEIOU aeiou":
            translation = translation + "s"
        else :
            translation = translation + letter

    return translation





print(translate(input("Enter a word: ")))