# Write your solution here
editors = {
    "emacs" : "not good",
    "vim" : "not good",
    "word" : "awful",
    "notepad" : "awful",
    "atom" : "not good",
    "visual studio code" : "an excellent choice!",
}

while True:
    editor = input("Editor: ").lower()
    if editor != "visual studio code":
        print(editors[editor])
    else:
        print(editors[editor])
        break
