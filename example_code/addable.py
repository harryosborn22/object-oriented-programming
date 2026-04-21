from abc import ABC, abstractmethod


class Addable(ABC):

    @abstractmethod
    def __add__(self, other):
        return NotImplemented

    @classmethod
    def __subclasshook__(cls, c):
        if cls is not Addable:
            return NotImplemented
        for b in c.__mro__:
            if "__add__" in b.__dict__:
                if b.__dict__["__add__"] is None:
                    return NotImplemented
                return True
        return NotImplemented
