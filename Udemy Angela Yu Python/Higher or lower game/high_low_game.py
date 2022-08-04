from game_data import data
import random

rand_list = []

def pick_randomly(data): #get random dict from game_data
    for _ in range(1):
        entity = random.choice(data)
        if entity in rand_list:
            entity = random.choice(data)
        else:
            return entity
    
    return entity


def follower_count(entity): #grab information from entity and format.
    follower = ""

    follower = entity['follower_count'], f"{entity['name']}, a {entity['description']}, from {entity['country']}"

    return follower

a_random = pick_randomly(data) #pick random data and assign to a_random.
rand_list.append(a_random) #add it to the list rand_list.
b_random = pick_randomly(data) #pick random data and assign to b_random.
rand_list.append(b_random) #add it to the list rand_list.

a_follower = follower_count(a_random) #get follower count from a_random and assign to a_follower.
b_follower = follower_count(b_random) #get follower count from b_random and assign to b_follower.

score = 0

while True:
    print(f"Test A: {a_follower}")
    print(f"Test B: {b_follower}")
    print("")
    print(f"Compare A: {a_follower[1]}") #only show rest of information and not follower count for the user.
    print(f"Against B: {b_follower[1]}") #only show rest of information and not follower count for the user.
    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if b_follower == a_follower:
        score += 1
        add_point = print("You're right! Current score:",score)
        a_follower = b_follower
        b_random = pick_randomly(data)
        b_follower = follower_count(b_random)
        continue

    elif a_follower > b_follower: 
        if user_input == 'a': #if user selects 'a', it is the correct answer.
            score += 1
            add_point = print("You're right! Current score:",score)
            a_follower = b_follower #assign b_follower to a_follower.
            b_random = pick_randomly(data) #pick random data and assign to b_random.
            b_follower = follower_count(b_random) #get follower count and assign to b_follower.
            continue
        elif user_input == 'b': #if wrong answer, break.
            print("Wrong answer! Final score:",score)
            break
    
    elif b_follower > a_follower:
        if user_input == 'b':
            score += 1
            add_point = print("You're right! Current score:",score)
            a_follower = b_follower
            b_random = pick_randomly(data)
            b_follower = follower_count(b_random)
        elif user_input == 'a':
            print("Wrong answer! Final score:",score)
            break