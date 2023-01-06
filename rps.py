import random
from tenacity import *


def check_choice(choice):
    if choice not in ["rock", "paper", "scissors"]:
        raise ValueError("Invalid choice")


def random_choice():
    return random.choice(["rock", "paper", "scissors"])


class Player:
    choice: str

    def __init__(self, choice: str):
        check_choice(choice)
        self.choice = choice


class Round:
    _p1: Player
    _p2: Player

    def __init__(self, p1: Player, p2: Player):
        self.p1 = p1
        self.p2 = p2

    def play(self):
        print(f"p1 plays {self.p1.choice}")
        print(f"p2 plays {self.p2.choice}")

        if self.p1.choice == self.p2.choice:
            print("Draw\n-")
            return "draw"
        elif self.p1.choice == "rock" and self.p2.choice == "scissors":
            print("p1 wins\n-")
            return "p1"
        elif self.p1.choice == "scissors" and self.p2.choice == "paper":
            print("p2 wins\n-")
            return "p2"
        elif self.p1.choice == "paper" and self.p2.choice == "rock":
            print("p1 wins\n-")
            return "p1"
        else:
            print("p2 wins\n-")
            return "p2"


def init_failed(value):
    print("Please enter rounds as a valid whole number.\n------------------------")
    return value is None


def return_last_value(_last_state):
    print("Failed to start game. Exiting.")
    quit(1)


class Tournament:
    p1_wins = 0
    p2_wins = 0
    draws = 0
    rounds = 0

    @retry(stop=stop_after_attempt(3),
           retry=retry_if_result(init_failed),
           retry_error_callback=return_last_value)
    def __init__(self):
        try:
            self.rounds = int(input("How many rounds do you want to play? \n"))
        except ValueError:
            pass

    def start(self):
        for i in range(self.rounds):
            print('--------------- ROUND {} ---------------'.format(i + 1))
            option = input("Player 1, enter your option: \n")

            _p1 = Player(option)
            _p2 = Player(random_choice())

            game = Round(_p1, _p2)
            winner = game.play()

            match winner:
                case "p1":
                    self.p1_wins += 1
                case "p2":
                    self.p2_wins += 1
                case "draw":
                    self.draws += 1

    def print_results(self):
        print("--------------- RESULTS ---------------")
        print(f"p1 win count: {self.p1_wins}")
        print(f"p2 win count: {self.p2_wins}")
        print(f"draw count: {self.draws}")

        if self.p1_wins > self.p2_wins:
            print(f"Player 1 wins the game with {self.p1_wins} wins")
        elif self.p2_wins > self.p1_wins:
            print(f"Player 2 wins the game with {self.p2_wins} wins")
        else:
            print("Draw")


def main():
    tournament = Tournament()
    tournament.start()
    tournament.print_results()


main()
