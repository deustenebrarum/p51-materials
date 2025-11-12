from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def update(self, game):
        ...

    @abstractmethod
    def draw(self, game):
        ...
