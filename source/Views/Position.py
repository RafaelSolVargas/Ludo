from Config.PositionsColor import PositionsColor
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore


class Position:
    def __init__(self, color: PositionsColor):
        self.__widget = QPushButton()
        self.__selected: bool = False
        self.__widget.setFixedHeight(55)
        self.__widget.setFixedWidth(55)

        self.__color = color
        self.__configureClick()

        self.__defaultStyle = self.__getStyle()
        self.__selectedStyle = '''
            *{  
                background-color: 'grey';
                border: 4px solid 'black';  
            }
        '''
        self.__widget.setStyleSheet(self.__defaultStyle)

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

    @property
    def widget(self) -> QPushButton:
        return self.__widget

    def __getStyle(self):
        if self.__color == PositionsColor.WHITE:
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'black';  
            }
            *:hover{
                background-color: 'grey';
                border: 4px solid 'black';  
            }
            '''
        elif self.__color == PositionsColor.BLUE:
            return '''
            *{  
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            *:hover{
                background-color: 'grey';
                border: 4px solid 'black';  
            }
            '''

        elif self.__color == PositionsColor.YELLOW:
            return '''
            *{  
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            *:hover{
                background-color: 'grey';
                border: 4px solid 'black';  
            }
            '''

        elif self.__color == PositionsColor.GREEN:
            return '''
            *{  
                background-color: 'green';
                border: 2px solid 'black';  
            }
            *:hover{
                background-color: 'grey';
                border: 4px solid 'black';  
            }
            '''
        elif self.__color == PositionsColor.RED:
            return '''
            *{  
                background-color: 'red';
                border: 2px solid 'black';  
            }
            *:hover{
                background-color: 'grey';
                border: 4px solid 'black';  
            }
            '''
        elif self.__color == PositionsColor.NONE:
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'white';  
            }
            '''
        elif self.__color == PositionsColor.FULL:
            return '''
                *{  
                    border-top: 30px solid yellow;
                    border-right: 30px solid blue;
                    border-bottom: 30px solid green;
                    border-left: 30px solid red
                }
                '''
        elif self.__color == PositionsColor.RED_YELLOW:
            return '''
                *{  
                    border-top: 100px solid yellow;
                    border-left: 100px solid red
                }
                '''
        elif self.__color == PositionsColor.RED_GREEN:
            return '''
                *{  
                    border-bottom: 100px solid green;
                    border-left: 100px solid red
                }
                '''
        elif self.__color == PositionsColor.BLUE_GREEN:
            return '''
                *{  
                    border-right: 100px solid blue;
                    border-bottom: 100px solid green;
                }
                '''
        else:  # Blue_Yellow
            return '''
                *{  
                    border-left: 100px solid yellow;
                    border-bottom: 100px solid blue;
                }
                '''
