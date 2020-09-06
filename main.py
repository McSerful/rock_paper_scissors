# ROCK, PAPER, SCISSORS GAME

import random

print("Play rock, paper, scissors with me, a computer!")


wins = 0
losses = 0
ties = 0



game_is_going = True

while game_is_going is True:
    computer_move = random.randint(1, 3)
    print("ROCK, PAPER, SCISSORS")
    print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit: ")
    move = input("> ").lower()
    if move == "r":
        print("ROCK versus...")
        computer_move
        if computer_move == 1:
            print("ROCK")
            print("It's a tie.")
            ties += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue
        elif computer_move == 2:
            print("PAPER")
            print("You lose.")
            losses += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue
        elif computer_move == 3:
            print("SCISSORS")
            print("You win!")
            wins += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue


    elif move == "p":
        print("PAPER versus...")
        if computer_move == 1:
            print("ROCK")
            print("You win!")
            wins += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue
        elif computer_move == 2:
            print("PAPER")
            print("It's a tie.")
            ties += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue
        elif computer_move == 3:
            print("SCISSORS")
            print("You lose.")
            losses += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue

    elif move == "s":
        print("SCISSORS versus...")
        if computer_move == 1:
            print("ROCK")
            print("You lose.")
            losses += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue
        elif computer_move == 2:
            print("PAPER")
            print("You win!")
            wins += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue
        elif computer_move == 3:
            print("SCISSORS")
            print("It's a tie.")
            ties += 1
            print(f'{wins} Wins, {losses} Losses, {ties} Ties')
            continue


    elif move == "q":
        game_is_going = False

    else:
        print("Sorry, I don't understand. I'm just a machine.")
        continue

print("The game is over.")
