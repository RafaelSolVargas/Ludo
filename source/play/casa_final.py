from PyQt5.QtWidgets import QWidget


class CasaFinal:
    def __init__(self, styleType: str):
        self.__widget = QWidget()
        self.__style = self.__getStyle(styleType)
        self.__start()

    @property
    def widget(self) -> QWidget:
        return self.__widget

    def __getStyle(self, buttonType: str):
        if buttonType == 'full':
            return '''
                *{  
                    border-top: 30px solid yellow;
                    border-right: 30px solid blue;
                    border-bottom: 30px solid green;
                    border-left: 30px solid red
                }
                '''

        elif buttonType == 'red':
            return '''
                *{  
                    background-color : red
                }
                '''

        elif buttonType == 'green':
            return '''
                *{  
                    background-color : green
                }
                '''

        elif buttonType == 'blue':
            return '''
                *{  
                    background-color : blue
                }
                '''

        elif buttonType == 'yellow':
            return '''
                *{  
                    background-color : yellow
                }
                '''

        elif buttonType == 'red-yellow':
            return '''
                *{  
                    border-top: 100px solid yellow;
                    border-left: 100px solid red
                }
                '''

        elif buttonType == 'red-green':
            return '''
                *{  
                    border-bottom: 100px solid green;
                    border-left: 100px solid red
                }
                '''

        elif buttonType == 'green-blue':
            return '''
                *{  
                    border-right: 100px solid blue;
                    border-bottom: 100px solid green;
                }
                '''

        elif buttonType == 'blue-yellow':

            return '''
                *{  
                    border-left: 100px solid yellow;
                    border-bottom: 100px solid blue;
                }
                '''

    def __start(self):

        self.__widget.setStyleSheet(self.__style)
