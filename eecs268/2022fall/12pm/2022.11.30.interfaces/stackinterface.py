from stackinterface import StackInterface


class StackAsList(StackInterface):
    def __init__(self):
        self._stack_list = []
