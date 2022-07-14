import random
import string
import re


moves = ['rock', 'paper', 'scissors']

class Game:
    
    def valid_num(prompt):
        while True:
            choice = input(prompt)
            if choice != '[0-9]':
                print('Please enter a number. ')
                valid_num(prompt)

    num_of_rounds = valid_num("Please enter the number of rounds you wish to play: ")

    def __init__(self, p1, p2):
        # the variable name we give to each Player object so that they know their name reference
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f'Round {round + 1}: ')
        print(f'Player 1: {move1} \n Player 2: {move2}')
        # self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print('Game start!')
        for round in range(num_of_rounds):
            # the game object will call this method
            self.play_game()

class Player:
    def __init__(self, score):
        self.p1.score = 0
        self.p2.score = 0

    def valid_input(prompt):
        choice = input(prompt).lower().strip(string.punctuation)
        if ((choice in prompt) and (choice != 'or')):
            return
        else:
            print('Please enter a valid choice: ')
            valid_input(prompt)
   
    def learn(self, my_move, their_move):
        self.my_move = p1.move()
        self.their_move = p2.move()
    
    def move():
        move1 = valid_input('Rock, Paper, or Scissors? ')

class Rock_Player:
    def move(self):
        return 'rock'

class Loop_Player:
    def move(self):
        for move in moves:
            return move[round]

class Random_Player:
    def move(self):
        return random.choice(moves)

class Imitation_Player:
    def move(self):
        their_move = self.p2.learn(my_move)
        self.p2.move = their_move
        
if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
        
