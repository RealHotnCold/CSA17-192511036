from itertools import permutations

letters = "SENDMORY"

def word_value(word, values):
    number = 0
    for ch in word:
        number = number * 10 + values[ch]
    return number

for digits in permutations(range(10), 8):
    values = dict(zip(letters, digits))

    if values["S"] == 0 or values["M"] == 0:
        continue

    send = word_value("SEND", values)
    more = word_value("MORE", values)
    money = word_value("MONEY", values)

    if send + more == money:
        print("Solution found:")
        for letter in letters:
            print(letter, "=", values[letter])

        print("\nSEND =", send)
        print("MORE =", more)
        print("MONEY =", money)
        break
else:
    print("No solution found.")
