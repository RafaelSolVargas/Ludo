from abc import ABC, abstractmethod


class DogPlayerInterface(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def receive_start(self, start_status):
        pass

    @abstractmethod
    def receive_move(self, a_move):
        pass

    @abstractmethod
    def receive_withdrawal_notification(self):
        pass
