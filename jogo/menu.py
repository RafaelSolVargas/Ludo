import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from option_button import OptionButton
from play_button import PlayButton
from logo import Logo
from play.game import Game
class Menu:
    def __init__(self, width = 640):
        self.width = width
        self.app = QApplication(sys.argv)
        self.window = QWidget()
        self.grid = QGridLayout()

        self.widgets = {
            "n_players_buttons": [],
            "n_pins_buttons": [],
            "logos": [],
            "play_button": []
        }
    
    def window_set(self):
        self.window.setWindowTitle(' ')
        self.window.setStyleSheet("background: black;")
        self.window.move(640, 108)


    def create_widgets(self):
        self.widgets['logos'].append(Logo("n_o_pins_logo.png", 50))
        self.widgets['logos'].append(Logo("ludo_logo.png", 25))
        self.widgets['logos'].append(Logo("n_o_players_logo.png", 50))
        

        for i in range(4):
            b = OptionButton(i+1)
            self.widgets['n_players_buttons'].append(b)
            
        for i in range(4):
            b = OptionButton(i+1)
            self.widgets['n_pins_buttons'].append(b)

        p_b = PlayButton('PLAY')
        p_b.widget.clicked.connect(self.play)
        self.widgets['play_button'].append(p_b) 

    def set_grids(self):
        n_pins_grid = QGridLayout()
        n_players_grid = QGridLayout()

        for k in self.widgets:
            
            linha = None
            if k == 'logos':
                for i in self.widgets[k]:
                    
                    if i.image == 'n_o_players_logo.png':
                        
                        linha = 1
                    elif i.image == 'ludo_logo.png':

                        linha = 0
                    elif i.image == 'n_o_pins_logo.png':
                        
                        linha = 3

                    self.grid.addWidget(i.widget, linha , 0)    

            elif k == "n_pins_buttons":
               
                for i in self.widgets[k]:
                    
                    coluna = i.number - 1
                   
                    n_pins_grid.addWidget(i.widget, 0, coluna)

                self.grid.addLayout(n_pins_grid, 4, 0)
        
            elif k == "n_players_buttons":
                
                for i in self.widgets[k]:
                    
                    coluna = i.number - 1
                    
                    n_players_grid.addWidget(i.widget, 0, coluna)

                self.grid.addLayout(n_players_grid, 2, 0)

            elif k == "play_button":
                
                self.grid.addWidget(self.widgets[k][0].widget, 5 ,0)


    def clear(self):
        for v in self.widgets.values():
            if v != []:
                for i in v:
                    i.widget.hide()
                for i in range(len(v)):
                    v.pop()

            

    def play(self):
        self.clear()
        self.window.setStyleSheet("background: white;")
        self.window.setWindowTitle('LUDO')
        
        self.grid.addWidget(Game().widget, 0, 0)

    def run(self):
        
        self.window_set()

        self.create_widgets()
        
        self.set_grids()
        

        self.window.setLayout(self.grid)

        self.window.show()
        sys.exit(self.app.exec())

interface = Menu()

interface.run()