import requests

api_url = 'https://random-word-form.herokuapp.com/random/noun'
chosen_word = requests.get(api_url).text.replace('[','').replace(']','').replace('"','')
filler_txt_container = ['_ ' for i in chosen_word]
lives = 6
filler_txt = ''

print(chosen_word)

def find_letter_positions(letter, word_letter_list):
    pos = []
    for i in range(len(word_letter_list)):
        if word_letter_list[i] == letter:
            pos.append(i)
    return pos

while lives > 0:
    print('\n')
    for i in filler_txt_container:
        filler_txt += i
    print(filler_txt)
    geuss = input('Enter a letter: ')
    if geuss.lower() in chosen_word.lower():
        print('\n')
        filler_txt = ''
        letter_positions = find_letter_positions(geuss,list(chosen_word))
        for i in letter_positions:
            filler_txt_container[i] = geuss + " "
        for i in filler_txt_container:
            filler_txt += i
        print(filler_txt)
        print('The geuss was correct!')
        geuss_word_yn = input('Would you like to try and geuss the word?(Y/N): ')
        if geuss_word_yn.lower() == 'y':
            print('\n')
            geuss_word = input('Input the word: ')
            if geuss_word == chosen_word:
                print(f'You have won with {lives} lives remaining')
                print(f"The word was {chosen_word.upper()}")
                break
            else:
                lives -= 1
                print(f'The geuss was wrong! You have {lives} lives remaining.')
    else:
        lives -= 1
        print(f'The geuss was wrong! You have {lives} lives remaining.')
    filler_txt = ''

if lives == 0:
    print('\n')
    geuss_word = input('Input your last guess: ')
    if geuss_word == chosen_word:
        print('\n')
        print(f'You have won with your last guess!')
        print(f"The word was {chosen_word.upper()}")
    else:
        print('\n')
        print('You have lost!')
        print(f"The word was {chosen_word.upper()}")
   