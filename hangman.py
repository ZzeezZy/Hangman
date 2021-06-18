import random
words = ['python', 'java', 'kotlin', 'javascript']
print("H A N G M A N \n")
a = random.choice(words)
replaced_word = '-' * (len(a))
guessed_letter = list()

while True:
    print("Type \"play\" to play the game, \"exit\" to quit: > ")
    menu = input()
    print()
    if menu == 'play':
        tries = 8
        while tries > 0:
            print(replaced_word)
            word = list(replaced_word)

            if replaced_word == a:
                print("You guessed the word!")
                print("You survived!\n")
                break
            print("Input a letter: > ")
            letter = input()
            guessed_letter.append(letter)

            if len(letter) != 1:
                print("You should input a single letter\n")
                continue
            if letter.islower() is False:
                print("Please enter a lowercase English letter\n")
                continue

            if letter not in a or letter in word:
                if letter in word:
                    print("You've already guessed this letter")
                    if tries > 0:
                        print()
                if letter not in a:
                    if guessed_letter.count(letter) >= 2:
                        print("You've already guessed this letter\n")
                        continue
                    else:
                        print('That letter doesn\'t appear in the word')
                        tries -= 1
                        if tries > 0:
                            print()
            elif letter in a:
                for i in range(len(a)):
                    test = a[i]
                    if test == letter:
                        word.pop(i)
                        word.insert(i, letter)
                        replaced_word = ''.join(word)
                        print()
            if tries == 0:
                print("You lost!\n")
                break
    elif menu == 'exit':
        quit()
