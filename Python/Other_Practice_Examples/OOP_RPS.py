import random
import string
import re

class Player:
    def __init__(self, score):
        self.score = 0
        self.moves = ["rock", "paper", "scissors"]
    
    def move(self):
        move1 = input("rock, paper, or scissors? ")
        if move1 in self.moves:
            return move1
        else:
            print("Please pick one of the options. ")
            

    # def learn(self, move1, move2):
    #     self.move1 = self.p1.move
    #     self.move2 = self.p2.move

    # def beats(self, one, two):
    #     one = self.move1
    #     two = self.move2
    #     if ((one == "rock") and (two == "scissors") or 
    #         (one == "scissors") and (two == "paper") or 
    #         (one == "paper") and (two == "rock")):
    #         print("**PLAYER ONE WINS**")
    #         self.p1.score += 1
    #     elif (one == two):
    #         print("IT'S A TIE!")
    #         num_of_rounds += 1
    #     else:
    #         print("**PLAYER TWO WINS**")
    #         self.p2.score += 1
    #     print(f"Player 1: {self.p1.score} : Player 2: {self.p2.score}")

class Rock_Player(Player):
    def move(self):
        return "rock"

class Loop_Player(Player):
    def move(self):
        index = 0
        for move in self.moves:
            return move[index]
        index += 1

class Random_Player(Player):
    def move(self):
        return random.choice(self.moves)

class Imitation_Player(Player):
    def move(self):
        self.learn()
        if (round == 1):
            self.p2.move = random.choice(self.moves)
        else:
            self.p2.move = p1_move[round - 1]


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def score(self):
        if (self.p1.score > self.p2.score):
            print("PLAYER ONE IS THE CHAMPION")
        else:
            print("PLAYER TWO IS THE CHAMPION")

    def beats(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if (move1 == move2):
            print("**IT'S A TIE**")
            num_of_rounds += 1
        elif ((move1 == "rock") and (move2 == "scissors") or 
            (move1 == "scissors") and (move2 == "paper") or
            (move1 == "paper") and (move2 == "rock")):
            print("**PLAYER ONE WINS**")
        else:
            print("**PLAYER TWO WINS**")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.beats()
        
        # self.p1.learn(move1, move2)
        # self.p2.learn(move2, move1)

    def play_game(self):
        while True:
            try: 
                num_of_rounds = int(input("Please enter the number of rounds you wish to play: "))
                print("Game start!")
                for round in range(num_of_rounds):
                    print(f"Round {round + 1}:")
                    self.play_round()
                self.score()
                print("Game over!")
            except (ValueError, TypeError):
                print("That's not a valid number.")

if __name__ == '__main__':
    game = Game(Player(0), Rock_Player(0))
    game.play_game()
