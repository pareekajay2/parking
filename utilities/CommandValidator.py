import abc


class CommandValidator(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'is_valid') and
                callable(subclass.is_valid))

    @abc.abstractmethod
    def is_valid(self):
        raise NotImplementedError
