from functools import partial
import random

from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *

class Tic_Tac_Toe(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('Tic_Tac_Toe.ui', None)
        self.ui.show()

        self.game = [[self.ui.btn_1, self.ui.btn_2, self.ui.btn_3],
                     [self.ui.btn_4, self.ui.btn_5, self.ui.btn_6],
                     [self.ui.btn_7, self.ui.btn_8, self.ui.btn_9]]

        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].clicked.connect(partial(self.play, i, j))

        self.ui.new_game.clicked.connect(self.new_game)

        self.counter = 0
        self.score_X = 0
        self.score_O = 0
        self.score_draws = 0
        self.winner = ''
    
    def play(self, i, j):
        if self.ui.player_player.isChecked():
            if self.game[i][j].text() == '' and self.winner == '':
                if self.counter % 2 == 0:
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color: yellow; background-color: purple; font: 700 20pt "Segoe UI"')
                else:
                    self.game[i][j].setText('O')
                    self.game[i][j].setStyleSheet('color: lightblue; background-color: red; font: 700 20pt "Segoe UI"')

                self.counter += 1

        elif self.ui.player_cpu.isChecked():
            if self.game[i][j].text() == '' and self.winner == '':
                if self.counter % 2 == 0:
                    self.game[i][j].setText('X')
                    self.game[i][j].setStyleSheet('color: yellow; background-color: purple; font: 700 20pt "Segoe UI"')
                    self.counter += 1

                    if self.counter != 9:
                        while True :
                            row = random.randint(0,2)
                            col = random.randint(0,2)
                            if self.game[row][col].text() == '':
                                self.game[row][col].setText('O')
                                self.game[row][col].setStyleSheet('color: lightblue; background-color: red; font: 700 20pt "Segoe UI"')
                                self.counter += 1
                                break
         
        self.check()
        self.who_winner()

    def check(self):
        for i in range(3):
            if self.game[i][0].text() == self.game[i][1].text() == self.game[i][2].text():
                if self.game[i][0].text() == 'X':
                    self.winner = 'X'
                elif self.game[i][0].text() == 'O':
                    self.winner = 'O'
            
            elif self.game[0][i].text() == self.game[1][i].text() == self.game[2][i].text():
                if self.game[0][i].text() == 'X':
                    self.winner = 'X'
                elif self.game[0][i].text() == 'O':
                    self.winner = 'O'
        
        if self.game[0][0].text() == self.game[1][1].text() == self.game[2][2].text():
            if self.game[0][0].text() == 'X':
                self.winner = 'X'
            elif self.game[0][0].text() == 'O':
                self.winner = 'O'

        if self.game[0][2].text() == self.game[1][1].text() == self.game[2][0].text():
            if self.game[0][2].text() == 'X':
                self.winner = 'X'
            elif self.game[0][2].text() == 'O':
                self.winner = 'O'

    def who_winner(self):
        if self.winner != '' :
            msgBox = QMessageBox()
            msgBox.setText(self.winner + '\n Winner!')
            msgBox.exec()
        elif self.winner == '' and self.counter == 9:
            self.score_draws += 1
            self.ui.draw.setText('Draws :   ' + str(self.score_draws))
            msgBox = QMessageBox()
            msgBox.setText('X O Draw!')
            msgBox.exec()

        if self.winner == 'X' :
            self.score_X += 1
            self.ui.player_X.setText('Player_X :   ' + str(self.score_X))
        elif self.winner == 'O' :
            self.score_O += 1
            self.ui.player_O.setText('Player_O :   ' + str(self.score_O))

    def new_game(self):
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('background-color: pink')
        
        self.counter = 0
        self.winner = ''

app = QApplication()
window = Tic_Tac_Toe()

app.exec()