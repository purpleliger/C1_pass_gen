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

def main():
    print("Generate a randomized password of desired difficulty")
    length = int(input("Enter the length of the password: "))
    special = input("Do you wish to include special characters? (y/n): ").lower() == 'y'
    numbers = input("Do you wish to include numbers? (y/n): ").lower() == 'y'

    password = gen_password(length, special, numbers)

    print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    main()
    