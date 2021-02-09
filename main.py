"""Morse code to english translator and vis versa that allows translating and saving to a file. You also have options to
 upload and translate a file. Words are separated by spaces and morse will be separated by forward slashes."""

from os import path
import sys

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}


def english_to_morse(inp):
    """Takes a string, converts to Morse code, returns converted string

    :param inp:
        (string): The text that is to be converted to morse

    :return:
        (string): The morse
    """
    morse = ''
    for letter in inp.upper():
        if letter in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[letter] + ' '
        else:
            morse += letter + ' '
    return morse


def morse_to_english(inp):
    """Takes string of Morse code separated by spaces,converts to list, converts to English, returns a string

    :param inp:
        (string): The text that is to be converted to english

    :return:
        (string): The english
    """
    english = ''
    for character in inp.split():
        if character in MORSE_CODE_DICT.values():
            for letter, morse_value in MORSE_CODE_DICT.items():
                if character == morse_value:
                    english += letter
        else:
            english += character
    return english


def print_options(options):
    for option in options:
        print(option)


def convert_message_and_save(message, convert):
    """
    prints translated message and ask if you want to save. If yes saves to provide file path.

    :param message:
        (string): ask for type of message
    :param convert:
        (function_name): how to translate
    :return:
        (void)
    """
    inp = input(message)
    print(convert(inp))
    print()
    while True:
        inp1 = input("Would you like to save to file: ")
        if inp1.upper() == 'Y':
            file_path = input("Enter file path: ")
            if path.exists(file_path):
                if path.isfile(file_path):
                    try:
                        write_to_file(file_path, convert(inp))
                        break
                    except FileNotFoundError:
                        print('File Not Found')
                        print()
                    except TypeError:
                        print(TypeError)
        if inp1.upper() == 'N':
            break
        else:
            print('Enter Y or N')


def check_if_quitting(inp):
    if inp.upper() == 'QUIT':
        sys.exit()


def read_from_file_and_convert(file_path, convert):
    with open(file_path, 'r') as f:
        text = f.read()
        print(convert(text))
        print()


def write_to_file(file_path, text):
    with open(file_path, 'w') as f:
        f.write(text)
        print()


def main():
    while True:
        options = ['1. Type a message to convert to morse',
                   '2. Type morse to convert to english',
                   '3. Load a file to convert to morse',
                   '4. Load a file to convert to english',
                   '5. Quit']
        print_options(options)
        inp = input("Enter a number: ")
        check_if_quitting(inp)
        try:
            if int(inp) not in range(1, len(options) + 1):
                print("Invalid input!\n")
                continue
            if int(inp) == 1:
                convert_message_and_save("Type a english message: ", english_to_morse)
                continue
            if int(inp) == 2:
                convert_message_and_save("Type a morse message: ", morse_to_english)
                continue
            if int(inp) == 3:
                file_path = input("Enter file path: ")
                try:
                    read_from_file_and_convert(file_path, english_to_morse)
                    continue
                except FileNotFoundError:
                    print('File Not Found')
                    print()
            if int(inp) == 4:
                file_path = input("Enter file path: ")
                try:
                    read_from_file_and_convert(file_path, morse_to_english)
                    continue
                except FileNotFoundError:
                    print('File Not Found')
                    print()
            if int(inp) == 5:
                sys.exit()
        except ValueError:
            print("Invalid input!\n")


if __name__ == "__main__":
    main()
# check to see if file is created

# create new file. if file exist create new but add (x) to name, incrementing x
