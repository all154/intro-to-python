# Problem Set 2, hangman.py
# Name: Aloisio Valério Jr.
# Collaborators: None
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_found = 0

    for char in secret_word:
      for letter in letters_guessed:
        if char == letter:
          letters_found += 1
          break
    
    if letters_found == len(secret_word):
      return True
    else:
      return False


def test_is_word_guessed():
  assert is_word_guessed('apple',['e','i','k','p','r','s']) == False, 'Should be false'
  assert is_word_guessed('apple',['e','a','l','p','r','s']) == True, 'Should be true'

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ''
    
    for char in secret_word:
      for letter in letters_guessed:
        if char == letter:
          guessed_word += letter
          break

        if letter == letters_guessed[len(letters_guessed)-1]:
          guessed_word += '_ '

    return guessed_word

def test_get_guessed_word():
  assert get_guessed_word('bird',['b','i','k','d','r','s']) == 'bird', "Should be 'bird'"
  assert get_guessed_word('apple',['e','i','k','p','r','s']) == '_ pp_ e', "Should be '_ pp_ e'"
  assert get_guessed_word('bird',['e','i','k','p','r','s']) == '_ ir_ ', "Should be '_ ir_ '"

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    import string

    available_letters = ''
    alphabet = string.ascii_lowercase

    if (len(letters_guessed) == 0):
      return alphabet

    for char in alphabet:
      for letter in letters_guessed:
        if char == letter:
          break
        if letter == letters_guessed[len(letters_guessed)-1]:
          available_letters += char
    
    return available_letters
    
def test_get_available_letters():
  assert get_available_letters([]) == 'abcdefghijklmnopqrstuvwxyz'
  assert get_available_letters(['e', 'i', 'k', 'p', 'r', 's']) == 'abcdfghjlmnoqtuvwxyz'

def is_guess_in_word(guess, secret_word):
  '''
  guess: string, letter guessed by user
  secret_word: string, the secret word to guess
  returns: boolean, True if letter is found in secret_word
      False otherwise
  '''
  for char in secret_word:
    if char == guess:
      return True

  return False

def test_is_guess_in_word():
  assert is_guess_in_word('e', 'apple') == True
  assert is_guess_in_word('m', 'apple') == False

def was_already_guessed(guess, letters_guessed):
  '''
  guess: string, letter guessed by user
  letters_guessed: list (of letters), which letters have been guessed so far
  returns: boolean, True if letter is found in letters_guessed
      False otherwise
  '''
  for letter in letters_guessed:
    if guess == letter:
      return True

  return False

def test_was_already_guessed():
  assert is_guess_in_word('m', []) == False
  assert is_guess_in_word('e', ['a','e','b']) == True
  assert is_guess_in_word('m', ['a','e','b']) == False

def is_valid_letter(guess):
  '''
  guess: string, letter guessed by user
  returns: boolean, True if letter is valid
      False otherwise
  '''
  import string

  alphabet = string.ascii_lowercase

  for char in alphabet:
    if guess == char:
      return True
  
  return False

def test_is_valid_letter():
  assert is_valid_letter('n') == True
  assert is_valid_letter('$') == False
  assert is_valid_letter('5') == False

def list_of_unique_letters(word):
  unique_letters = []

  for char in word:
    if (not was_already_guessed(char, unique_letters)):
      unique_letters.append(char)
  
  return unique_letters

def unique_letters(secret_word):
  '''
  secret_word: string, the secret word to guess
  returns: integer, number of unique letters in given word
  '''
  return len(list_of_unique_letters(secret_word))

def test_unique_letters():
  assert unique_letters('') == 0
  assert unique_letters('apple') == 4
  assert unique_letters('general') == 6
  assert unique_letters('punctures') == 8

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses_remaining = 6
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    print("-------------")

    while(guesses_remaining > 0):
      if(is_word_guessed(secret_word, letters_guessed)):
        total_score = guesses_remaining * unique_letters(secret_word)

        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(total_score))

        break
        
      print("You have " + str(guesses_remaining) + " guesses left.")
      print("Available letters: " + get_available_letters(letters_guessed))
      
      guess = input("Please, guess a letter:")

      if (is_valid_letter(guess)):
        if (was_already_guessed(guess, letters_guessed)):
          if (warnings > 0):
            warnings -= 1
            print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left:" + guessed_word)
          else:
            guesses_remaining -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" + guessed_word)
        else:
          letters_guessed.append(guess)
          guessed_word = get_guessed_word(secret_word, letters_guessed)

          if (is_guess_in_word(guess, secret_word)):
            print("Good guess: " + guessed_word)
          else:
            print("Oops! That letter is not in my word: " + guessed_word)
            guesses_remaining -= 1
      else:
        if (warnings > 0):
          warnings -= 1
          print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left:" + guessed_word)
        else:
          guesses_remaining -= 1
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:" + guessed_word)
        
      
      print("-------------")

      if (guesses_remaining == 0):
        print("Sorry, you ran out of guesses. The word was " + secret_word)


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word_without_spaces = my_word.replace(" ","")
    missing_letters = []

    if (len(my_word_without_spaces) != len(other_word)):
      return False
    else:
      for i in range(len(other_word)):
        if (my_word_without_spaces[i] != other_word[i]):
          if (my_word_without_spaces[i] == "_"):
            missing_letters.append(other_word[i])
            continue
          else:
            return False
    
    # if missing letter was already used, word cannot match
    for char in list_of_unique_letters(my_word):
      for letter in missing_letters:
        if char == letter:
          return False

    return True

def test_match_with_gaps():
  assert match_with_gaps('te_ t', 'tact') == False
  assert match_with_gaps("a_ _ le", "banana") == False
  assert match_with_gaps("a_ _ le", "apple") == True
  assert match_with_gaps("a_ ple", "apple") == False 

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = 0

    for word in wordlist:
      if match_with_gaps(my_word, word):
        print(word, end =" ")
        possible_matches += 1
    
    if possible_matches == 0:
      print("No matches found")
      return
    
    print("")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    warnings = 3
    guesses_remaining = 6
    letters_guessed = []
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    
    print("-------------")
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings) + " warnings left.")
    print("-------------")

    while guesses_remaining > 0:
      if is_word_guessed(secret_word, letters_guessed):
        total_score = guesses_remaining * unique_letters(secret_word)

        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(total_score))

        break
        
      print("You have " + str(guesses_remaining) + " guesses left.")
      print("Available letters: " + get_available_letters(letters_guessed))
      
      guess = input("Please, guess a letter:")

      if is_valid_letter(guess):
        if was_already_guessed(guess, letters_guessed):
          if warnings > 0:
            warnings -= 1
            print("Oops! You've already guessed that letter. You have " + str(warnings) + " warnings left:" + guessed_word)
          else:
            guesses_remaining -= 1
            print("Oops! You've already guessed that letter. You have no warnings left so you lose one guess:" + guessed_word)
        else:
          letters_guessed.append(guess)
          guessed_word = get_guessed_word(secret_word, letters_guessed)

          if is_guess_in_word(guess, secret_word):
            print("Good guess: " + guessed_word)
          else:
            print("Oops! That letter is not in my word: " + guessed_word)
            guesses_remaining -= 1
      elif guess == "*":
        print("Possible word matches are:")
        show_possible_matches(guessed_word)
      else:
        if warnings > 0:
          warnings -= 1
          print("Oops! That is not a valid letter. You have " + str(warnings) + " warnings left:" + guessed_word)
        else:
          guesses_remaining -= 1
          print("Oops! That is not a valid letter. You have no warnings left so you lose one guess:" + guessed_word)
        
      
      print("-------------")

      if (guesses_remaining == 0):
        print("Sorry, you ran out of guesses. The word was " + secret_word)

def all_tests():
  # Calls every test of every helper function used

  print("Testing helper functions...")
  test_is_word_guessed()
  test_get_guessed_word()
  test_get_available_letters()
  test_is_guess_in_word()
  test_was_already_guessed()
  test_is_valid_letter()
  test_unique_letters()
  test_match_with_gaps()
  print("   All tests passed!")

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    all_tests()

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
