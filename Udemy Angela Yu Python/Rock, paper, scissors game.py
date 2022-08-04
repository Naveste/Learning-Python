import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def show_results():
    print("\nResults:\n")
    print("You:",user_count)
    print("Comp:",comp_count)

    if user_count > comp_count:
        print("You won the best of.")
    else:
        print("Computer won the best of.")


bestof_input = int(input("How many games do you want to play?"))

valid_numbers = [0, 1, 2]
user_count = 0
comp_count = 0

while True:
    #user choice
    user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
    
    if user not in valid_numbers:
        print("Incorrect value. Exiting.")
        break

    print("Your choice: ")
    if user == 0:
        print(rock)
    elif user == 1:
        print(paper)
    elif user == 2:
        print(scissors)
    
    #computer choice
    print("Computer's choice: ")
    result = random.choice([rock, paper, scissors])
    print(result)

    if user == 0:
        if result == scissors:
            print("You win!")
            user_count += 1
            if user_count == bestof_input:
                show_results()
                break
        elif result == paper:
            print("You lose!")
            comp_count += 1
            if comp_count == bestof_input:
                show_results()
                break
        else:
            print("Draw!")

    elif user == 1:
        if result == rock:
            print("You win!")
            user_count += 1
            if user_count == bestof_input:
                show_results()
                break
        elif result == scissors:
            print("You lose!")
            comp_count += 1
            if comp_count == bestof_input:
                show_results()
                break
        else:
            print("Draw!")

    elif user == 2:
        if result == paper:
            print("You win!")
            user_count += 1
            if user_count == bestof_input:
                show_results()
                break
        elif result == rock:
            print("You lose!")
            comp_count += 1
            if comp_count == bestof_input:
                show_results()
                break
        else:
            print("Draw!")