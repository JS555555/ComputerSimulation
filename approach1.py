import math
import numpy as np


class BoardSimulation:

    def __init__(self, board_size=(10, 10), total_iterations=10, number_of_generated_blocks=10):
        self.d = []
        self.board_size = 10
        self.board = np.zeros(board_size)
        self.game_iterations = 0
        self.total_iteriations = total_iterations
        self.number_of_generated_blocks = number_of_generated_blocks
        self.penalty_function = 0
        self.reward_function = 0
        self.objective_function = 0

    def block_generator(self):
        """function generate random block lenght, and number if iterations on the board"""

        for i in range(self.number_of_generated_blocks):

            uniform_number = np.random.uniform(0, 1)

            if 0 <= uniform_number < 1 / 3:
                block_length = 2
                number_of_iterations = np.random.randint(1, 20)
                self.d.append([block_length, number_of_iterations])

            elif 1 / 3 <= uniform_number < 2 / 3:
                block_length = 3
                number_of_iterations = np.random.randint(1, 20)
                self.d.append([block_length, number_of_iterations])

            else:
                block_length = 4
                number_of_iterations = np.random.randint(1, 20)
                self.d.append([block_length, number_of_iterations])

        self.d_array = np.array(self.d)

    def run_simulation(self, show_simulation=True):
        """running the simulation"""

        self.block_generator()  # generating first blocks

        while self.game_iterations <= self.total_iteriations:

            if self.game_iterations % self.number_of_generated_blocks == 0 and self.game_iterations != 0:
                self.d.clear()
                self.block_generator()
            # putting blocks
            for row in enumerate(self.d_array):
                put_block = False
                for board_row in enumerate(self.board):
                    for element in enumerate(board_row[1]):
                        # checking if block can be put
                        if element[1] == 0 and board_row[0] + row[1][0] <= math.sqrt(self.board.size) and element[0] + \
                                row[1][0] <= math.sqrt(self.board.size) \
                                and self.board[board_row[0] + row[1][0] - 1][element[0] + row[1][0] - 1] == 0 \
                                and self.board[board_row[0] + row[1][0] - 1][element[0]] == 0 \
                                and self.board[board_row[0]][element[0] + row[1][0] - 1] == 0:
                            # putting a block
                            for i in range(row[1][0]):
                                self.board[board_row[0] + i][element[0] + i] = row[1][1]
                                self.board[board_row[0]][element[0] + i] = row[1][1]
                                self.board[board_row[0] + i][element[0]] = row[1][1]
                                self.board[board_row[0] + 1][element[0] + i] = row[1][1]
                                self.board[board_row[0] + i][element[0] + 1] = row[1][1]
                                if row[1][0] == 4:
                                    self.board[board_row[0] + 2][element[0] + i] = row[1][1]
                                    self.board[board_row[0] + i][element[0] + 2] = row[1][1]
                            put_block = True
                            break
                    if put_block:
                        if show_simulation:
                            print(self.board)
                            print("--------------------------------------------")
                        break

                # increasing penality function
                if not put_block:
                    self.penalty_function += row[1][0] + row[1][1]


                self.board -= np.ones(self.board_size)
                self.board[self.board < 0] = 0

                self.reward_function += np.count_nonzero(self.board)

                self.game_iterations += 1

