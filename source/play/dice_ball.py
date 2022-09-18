from PyQt5.QtWidgets import QWidget


class DiceBall:
    def __init__(self, diceType: str, width: int) -> None:
        self.__widget = QWidget()
        self.__width = width
        self.__diceType = diceType
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __start(self):
        self.__setWindow()

    def __setWindow(self):
        self.__widget.setFixedHeight(self.__width)
        self.__widget.setFixedWidth(self.__width)
        self.__widget.setStyleSheet(self.__getStyle())

    def __getStyle(self):
        if self.__diceType == 'white':
            return '''
                *{  
                    border-color: white;
                    border-radius: 8px;
                    background-color: white;
                }
                '''

        elif self.__diceType == 'black':
            return '''
                *{  
                    border-color: black;
                    border-radius : 8px;
                    background-color: black;
                }
                '''
