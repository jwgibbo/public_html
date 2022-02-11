class Stack:
    #assume __init__ and push

    def pop(self):
        if self._top != None:
            self._top  = self._top.next
        else:
            raise RuntimeError('Stack empty')

    def peek(self):
        if self._top != None:
            return self._top.entry
        else:
            raise RuntimeError('Stack empty')
