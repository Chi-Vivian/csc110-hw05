"""
Name: Vivian Nguyen 
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Inside the function, it should repeatedly run.
    Ask the user for a string. 
    If the length of the provided answer is not 1, print the Error message and make the loop repeat the question.
    If the length is 1, check the next thing.
    If the provided string is not "A", "B", or "C", print the Error message and ask the question again. If the provided string is, return the character."""
    
    while True: # infinite repeated loop until getting the right string
        letter_string = input("Give an single uppercase letter: ") # ask for a string
        len_string = len(letter_string) # get the length of the string
        
        # Check if the length of the string is 1 or not
        if len_string != 1:
            print("Error: it needs to be a single character.")
            continue
        
        # Check if the string is "A", "B", "C", or not
        if letter_string not in ("A", "B", "C"):
            print("Error: You provided the wrong character.")
            continue
        
        # Return the checked string and exit the loop
        else:
            return letter_string
    

def get_digit():
    """ Ask the user for a single number character.
    If the provided answer does not contain only digits, print the Error message and ask again.
    If the asnwer is digit, check if the digit is "1", "2", or "3". If not, print the Error message and ask again.
    If match, return the character. """
    
    while True: 
        number = input("Give an single number character: ") # get the user's input
        
        # Check if the input is composed of only digit or not
        if not number.isdigit():
            print("Error: your input should be only digits.")
            continue
        
        # Check if the input is "1", "2", "3", or not
        if number not in ("1", "2", "3"):
            print("Error: a single digit needs to be in [1,3].")
            continue
        
        # Return the number and exit the loop
        else:
            return number


def check_pattern(letter, digit, lst):
    """ Searches a list of strings and prints those where letter appears before digit.
    The words that contain the pattern get printed out. But the words that contain the letter and the number but not in the order is not be printed out and words that have the pattern more than once only get printed once."""
    
    print("Strings with the pattern:") # print the message first
    
    # define the pattern to check
    pattern = letter + digit
     
    # check each word in the list
    for word in lst:
        
        # set the default condition to be True
        condition = True
        
        # check each letter in the word
        for i in range(len(word)):
            
            # if the letter appear, move on to the the loop
            if word[i] == letter:
                
                # check each letter in the word after the letter justed get checked 
                for j in range(i+1, len(word)):
                    
                    # check if the digit appears
                    if word[j] == digit:
                        print(word, end=" ")
                        condition = False
                        break
            
            # if the letter does not appear, the condition is false, break the loop
            if condition == False:
                break
    
    print()

    
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    while True:
        letter = get_letter() # call the function to get the letter from the user's input
        digit = get_digit()  # call the function to get the digit from the user's input
        check_pattern(letter, digit, st_list) # check the pattern and print the ones that matched
        
        # ask if the user want to continue or not
        again = input("Try Again? (y/n): ")
        
        if again.lower() == "y":
            continue
        else:
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()
