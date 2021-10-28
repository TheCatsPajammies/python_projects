import random

print("H A N G M A N\n")

running = True
while running == True:
    menu = True
    while menu is True:
        menu = input("""Type "play" to play the game, "exit" to quit:""")
        if menu == 'exit':
            exit()
        if menu == 'play':
            break
        else:
            print("\nBr0ether, please type 'exit' or 'play'....\n")
            menu = True



    wordlist = ['python', 'java', 'kotlin', 'javascript']

    wrng_attempts = 0
    mx_attempts = 8

    cor_ans = random.choice(wordlist)
    progress = len(cor_ans) * "-"
    guessed_cor = []
    guessed_incor = []


    while wrng_attempts != mx_attempts:
    
    
    
        letter = input(f'\n{progress}\nInput a letter:')
    
        if letter in guessed_cor:
            print("You already typed this letter")

        if letter in cor_ans:
            guessed_cor.append(letter)
            new_progress = ""
            for index, char in enumerate(cor_ans):
                if char == letter:
                    new_progress += letter
                else:
                    new_progress += progress[index]
            progress = new_progress

            if new_progress == cor_ans:
                print(f'\n{progress}\nYou guessed the word!\nYou survived!')
                break
        
            if wrng_attempts == mx_attempts and progress != cor_ans:
                print("You are hanged!")
                break
    
    
        elif len(letter) > 1:
            print("You should input a single letter")
        elif letter.isalpha() == False or letter.lower() != letter:
            print("It is not an ASCII lowercase letter")
        elif letter.lower() in guessed_incor:
            print("You already typed this letter")
        elif letter.lower() not in cor_ans:
            print("No such letter in the word")
            wrng_attempts += 1
            guessed_incor.append(letter)
            if wrng_attempts == mx_attempts and progress != cor_ans:
                print("You are hanged!")
                break

    
