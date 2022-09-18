from PyQt5.QtWidgets import QWidget, QGridLayout
from Config.HouseColor import HouseColor
from play.casa_inicial_pos import CasaInicialPos


class House:
    def __init__(self, color: HouseColor):
        self.__widget = QWidget()
        self.__color = color
        self.__grid = QGridLayout()
        self.__style = self.__getStyle()
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __setGrid(self) -> None:
        for l in range(2):
            for c in range(2):
                self.__grid.addWidget(CasaInicialPos(self.__color).widget, l,  c)

    def __start(self) -> None:
        self.__widget.setStyleSheet(self.__style)
        self.__setGrid()
        self.__widget.setLayout(self.__grid)

    def __getStyle(self):
        if self.__color == HouseColor.BLUE:
            return '''
            *{  
                border-radius: 161px;
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == HouseColor.YELLOW:
            return '''
            *{  
                border-radius: 161px;
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == HouseColor.GREEN:
            return '''
            *{  
                border-radius: 161px;
                background-color: 'green';
                border: 2px solid 'black';  
            }
            '''
        else:  # Red
            return '''
            *{  
                border-radius: 161px;
                background-color: 'red';
                border: 2px solid 'black';  
            }
            '''
