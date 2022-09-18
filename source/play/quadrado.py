from xml.sax.handler import property_encoding
from PyQt5.QtWidgets import QWidget


class Quadrado:
    def __init__(self, color: str):
        self.__widget = QWidget()
        self.__color = color
        self.style = self.__getStyle()

        self.__start()

    def __start(self):
        self.__widget.setStyleSheet(self.style)

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __getStyle(self):
        if self.__color == 'white':
            return '''
            *{  
        
                background-color: 'white';
                border: 2px solid 'black';  
            }
            '''
        elif self.__color == 'blue':
            return '''
            *{  
                background-color: 'blue';
                border: 2px solid 'black';  
            }
            '''

        elif self.__color == 'yellow':
            return '''
            *{  
                background-color: 'yellow';
                border: 2px solid 'black';  
            }
            '''

        elif self.__color == 'green':
            return '''
            *{  
                background-color: 'green';
                border: 2px solid 'black';  
            }
            '''

        elif self.__color == 'red':
            return '''
            *{  
                background-color: 'red';
                border: 2px solid 'black';  
            }
            '''

        elif self.__color == 'none':
            return '''
            *{  
                background-color: 'white';
                border: 2px solid 'white';  
            }
            '''
