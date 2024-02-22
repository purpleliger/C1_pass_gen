import random
import string

"""Function generates a 15 character password including special characters and numbers."""
def gen_password(length = 15, special = True, numbers = True):
    chars = string.ascii_letters + string.digits
    #if user selects 'y' for special characters, then include them
    if special:
        chars += string.punctuation
    
    #if user selects 'y' for numbers, then include them
    if numbers:
        chars += string.digits

    password = ''.join(random.choice(chars) for i in range(length))
    return password

