
# Available letter variables
first_slot_letters = []
second_slot_letters = []
third_slot_letters = []
fourth_slot_letters = []
fifth_slot_letters = []

# Command List
cmds = '''
help - List all commands
exit - Exit the program
letters - Enter the valid letters for the wordle
required - enter the required letters for the wordle
solve - solve the wordle
'''

def stringifyList(list):
    string = ""
    for item in list:
                string += f"{item}, "
    return string[:-2]

def validLetter(letter, list):
    if len(letter) == 1 and letter.isalpha() and letter not in list:
        return True
    else:
        return False

def validList(letter, list):
    if letter.lower() == "done" and len(list) > 0:
        return True
    else:
        return False

def enterLetters(string_index, list):
    list.clear()
    while True:
                letter = input(f"Enter the {string_index} letter possibilities (type done when all possible answers have been entered): ")
                if validList(letter, list):
                    break
                else:
                    if validLetter(letter, list):
                        list.append(letter)
                        print(stringifyList(list))
                    else:
                        print("That is not a valid letter or it is already in the list!")
    return list

try:
  while True:
    command = input("Enter a command: ")
    match command.lower():
        case "help":
            print(cmds)
        case "letters":
            enterLetters("first", first_slot_letters)
            enterLetters("second", second_slot_letters)
            enterLetters("third", third_slot_letters)
            enterLetters("fourth", fourth_slot_letters)
            enterLetters("fifth", fifth_slot_letters)
        case "required":
            required = []
            while True:
                letter = input("Enter any required letters (green or amber): ")
                if letter.lower() == "done":
                    break
                else:
                    if len(letter) == 1 and letter.isalpha() and letter not in required:
                        required.append(letter)
                    else:
                        print("That is not a valid letter or it is already in the list!")
        case "solve":
            generated_words = []
            for l1 in first_slot_letters:
                for l2 in second_slot_letters:
                    for l3 in third_slot_letters:
                        for l4 in fourth_slot_letters:
                            for l5 in fifth_slot_letters:
                                word = f"{l1}{l2}{l3}{l4}{l5}"
                                print(word)
                                generated_words.append(word)
            accepted_words = []

            with open("words.txt") as f:
                words = f.read().lower()
            for word in generated_words:
                required_in_word = 0
                for letter in required:
                    if letter in word:
                        required_in_word += 1
                if required_in_word == len(required):
                    if word in words:
                        accepted_words.append(word)
            print(f"The wordle could be {stringifyList(accepted_words)}.")
                
        case "exit":
            exit()
        case unknown_command:
            print("Command not recognised, try 'help'")
except KeyboardInterrupt:
    print("\nExiting...")
    exit()

