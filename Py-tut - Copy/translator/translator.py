# cats lang.
# vowels -> m

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "m"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))
