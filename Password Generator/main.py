import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to interact with the user
def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            password = generate_password(length)
            print("Generated Password: ", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

# Run the main function
if __name__ == "__main__":
    main()
