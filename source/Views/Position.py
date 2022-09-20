from PyQt5.QtWidgets import QWidget
from Config.PositionsColor import PositionsColor


class Position:
    def __init__(self, color: PositionsColor):
        self.__widget = QWidget()
        self.__color = color
        self.__style = self.__getStyle()

        self.__start()

    def __start(self):
        self.__widget.setStyleSheet(self.__style)

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __getStyle(self):
        if self.__color == PositionsColor.WHITE:
            return '''
            *{  
        
                background-color: 'white';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == PositionsColor.BLUE:
            return '''
            *{  
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            '''

        elif self.__color == PositionsColor.YELLOW:
            return '''
            *{  
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            '''

        elif self.__color == PositionsColor.GREEN:
            return '''
            *{  
                background-color: 'green';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == PositionsColor.RED:
            return '''
            *{  
                background-color: 'red';
                border: 2px solid 'black';  
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
