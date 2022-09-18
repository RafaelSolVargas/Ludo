from PyQt5.QtWidgets import QWidget, QGridLayout
from play.casa_inicial_pos import CasaInicialPos


class CasaInicial:
    def __init__(self, cor: str):
        self.__widget = QWidget()
        self.__color = cor
        self.__grid = QGridLayout()
        self.__style = self.__getStyle()
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __getStyle(self):
        if self.__color == 'white':
            return '''
            *{  
                border-radius: 161px;
                background-color: 'white';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == 'blue':
            return '''
            *{  
                border-radius: 161px;
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == 'yellow':
            return '''
            *{  
                border-radius: 161px;
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == 'green':
            return '''
            *{  
                border-radius: 161px;
                background-color: 'green';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == 'red':
            return '''
            *{  
                border-radius: 161px;
                background-color: 'red';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == 'none':
            return '''
            *{  
                border-radius: 161px;
                background-color: 'white';
                border: 2px solid 'white';  
            }
            '''

    def __setGrid(self) -> None:
        for l in range(2):
            for c in range(2):
                self.__grid.addWidget(CasaInicialPos(self.__color).widget, l,  c)

    def __start(self) -> None:
        self.__widget.setStyleSheet(self.__style)
        self.__setGrid()
        self.__widget.setLayout(self.__grid)
