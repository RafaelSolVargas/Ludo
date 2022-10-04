from Config.PositionsColor import PositionsColor
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore


class Position:
    def __init__(self, color: PositionsColor):
        self.__widget = QPushButton()
        self.__selected: bool = False

        self.__color = color
        self.__configureClick()

        self.__defaultStyle = self.__getStyle()
        self.__selectedStyle = '''
            *{  
                background-color: 'grey';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;   
            }
        '''
        self.__widget.setStyleSheet(self.__defaultStyle)

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected) -> bool:
        self.__selected = selected
        if self.__selected:
            self.__widget.setStyleSheet(self.__defaultStyle)
        else:
            self.__widget.setStyleSheet(self.__selectedStyle)

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    def __configureClick(self) -> None:
        if (self.__color in [PositionsColor.BLUE, PositionsColor.YELLOW,
                             PositionsColor.RED, PositionsColor.GREEN, PositionsColor.WHITE]):
            self.__widget.clicked.connect(lambda: self.__selectPosition())
            self.__widget.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        else:
            self.__widget.setDisabled(True)

    def __selectPosition(self):
        if self.__selected:
            self.__selected = False
            self.__widget.setStyleSheet(self.__defaultStyle)
        else:
            self.__selected = True
            self.__widget.setStyleSheet(self.__selectedStyle)

    def __getStyle(self):

        if self.__color == PositionsColor.WHITE:
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;  
            }
            *:hover{
                background-color: 'grey';
            }
            '''
        elif self.__color == PositionsColor.BLUE:
            return '''
            *{  
                background-color: 'blue';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;    
            }
            *:hover{
                background-color: 'grey';
            }
            '''

        elif self.__color == PositionsColor.YELLOW:
            return '''
            *{  
                background-color: 'yellow';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;   
            }
            *:hover{
                background-color: 'grey';
            }
            '''

        elif self.__color == PositionsColor.GREEN:
            return '''
            *{  
                background-color: 'green';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;   
            }
            *:hover{
                background-color: 'grey';
            }
            '''
        elif self.__color == PositionsColor.RED:
            return '''
            *{  
                background-color: 'red';
                border: 2px solid 'black';
                width: 55%;
                height: 55%;    
            }
            *:hover{
                background-color: 'grey';
            }
            '''
        elif self.__color == PositionsColor.NONE:
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'white';
                width: 55%;
                height: 55%;     
            }
            '''
