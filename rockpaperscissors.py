import random
def det_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a tie!"
    elif user_choice=='rock':
        if computer_choice=='paper':
            return 'Computer wins!'
        else:
            return 'you win!'
    elif user_choice=='paper':
        if computer_choice=='scissors':
            return 'Computer wins!'
        else:
            return 'you win!'
    elif user_choice=='scissors':
        if computer_choice=='rock':
             return 'Computer wins!'
        else:
            return 'you win!'
    else:
        return "Please enter a Valid Input"
def game():
    user_choice=input('rock,paper,scissors:')
    computer_choice=random.choice(['rock','paper','scissors'])
    print('You Choose:',user_choice)
    print('Computer Choose:',computer_choice)
    print(det_winner(user_choice,computer_choice))
game()
    
    
    