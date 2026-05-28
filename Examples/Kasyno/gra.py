from Player import *
import random as rnd


def draw_card(deck, side):
    if not deck:
        raise ValueError("Deck is empty!")
    card = rnd.choice(deck)        
    deck.remove(card)
    print(f"{side} draws: {card}")
    return card

def game():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
    cassino = 0
    player = 0

    # Casino draws 2 first card
    cassino += draw_card(deck, "Casino")
    cassino += draw_card(deck, "Casino")
    # Player draws first card
    player += draw_card(deck, "Player")

    player_wanted_to_draw = True
    cassino_wants_to_draw = True

    while True:
        print(f"Casino's score: {cassino}, Player's score: {player}")

        if cassino < 17:
            cassino += draw_card(deck, "Casino")
            if cassino > 21:
                break
        else:
            cassino_wants_to_draw = False
        
        choose = input("Do you want to draw another card? (y/n): ").lower()        

        if choose == 'y':
            player += draw_card(deck, "Player")
            if player > 21:
                break
        else:
            player_wanted_to_draw = False

        if not player_wanted_to_draw and not cassino_wants_to_draw:
            break
    
    if player > cassino and player <= 21:
        if player == 21:
            print("Player won with a Blackjack!")
            return 5
        print("Player won the game.")
        return 1
    elif player > 21:
        print("Player busted! Casino wins.")
        return -1
    elif cassino > 21:
        print("Casino busted! Player wins.")
        if player == 21:
            print("Player won with a Blackjack!")
            return 5
        return 1
    elif player == cassino:
        print("It's a tie!")
        return 0
    else:
        print("Player lost the game.")
        return -1    
        
                    
            

def menu():
    while True:
        print("1. New Game")
        print("2. Players Stats")    
        print("3. Exit")
        try:
            choice = int(input("Choose an option: "))
            if 1 <= choice <= 3:
                return choice
        except ValueError:
            ...
        except KeyboardInterrupt:
            return 3

def find_player(players, name):
    for player in players:
        if player.name == name:
            return player
    return None

def main():
    players = []
    while True:
        choice = menu()
        if choice == 1:
            name = input("Enter player name: ")

            active_player = find_player(players, name)
            if active_player:
                print(f"Active player:  {active_player}")
                if active_player.score <= 0:
                    print("Player has no points left!")                    
            else:
                active_player = Player(name)
                print(f"New player created: {active_player}")
                players.append(active_player)

            while active_player.score > 0:
                score = game()
                
                
                active_player.score += score
                choose = input("Do you want to play again? (y/n): ").lower()
                if choose != 'y':
                    break


        elif choice == 2:
            print("Player Stats:")
            for player in players:
                print(player)

        elif choice == 3:
            print("Exiting game. Goodbye!")
            break





if __name__ == "__main__":
    main()