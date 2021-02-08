"""morse code translator that allows translating and encrypting a file and creating a new one with
the opposite. letters are separated by spaces and words will be separated by forward slashes for the morse version"""
from os import path
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
    """takes a string, converts to Morse code, returns converted string"""
    morse = ''
    for letter in inp.upper():
        if letter in MORSE_CODE_DICT:
            morse += MORSE_CODE_DICT[letter] + ' '
        else:
            morse += letter + ' '
    return morse


def morse_to_english(inp):
    """takes list of Morse code separated by spaces, converts to English, returns a string"""
    english = ''
    for character in inp.split():
        if character in MORSE_CODE_DICT.values():
            for letter, morse_value in MORSE_CODE_DICT.items():
                if character == morse_value:
                    english += letter
        else:
            english += character
    return english


def main():
    while True:
        options = ['1. Type a message to convert to morse',
                   '2. Type morse to convert to english',
                   '3. Load a file to convert to morse',
                   '4. Load a file to convert to english',
                   '5. Quit']
        for choices in options:
            print(choices)
        inp = input("Enter a number: ")
        if inp.upper() == 'QUIT':
            break
        try:
            if int(inp) in range(1, len(options) + 1):
                if int(inp) == 1:
                    inp = input("Type a english message: ")
                    print(english_to_morse(inp))
                    print()
                    while True:
                        inp1 = input("Would you like to save to file: ")
                        if inp1.upper() == 'Y':
                            inp2 = input("Enter file path: ")
                            if path.exists(inp2):
                                if path.isfile(inp2):
                                    try:
                                        with open(inp2, 'w') as f:
                                            f.write(inp)
                                            print()
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
                    continue
                if int(inp) == 2:
                    inp = input("Type a morse message: ")
                    print(morse_to_english(inp))
                    print()
                    while True:
                        inp1 = input("Would you like to save to file: ")
                        if inp1.upper() == 'Y':
                            inp2 = input("Enter file path: ")
                            if path.exists(inp2):
                                if path.isfile(inp2):
                                    try:
                                        with open(inp2, 'w') as f:
                                            f.write(inp)
                                            print()
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
                    continue
                if int(inp) == 3:
                    inp = input("Enter file path: ")
                    try:
                        with open(inp, 'r') as f:
                            inp = f.read()
                            print(english_to_morse(inp))
                            print()
                        continue
                    except FileNotFoundError:
                        print('File Not Found')
                        print()
                if int(inp) == 4:
                    inp = input("Enter file path: ")
                    try:
                        with open(inp, 'r') as f:
                            inp = f.read()
                            print(morse_to_english(inp))
                            print()
                        continue
                    except FileNotFoundError:
                        print('File Not Found')
                        print()
                if int(inp) == 5:
                    break
            else:
                print("Invalid input!\n")
        except ValueError:
            print("Invalid input!\n")


if __name__ == "__main__":
    main()
# check to see if file is created

# create new file. if file exist create new but add (x) to name, incrementing x
