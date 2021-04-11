

'''

       iM gOnNa sAy sOmEthInG dUmB aNd iT mUsT bE mOcKeD

       Script to return a body of text in a mocking tone.

'''
import random


test_text = "Please pass me some text that deserves to be mocked. "

bit_flip_chance = 0.15

def setup():
    random.seed()



def mock_this(text):
    text_list = list(text)
    next_char_lower = True

    return_text = []
    for char in text_list:
        if char == " ":                                                  # If we detect a space, 
            next_char_lower = True                             # The next character must be lowercase
            char_out = char
        else:
            if next_char_lower:                                      # If there is not a space, then if we have set the 
                char_out = char.lower()                         # Next char to be lower, it will be lower
                next_char_lower = chance_flip_bit(False, bit_flip_chance)   # we then want the next char to be high, but with a chance for it to stay low
            else:
                char_out = char.upper()
                next_char_lower = chance_flip_bit(True, bit_flip_chance)
        return_text.append(char_out)
    output = list_to_string(return_text)
    #print(output)
    return output
           
                
def list_to_string(l):
    str1 = ""
    for char in l:
        str1 += char
    return str1
            


# We do not want a totally random flip, we want to mostly alternate between 0 and 1, but occasionally not
def coin_flip():
    while 1:
        coin = random.getrandbits(1)
        print(coin)
    return coin


# This function will give chance to flip a bit passed to it
def chance_flip_bit(last_bit, chance):
    val = random.randrange(0, 100, 1)
    if (val < chance*100):                                 # if our random number between 0 and 100 is less than our chance * 100  
        if last_bit:
            next_bit = 0
        else:
            next_bit = 1
    else:
            next_bit = last_bit
    return next_bit



def if_input_yes(user_input):
    if user_input.lower()=="y" or user_input.lower()=="yes":
        return True
    else:
        return False


def if_input_yes_no():
    while 1:
        user_input = input("[ y ] / [ n ] ?\n")
        if user_input.lower()=="y" or user_input.lower()=="yes":
            return True
            break
        else:
            if user_input.lower()=="n" or user_input.lower()=="no":
                return False
                break
            else:
                continue



def main():
    while 1:
        mock_this(test_text)
        print("\n\n\n")
        try:
            user_input = input("Please pass me some text that deserves to be mocked. \n\n\n")
            mocking_output = mock_this(user_input)
            print("\n\n\n", mocking_output)
        except:
            print("Error parsing text...")
        print("\n\n\n")
        print("Any More Text to Mock?\n")
        if if_input_yes_no():                
            continue
        else:
            break
            
        
        
    






if __name__ == "__main__":
    main()



