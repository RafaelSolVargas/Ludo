from Config.PositionsColor import PositionsColor
from PyQt5.QtWidgets import QWidget

#TODO: adicionar classe ao diagrama de classes de interface
class EndHouse:
    def __init__(self, color: PositionsColor):
        self.__widget = QWidget()

        self.__color = color

        self.__defaultStyle = self.__getStyle()

        self.__widget.setStyleSheet(self.__defaultStyle)

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __getStyle(self):

        if self.__color == PositionsColor.BLUE:
            return '''
            *{  
                background-color: 'blue';
                width: 55%;
                height: 55%;    
            }
            '''

        elif self.__color == PositionsColor.YELLOW:
            return '''
            *{  
                background-color: 'yellow';
                width: 55%;
                height: 55%; 
                width: 55%;
                height: 55%;     
            }
            }
            '''

        elif self.__color == PositionsColor.GREEN:
            return '''
            *{  
                background-color: 'green';
                width: 55%;
                height: 55%;    
            }
            '''
        elif self.__color == PositionsColor.RED:
            return '''
            *{  
                background-color: 'red';
                width: 55%;
                height: 55%;  
            }
            '''

        elif self.__color == PositionsColor.FULL:
            return '''
                *{  
                    border-top: 30px solid yellow;
                    border-right: 30px solid blue;
                    border-bottom: 30px solid green;
                    border-left: 30px solid red;
                    width: 55%;
                    height: 55%;  
                }
                '''
        elif self.__color == PositionsColor.RED_YELLOW:
            return '''
                *{  
                    border-right: 30px solid yellow;
                    border-top: 30px solid yellow;
                    border-left: 30px solid red;
                    border-bottom: 30px solid red;
                    width: 55%;
                    height: 55%;  
                }
                '''
        elif self.__color == PositionsColor.RED_GREEN:
            return '''
                *{  
                    border-bottom: 30px solid green;
                    border-right: 30px solid green;
                    border-left: 30px solid red;
                    border-top: 30px solid red;
                    width: 55%;
                    height: 55%;  
                }
                '''
        elif self.__color == PositionsColor.BLUE_GREEN:
            return '''
                *{  
                    border-top: 30px solid blue;
                    border-right: 30px solid blue;
                    border-left: 30px solid green;
                    border-bottom: 30px solid green;
                    width: 55%;
                    height: 55%;  
                }
                '''
        elif self.__color == PositionsColor.BLUE_YELLOW:  # Blue_Yellow
            return '''
                *{  
                    border-top: 30px solid yellow;
                    border-left: 30px solid yellow;
                    border-right: 30px solid blue;
                    border-bottom: 30px solid blue;
                    width: 55%;
                    height: 55%;  
                }
                '''
