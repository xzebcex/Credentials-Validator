# Credentials Validator:

# Continuously prompt the user to enter a username until a valid input is received.
while True:
    print('Enter your UserName:')
    user_name = input()
    # Check if the input only contains letters.
    if user_name.isalpha():
        break
    print('Please enter a username consisting of only Letters.')

# Continuously prompt the user to enter a password until a valid input is received.
while True:
    print('Select a new Password (Letters and Numbers only):')
    password = input()
    # Check if the input only contains alphanumeric characters.
    if password.isalnum():
        break
    print('Password can only have letters and numbers.')

# Display the entered username and password.
print(f'Your UserName: {user_name}\nYour Password: {password} ')
