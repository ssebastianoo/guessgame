import time, os

if os.name == "nt":
    clear = "cls"

else:
    clear = "clear"

def write(text):
    result = ""
    for letter in text:
        time.sleep(0.03)
        os.system(clear)
        result += letter
        print(result)

write("hello, I'm gonna try guess the number you're thinking! Give me a range using this format: 0 - 100 or 40 - 65")

end = False
while not end:
    range = input()
    if " " in range:
        range = range.split(" - ")

    else:
        range = range.split("-")

    if len(range) != 2:
        write("not a valid format! Give me a range using this format: 0 - 100 or 40 - 65")
        end = False

    else:
        end_ = []
        for num in range:
            try:
                num = int(num)
            except ValueError:
                write("not a valid format! Give me a range using this format: 0 - 100 or 40 - 65")
                end_.append(1)
            else:
                end_.append(0)

        if 1 in end_:
            end = False

        else:
            end = True

rangeA = int(range[0])
rangeB = int(range[1])

if rangeA > rangeB:
    a = rangeA
    b = rangeB
    rangeA = b
    rangeB = a

passed = False

while not passed:
    write(f'is your number {round((rangeB + rangeA) / 2)}?\n\nreply with\nA (yes)\nB (major)\nC (minor)')
    guess = input()

    if guess.lower() not in ["a", "b", "c"]:
        write(f"{guess} is not a valid option")
        passed = False 

    else:
        if guess.lower() in ["a", "yes"]:
            write("oh, wow, I won!")
            passed = True
            break

        elif guess.lower() in ["b", "major"]:
            rangeA = (rangeB + rangeA) / 2
            passed = False

        elif guess.lower() in ["c", "minor"]:
            rangeB = (rangeB + rangeA) / 2    