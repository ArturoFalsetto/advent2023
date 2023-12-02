# strings = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]
strings = [
    "oneabctwo",
    "pqrthreestueightvwx",
    "aonebtwocthreedfoutefivef",
    "trebsevenuchet",
]

wordstrangs = [
    "two1nine",
    "eightwothree",
    "abcone2threexyz",
    "xtwone3four",
    "4nineeightseven2",
    "zoneight234",
    "7pqrstsixteen",
]


def read_input(path):
    with open(path, "r") as f:
        strings = f.read().splitlines()
    return strings


def numb(string):
    first = None
    last = None
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
    return int(digits[0] + digits[-1])


def numb_with_english(string):
    english_digits = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    digits = []
    for i, char in enumerate(string):
        for eng_digit, digit in english_digits.items():
            if string[i:].startswith(digit):
                digits.append(digit)
            if string[i:].startswith(eng_digit):
                digits.append(digit)
    return int(digits[0] + digits[-1])


if __name__ == "__main__":
    wordstrangs = read_input("input_data.txt")
    wordless_calibrations = list(map(numb, wordstrangs))
    wordy_calibrations = list(map(numb_with_english, wordstrangs))
    print("SUM (WITHOUT WORDS):", sum(wordless_calibrations))
    print("SUM (WITH WORDS):", sum(wordy_calibrations))
