import random

outcome = {
    'r':'Rock',
    'p':'Paper',
    's':'Scissors'
}
player = str(input('Enter your name: '))
user_input = input("Enter a choice (R, P, S): ").lower()
computer_choice = random.choice(list(outcome.keys()))

while True:
    
    if user_input == computer_choice:
        choices = outcome[user_input]
        choice = outcome[computer_choice]
        print(f'{player}: {choices}, CPU: {choice}')
        print(f"Both players selected {choice}. It's a tie!")
        break
    elif user_input == "r":
        choices = outcome[user_input]
        if computer_choice == "s":
            choice = outcome[computer_choice]
            print(f'{player}: {choices}, CPU: {choice}')
            print("Rock smashes scissors! You win!")
        else:
            choice = outcome[computer_choice]
            print(f'{player}: {choices}, CPU: {choice}')
            print("Paper covers rock! You lose.")
        break
    elif user_input == "p":
        choices = outcome[user_input]
        if computer_choice == "r":
            choice = outcome[computer_choice]
            print(f'{player}: {choices}, CPU: {choice}')
            print("Paper covers rock! You win!")
        else:
            choice = outcome[computer_choice]
            print(f'{player}: {choices}, CPU: {choice}')
            print("Scissors cuts paper! You lose.")
        break
    elif user_input == "s":
        choices = outcome[user_input]
        if computer_choice == "p":
            choice = outcome[computer_choice]
            print(f'{player}: {choices}, CPU: {choice}')
            print("Scissors cuts paper! You win!")
        else:
            choice = outcome[computer_choice]
            print(f'{player}: {choices}, CPU: {choice}')
            print("Rock smashes scissors! You lose.")
        break



