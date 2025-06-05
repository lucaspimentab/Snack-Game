import abc

class Entity(abc.ABC):
    @abc.abstractmethod
    def desenhar(self, tela):
        pass

    @abc.abstractmethod
    def get_pos(self):
        pass
