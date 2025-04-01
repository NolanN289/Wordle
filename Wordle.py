import string
word_length = 5

def read_dictionary(file_name):
    file_object = open(file_name)
    file_list = file_object.readlines()
    new_dictionary_list = []
    for i in file_list:
        x = i.replace('\n', '')
        new_dictionary_list.append(x.lower())
    return new_dictionary_list

def enter_a_word(word_type, num_letters):
    word_input = str(input(f'Enter the {num_letters}-letter {word_type} word: '))
    a_word = word_input.lower()
    return a_word            


def is_it_a_word(input_word, dictionary_list):
    if input_word in dictionary_list:
        is_word = True
    else:
        is_word = False
    return is_word

def enter_and_check(word_type, dictionary_list):
    x = False
    while x == False:
        in_word = enter_a_word(word_type, 5)
        if len(in_word) == 5:
            if is_it_a_word(in_word, dictionary_list):
                x = True
            else:
                print(f'\nYou entered a 5-letter {word_type} that is not in the dictionary. Please try again!')
                x = False
        elif len(in_word) != 5:
            if is_it_a_word(in_word, dictionary_list):
                print(f'\nYou entered a {len(in_word)}-letter word that is in the dictionary. Please try again!')
                x = False
            else:
                print(f'\nYou entered a {len(in_word)}-letter word that is not in the dictionary. Please try again!')
                x = False
    return in_word

def compare_words(player, secret):
    global remaining_alphabet 
    global in_secret_word_correct_spot 
    global in_secret_word_somewhere 
    global not_in_secret_word
    final = ''
    global in_correct_spot
    in_correct_spot = 0

    for i in range(len(secret)):
        in_str = False
        if player[i] == secret[i]:
            for y in in_secret_word_correct_spot:
                if player[i] == y:
                    in_str = True
                    break
                else:
                    in_str = False
            if in_str == False:
                in_secret_word_correct_spot.append(player[i])
            final += player[i]
            if player[i] in remaining_alphabet:
                remaining_alphabet.remove(player[i])
            in_correct_spot += 1
        elif player[i] in secret:
            for y in in_secret_word_somewhere:
                if player[i] == y:
                    in_str = True
                    break
                else:
                    in_str = False
            if in_str == False:
                in_secret_word_somewhere.append(player[i])
            final += (f'({player[i]})')
            if player[i] in remaining_alphabet:
                remaining_alphabet.remove(player[i])
        else:
            for y in not_in_secret_word:
                if player[i] == y:
                    in_str = True
                    break
                else:
                    in_str = False
            if in_str == False:
                not_in_secret_word.append(player[i])
            final += ('_')
            if player[i] in remaining_alphabet:
                remaining_alphabet.remove(player[i])

    print(f'\nletter in the right spot: {in_correct_spot}')            
    return final, in_correct_spot


#Start of the Actual Program
alphabet_string = string.ascii_lowercase
remaining_alphabet = list(alphabet_string)
in_secret_word_correct_spot = [] 
in_secret_word_somewhere = [] 
not_in_secret_word = []
words_list = read_dictionary('Wordle_dictionary.txt') # Change to match file name!

N = 0
attempts = 0

print('Welcome to new and improved Wordle (probably)!')
secret = enter_and_check('secret', words_list)
N = int(input("Input allowed number of attempts: "))

while attempts <= N:
    if N == 0:
        break
    if attempts == N:
        print(f'You already used #{attempts} attempts. Better luck tomorrow!')
        break  
    print(f'Enter your attempt #{attempts + 1}')
    player = enter_and_check('player', words_list)
    result, in_correct_spot = compare_words(player, secret)
    print(f'You guessed letters of the secret_word: {result}')
    print(f'Previously attempted letters that are in the correct spot of secret_word:\n{in_secret_word_correct_spot}')
    print(f'Previously attempted letters that are in some spot of secret_word:\n{in_secret_word_somewhere}')
    print(f'Previously attempted letters that are not in the secret_word:\n{not_in_secret_word}')
    print(f'Remaining letters of the alphabet that have not been tried:\n{remaining_alphabet}')

    if in_correct_spot == len(secret):
        print(f'Congrats you won using {attempts + 1} attempt(s)')
        break
    
    attempts += 1
