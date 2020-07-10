import time as t
import random
from colorama import Fore


class Cards:
    card_values = {
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5,
        6: 6,
        7: 7,
        8: 8,
        9: 9,
        10: 10,
        11: 11,
        "Ace": 1,
        "Jack": 10,
        "Queen": 10,
        "King": 10
    }


class Dealer(Cards):
    hand = {

    }
    hand_value = sum(hand.values())

    def play(self):
        scard1 = random.choice(list(Cards.card_values.values()))
        Dealer.hand.update(card1 = scard1)
        Dealer.hand_value = sum(Dealer.hand.values())
        print(f'{Fore.GREEN}Dealer has appeared')
        print(f'{Fore.LIGHTCYAN_EX}Dealer was given a: {scard1}')
        t.sleep(3)

        scard2 = random.choice(list(Cards.card_values.values()))

        if Dealer.hand_value <= 16:
            Dealer.hand.update(card2 = scard2)
            Dealer.hand_value = sum(Dealer.hand.values())
            print(f'Revealing Dealers Hidden Card..')
            t.sleep(5)
            print(f'Dealers hidden card was a {Fore.RED}{scard2}')
            print(f'{Fore.BLACK}Dealers Hand now equals to {Dealer.hand_value} ')

            if Dealer.hand_value <= 16:
                scard3 = random.choice(list(Cards.card_values.values()))
                print(f'{Fore.YELLOW}Dealer receives a: {Fore.RED}{scard3}')
                Dealer.hand.update(card3=scard3)
                Dealer.hand_value = sum(Dealer.hand.values())
                print(f'Dealers hand = {Dealer.hand_value}')

            t.sleep(4)
            if Dealer.hand_value <= 16:
                scard4 = random.choice(list(Cards.card_values.values()))
                Dealer.hand.update(card4=scard4)
                Dealer.hand_value = sum(Dealer.hand.values())
                print(f'{Fore.LIGHTBLUE_EX}Dealer receives a: {Fore.RED}{scard4}')
                print(f'Dealers hand now = {Dealer.hand_value}')

            if Dealer.hand_value <= 16:
                scard5 = random.choice(list(Cards.card_values.values()))
                Dealer.hand.update(card5=scard5)
                Dealer.hand_value = sum(Dealer.hand.values())
                print(f'{Fore.LIGHTBLUE_EX}Dealer receives a: {Fore.RED}{scard5}')
                print(f'Dealers hand now = {Dealer.hand_value}')
                t.sleep(2)

            if Dealer.hand_value == 21:
                print(f'{Fore.RED}Dealer Wins')

            if Dealer.hand_value > 16 & Player.hand_value > Dealer.hand_value or Player.hand_value > Dealer.hand_value > 16:
                t.sleep(3)
                print(f'{Fore.GREEN}Player wins!')
        t.sleep(2)

        if Dealer.hand_value > Player.hand_value & Player.hand_value < 21 or Player.hand_value > 21 or Player.hand_value < 21 & Dealer.hand_value > Player.hand_value:
            print(f'{Fore.RED}Dealer Wins')
            print(f'Players Hand Value: {Player.hand_value}, Dealers: {Dealer.hand_value}')

        if Dealer.hand_value == Player.hand_value & Dealer.hand_value > 16:
            print(f'{Fore.GREEN}It is a Tie.. Wow')


class Player(Cards):
    hand = {

    }
    hand_value = sum(hand.values())

    def __init__(self, name):
        self.player = name

    def play(self):
        scard1 = random.choice(list(Cards.card_values.values()))
        scard2 = random.choice(list(Cards.card_values.values()))
        Player.hand.update(card1 = scard1, card2 = scard2)
        Player.hand_value = sum(Player.hand.values())
        print(f'Welcome {self.player}, here is your hand: a {scard1}, and a {scard2} ')
        print(f'{Fore.BLUE}Your card values equal up to {Fore.BLACK}{scard1 + scard2}')
        if Player.hand_value == 21:
            print(f'{Fore.GREEN}You win! Well not yet..')
            Dealer.play(d)
        Player.hand_value = sum(Player.hand.values())
        while Player.hand_value != 21:
            next_move = input(f'{Fore.RESET}Hit or Pass?: ')
            Player.hand_value = sum(Player.hand.values())

            if next_move in 'pass':
                print(f'You stayed with a total value of: {Player.hand_value} ')
                Dealer.play(d)
                break
            if next_move in 'hit':
                scard3 = random.choice(list(Cards.card_values.values()))
                print('You got a: ' + str(scard3))
                Player.hand.update(card3 = scard3)
                Player.hand_value = sum(Player.hand.values())
                print(Player.hand_value)
                print(Player.hand)

            if Player.hand_value > 21:
                print(f'{Fore.RED}Bust!')
                print('Dealer Wins!')
                quit()

            if Player.hand_value == 21:
                print("You got 21!")
                Dealer.play(d)
                break

            next_move = input('Hit or pass?: ')
            if next_move in 'hit':
                scard4 = random.choice(list(Cards.card_values.values()))
                print(f'You got a {scard4}')
                Player.hand.update(card4 = scard4)
                Player.hand_value = sum(Player.hand.values())
                print(Player.hand_value)
                print(Player.hand)

            if Player.hand_value == 21:
                print("You got 21!")
                Dealer.play(d)
                break

            if next_move in 'pass':
                print(f'You stayed with a total value of: {Player.hand_value} ')
                Dealer.play(d)
                break

            if Player.hand_value > 21:
                print(f'{Fore.RED}Bust!')
                print('Dealer Wins!')
                quit()

            next_move = input('Hit or pass?: ')

            if Player.hand_value == 21:
                print("You got 21!")
                Dealer.play(d)
                break

            if next_move in 'hit':
                scard5 = random.choice(list(Cards.card_values.values()))
                print(f'You got a {scard5}')
                Player.hand.update(card5=scard5)
                Player.hand_value = sum(Player.hand.values())
                print(Player.hand_value)
                print(f'Your Hand: {Player.hand}')

            if Player.hand_value == 21:
                print(f'{Fore.LIGHTGREEN_EX}You got 21!')
                Dealer.play(d)
                break
            if next_move in 'pass':
                print(f'You stayed with a value of {Player.hand_value}')
                Dealer.play(d)
                break
            if Player.hand_value > 21:
                print(f'{Fore.RED}Bust!')
                print('Dealer Wins!')
                quit()


d = Dealer()
insert_player_name_here = ''
p1 = Player(insert_player_name_here)
p1.play()

