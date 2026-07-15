
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
'''

while True:
    command = input("Enter a command: ")
    match command.lower():
        case "help":
            print(cmds)
        case "letters":
            first_slot_letters.clear()
            while True:
                letter = input("Enter the first letter (type done when all possible answers have been entered): ")
                if letter.lower() == "done":
                    break
                else:
                    if len(letter) == 1 and letter.isalpha() and letter not in first_slot_letters:
                        first_slot_letters.append(letter)
                    else:
                        print("That is not a valid letter or it is already in the list!")
                print(first_slot_letters)
            second_slot_letters.clear()
            while True:
                letter = input("Enter the second letter (type done when all possible answers have been entered): ")
                if letter.lower() == "done":
                    break
                else:
                    if len(letter) == 1 and letter.isalpha() and letter not in second_slot_letters:
                        second_slot_letters.append(letter)
                    else:
                        print("That is not a valid letter or it is already in the list!")
                print(second_slot_letters)
            third_slot_letters.clear()
            while True:
                letter = input("Enter the third letter (type done when all possible answers have been entered): ")
                if letter.lower() == "done":
                    break
                else:
                    if len(letter) == 1 and letter.isalpha() and letter not in third_slot_letters:
                        third_slot_letters.append(letter)
                    else:
                        print("That is not a valid letter or it is already in the list!")
                print(third_slot_letters)
            fourth_slot_letters.clear()
            while True:
                letter = input("Enter the fourth letter (type done when all possible answers have been entered): ")
                if letter.lower() == "done":
                    break
                else:
                    if len(letter) == 1 and letter.isalpha() and letter not in fourth_slot_letters:
                        fourth_slot_letters.append(letter)
                    else:
                        print("That is not a valid letter or it is already in the list!")
                print(fourth_slot_letters)
            fifth_slot_letters.clear()
            while True:
                letter = input("Enter the fifth letter (type done when all possible answers have been entered): ")
                if letter.lower() == "done":
                    break
                else:
                    if len(letter) == 1 and letter.isalpha() and letter not in fifth_slot_letters:
                        fifth_slot_letters.append(letter)
                    else:
                        print("That is not a valid letter or it is already in the list!")
                print(fifth_slot_letters)
        case "required":
            required = []
            while True:
                letter = input("Enter any required letters (green): ")
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
            
            print(accepted_words)

                
        case "exit":
            exit()
        case unknown_command:
            print("Command not recognised, try 'help'")
